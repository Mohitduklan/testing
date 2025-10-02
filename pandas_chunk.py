import pandas as pd
from collections import defaultdict
import time

# Config
FILE = "./data/large_file.csv"
CHUNKSIZE = 500_000

# Accumulators
category_sums = defaultdict(float)
category_counts = defaultdict(int)

start = time.time()

# Process in chunks
for chunk in pd.read_csv(FILE, chunksize=CHUNKSIZE):
    grouped = chunk.groupby("category")["value"].agg(["sum", "count"])
    for category, row in grouped.iterrows():
        category_sums[category] += row["sum"]
        category_counts[category] += row["count"]

# Final result
category_means = {
    category: category_sums[category] / category_counts[category]
    for category in category_sums
}

end = time.time()

# Display
print("Chunked pandas result:")
for k, v in sorted(category_means.items()):
    print(f"{k}: {v:.6f}")
print(f"Chunked pandas time: {end - start:.2f} seconds")
