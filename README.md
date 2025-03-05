# AwakenTax-futures-and-perpetuals-to-TurboTax Converter

This repository contains a Python script to convert Awaken Tax futures/perpetuals transaction files into a CSV format compatible with TurboTax for IRS Form 8949 reporting. The script processes transaction data, calculates capital gains and losses, and ensures the total profit matches the provided Awaken Tax figure (dynamically adjustable based on the dataset).

## Overview

Awaken Tax provides transaction data where expenses for futures are realized when positions are opened, complicating traditional tax reporting. This tool:
- Handles "Open Position," "Close Position," and specific close transactions (e.g., "Close Long Position (SOL)").
- Dynamically allocates cost basis from open positions to generic closes based on their proportion of total proceeds.
- Generates a CSV file with columns required by TurboTax: `Description`, `Date Acquired`, `Date Sold`, `Proceeds`, `Cost Basis`, and `Gain or Loss`.

## Prerequisites

- **Python 3.6 or higher** (recommended: latest version, e.g., 3.11 or 3.12).
- **pip** (Python package manager, included with Python installation).
- **pandas** library for data processing.

## Installation

### 1. Install Python
If you don’t have Python installed:
- Download the latest version from [python.org/downloads](https://www.python.org/downloads/).
- During installation, check **"Add Python to PATH"** (Windows) and complete the setup.
- Verify installation by running `python --version` or `python3 --version` in your terminal.

### 2. Install pip
pip should come with Python. To ensure it’s installed or upgraded:
- Run: `python -m ensurepip --upgrade` and `python -m pip install --upgrade pip`.
- Verify with `pip --version` or `pip3 --version`.

### 3. Install pandas
Install the required pandas library:
- Run: `pip install pandas` or `pip3 install pandas`.
- Verify with `pip show pandas`.

## Usage

### 1. Prepare Your Data
- Save your Awaken Tax dataset as `awaken_data.csv` with the following columns:
  - `Notes` (e.g., "Close Long Position (SOL)", "Open Position")
  - `Date` (e.g., "09-02-2024 (UTC)")
  - `Proceeds (USD)` (e.g., 23634.84)
  - `Expenses (USD)` (e.g., -23609.03)
  - `Fees (USD)` (e.g., -7.49)
  - `Profit (USD)` (e.g., 18.32)
- Place `awaken_data.csv` in the same directory as the script.
- Ensure the dataset reflects the total profit you want to match (e.g., edit the last row’s "Profit (USD)" if necessary to align with your Awaken Tax report).

### 2. Run the Script
- Save the provided Python script as `convert_to_turbotax.py` in the same directory.
- Open a terminal, navigate to the directory (e.g., `cd path\to\directory`), and run: `python convert_to_turbotax.py` or `python3 convert_to_turbotax.py`
- The script will generate `turbotax_output.csv` with the converted data.

### 3. Verify Output
- Open `turbotax_output.csv` in a spreadsheet program (e.g., Excel).
- Ensure the total "Gain or Loss" matches the sum of "Profit (USD)" from your `awaken_data.csv` (the script adjusts the last row for rounding).
- Import the file into TurboTax under the "Stocks, Cryptocurrency, and Other Investments" section.

## Script Details

The script (`convert_to_turbotax.py`) performs the following:
- Loads the `awaken_data.csv` file using pandas.
- Separates transactions into specific closes (asset-specific) and generic closes.
- Calculates the total cost basis dynamically from "Open Position" rows (sum of absolute "Expenses (USD)" and "Fees (USD)").
- Calculates the total proceeds dynamically from "Close Position" rows.
- Allocates cost basis to generic closes based on their proportion of total proceeds.
- Combines data into a TurboTax-compatible format.
- Adjusts the final gain/loss to match the total "Profit (USD)" from the input file.

## Example Output
The output CSV includes:
- `Description`: Transaction type (e.g., "Close Long Position (SOL)").
- `Date Acquired`: Same as `Date Sold` (short-term assumption) or blank.
- `Date Sold`: Transaction date.
- `Proceeds`: Sale amount in USD.
- `Cost Basis`: Calculated cost (expenses + fees for specific closes, allocated for generic closes).
- `Gain or Loss`: Profit or loss in USD.
## Contributing
- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Commit changes (`git commit -m "Description"`).
- Push to the branch (`git push origin feature-name`).
- Open a Pull Request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Thanks to the Awaken Tax team for providing the dataset structure.

---

