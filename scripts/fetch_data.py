from pathlib import Path
from zipfile import ZipFile
from urllib.request import urlretrieve

import pandas as pd


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

DATA_URL = (
    "https://files.grouplens.org/datasets/movielens/"
    "ml_belief_2024_data_release_2.zip"
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
ZIP_PATH = RAW_DIR / "ml_belief_2024_data_release_2.zip"
EXTRACT_DIR = RAW_DIR / "ml_belief_2024"

# -------------------------------------------------------------------
# Download
# -------------------------------------------------------------------

def download_dataset():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if ZIP_PATH.exists():
        print(f"Dataset already downloaded: {ZIP_PATH}")
        return

    print("Downloading MovieLens Beliefs Dataset...")
    print(f"URL: {DATA_URL}")

    urlretrieve(DATA_URL, ZIP_PATH)

    print(f"Downloaded to: {ZIP_PATH}")


# -------------------------------------------------------------------
# Extract
# -------------------------------------------------------------------

def extract_dataset():
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

    # Avoid extracting again if files already exist
    if any(EXTRACT_DIR.iterdir()):
        print(f"Dataset already extracted: {EXTRACT_DIR}")
        return

    print("Extracting dataset...")

    with ZipFile(ZIP_PATH, "r") as zip_file:
        zip_file.extractall(EXTRACT_DIR)

    print(f"Extracted to: {EXTRACT_DIR}")


# -------------------------------------------------------------------
# Inspect files
# -------------------------------------------------------------------

def list_files():
    print("\nFiles in dataset:")
    print("-" * 50)

    for path in sorted(EXTRACT_DIR.rglob("*")):
        if path.is_file():
            print(path.relative_to(EXTRACT_DIR))


# -------------------------------------------------------------------
# Load CSVs
# -------------------------------------------------------------------

def load_csvs():
    csv_files = [
        path
        for path in EXTRACT_DIR.rglob("*.csv")
        if not path.name.startswith("._")
    ]

    print("\nCSV files:")
    print("-" * 50)

    for path in csv_files:
        print(path.relative_to(EXTRACT_DIR))

    data = {}

    for path in csv_files:
        name = path.stem

        print(f"\nLoading {name}.csv...")
        df = pd.read_csv(path)

        data[name] = df

        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")

    return data


# -------------------------------------------------------------------
# Basic exploration
# -------------------------------------------------------------------

def inspect_data(data):
    for name, df in data.items():
        print("\n" + "=" * 70)
        print(name)
        print("=" * 70)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nFirst 5 rows:")
        print(df.head())

        print("\nData types:")
        print(df.dtypes)

        print("\nMissing values:")
        print(df.isna().sum())

        print("\nUnique values:")
        for column in df.columns:
            print(f"  {column}: {df[column].nunique():,}")


# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------

def main():
    download_dataset()
    extract_dataset()
    list_files()

    data = load_csvs()
    inspect_data(data)


if __name__ == "__main__":
    main()