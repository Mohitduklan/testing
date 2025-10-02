
import dask.dataframe as dd
import time
df = dd.read_csv("./data/large_file.csv")
print(df.head())
print(df.columns)


# Compute to do eval
print(df.shape[0].compute())


# # Filtering
filtered_df = df[df["value"] > 600]
print(filtered_df.head())


# Value Count
t = time.time()
val_count = df["category"].value_counts().compute()
print(time.time() - t)
print(val_count)

t = time.time()
val_count = df["category"].value_counts(split_every=4).compute()
print(time.time() - t)
print(val_count)



# Time stamps
t = time.time()
print(df["timestamp"].dtype) # It is string
print(time.time() - t)
df["timestamp"] = dd.to_datetime(df["timestamp"])
print(time.time() - t)
df = df.set_index(df["timestamp"])
print(time.time() - t)
mean = df["value"]
print(mean.head(10))




# Time stamps
print(df["timestamp"].dtype) # It is string
df["timestamp"] = dd.to_datetime(df["timestamp"])
df = df.set_index(df["timestamp"])
df = df["value"].resample("1H").mean()
print(df.head(10))



# Transform
print(df.groupby("category")["value"].agg(lambda x: x - x.mean()))
print(df.groupby("category")["value"].transform(lambda x: x - x.mean()))
