import yfinance as yf

# Specify the stock ticker and time range
ticker = "COALINDIA.NS"  # Example: Replace with your desired stock ticker
data = yf.download(ticker, start="2019-12-10", end="2024-12-10")

# Save data to a CSV file
data.to_csv(f"{ticker}_5_years_data.csv")
print(f"Data saved to {ticker}_5_years_data.csv")

# Display the first few rows
print(data.head())
