import pandas as pd
import numpy as np

# size = 24*365 # 24 hours * 365 days
size = 24*365

for i in range(10):
    np.random.seed(42*i+7)  # For reproducibility
    electricity_prices = np.random.randint(-1000, 3000, size=size)

    # Create a DataFrame with explicit column names
    df = pd.DataFrame({
        "hour": list(range(size)),
        "electricity_price": electricity_prices
    })

    # Save to CSV
    csv_filename = f"input{i}.csv"
    df.to_csv(csv_filename, index=False)
