import pandas as pd
import numpy as np
import os

# Settings
rows_per_chunk = 500_000
total_size_gb = 12
approx_row_size_bytes = 300  # rough estimate per row size in bytes
total_rows = int((total_size_gb * 1024**3) / approx_row_size_bytes)
file_path = "./data/large_file.csv"

# Function to create and append chunks
def generate_large_csv(file_path, rows_per_chunk, total_rows):
    cols = {
        'id': np.arange(rows_per_chunk),
        'category': np.random.choice(['A', 'B', 'C', 'D'], size=rows_per_chunk),
        'value': np.random.rand(rows_per_chunk) * 1000,
        'description': np.random.choice(['foo', 'bar', 'baz', 'qux'], size=rows_per_chunk),
        'timestamp': pd.date_range("2020-01-01", periods=rows_per_chunk, freq='S')
    }

    chunks_written = 0
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode='w', newline='') as f:
        for i in range(0, total_rows, rows_per_chunk):
            chunk = pd.DataFrame(cols)
            chunk['id'] += i  # ensure unique ID
            chunk.to_csv(f, header=(i == 0), index=False)
            chunks_written += 1
            print(f"Written chunk {chunks_written}, row {i}")

    print(f"✅ Done. File saved to: {file_path}")

generate_large_csv(file_path, rows_per_chunk, total_rows)
