import dask.dataframe as dd
import time

start = time.time()

df = dd.read_csv("./data/large_file.csv")
result = df.groupby("category")["value"].mean().compute()

end = time.time()
print("dask result:\n", result)
print(f"dask time: {end - start:.2f} seconds")
