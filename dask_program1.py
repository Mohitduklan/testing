import dask.dataframe as dd
import time
data = dd.read_csv("./data/large_file.csv")
print(data.head())
print(data.columns)

# Compute to do eval
# print(data.shape[0].compute()) 

# # Filtering
# filtered_data = data[data["value"]>600]
# print(filtered_data.head())

# # Value Count
# t = time.time()
# val_count = data["category"].value_counts().compute()
# print(time.time() - t)
# print(val_count)

# t = time.time()
# val_count = data["category"].value_counts(split_every=4).compute()
# print(time.time() - t)
# print(val_count)


# # Time stamps
# t = time.time()
# print(data["timestamp"].dtype) # It is string
# print(time.time()-t)
# data["timestamp"] = dd.to_datetime(data["timestamp"])
# print(time.time()-t)
# data = data.set_index(data["timestamp"])
# print(time.time()-t)
# mean = data["value"]
# print(mean.head(10))



# # Time stamps
# print(data["timestamp"].dtype) # It is string
# data["timestamp"] = dd.to_datetime(data["timestamp"])
# data = data.set_index(data["timestamp"])
# data = data["value"].resample("1H").mean()
# print(data.head(10))


# Transform
print(data.groupby(by=["category"])["value"].agg(lambda x: x - x.mean()))