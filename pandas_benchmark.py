import pandas as pd
import time

start = time.time()

df = pd.read_csv("./data/large_file.csv")
result = df.groupby("category")["value"].mean()

end = time.time()
print("pandas result:\n", result)
print(f"pandas time: {end - start:.2f} seconds")
