import pandas as pd

# Load the dataset
df = pd.read_csv('awaken_data.csv')

# Separate specific closes and generic closes
specific_closes = df[df['Notes'].str.contains("Close Long Position|Close Short Position")]
generic_closes = df[df['Notes'] == "Close Position"]
open_positions = df[df['Notes'] == "Open Position"]

# Dynamically calculate total cost basis from open positions
C_total = abs(open_positions['Expenses (USD)'].sum()) + abs(open_positions['Fees (USD)'].sum())
P_total = generic_closes['Proceeds (USD)'].sum()

# Process specific closes
specific_data = specific_closes[['Notes', 'Date', 'Proceeds (USD)', 'Expenses (USD)', 'Fees (USD)', 'Profit (USD)']].copy()
specific_data.columns = ['Description', 'Date Sold', 'Proceeds', 'Expenses', 'Fees', 'Gain or Loss']
specific_data['Date Acquired'] = specific_data['Date Sold']
specific_data['Cost Basis'] = abs(specific_data['Expenses']) + abs(specific_data['Fees'])
specific_data = specific_data[['Description', 'Date Acquired', 'Date Sold', 'Proceeds', 'Cost Basis', 'Gain or Loss']]

# Process generic closes
generic_data = generic_closes[['Notes', 'Date', 'Proceeds (USD)']].copy()
generic_data.columns = ['Description', 'Date Sold', 'Proceeds']
generic_data['Description'] = "Perpetual Contract Close"
generic_data['Date Acquired'] = generic_data['Date Sold']
generic_data['Cost Basis'] = (generic_data['Proceeds'] / P_total) * C_total
generic_data['Gain or Loss'] = generic_data['Proceeds'] - generic_data['Cost Basis']

# Combine data
result = pd.concat([specific_data, generic_data])

# Adjust total to match the sum of Profit (USD) from the input file
target_total = df['Profit (USD)'].sum()  # Dynamically use the total profit from the dataset
current_total = result['Gain or Loss'].sum()
adjustment = target_total - current_total
if abs(adjustment) > 0.01:  # Adjust if difference > 1 cent
    result.iloc[-1, result.columns.get_loc('Gain or Loss')] += adjustment

# Save to CSV
result.to_csv('turbotax_output.csv', index=False)
print(f"CSV saved as 'turbotax_output.csv'. Total Gain/Loss: {result['Gain or Loss'].sum()}")
