def to_timestamp_csv(df, path):
    df_copy = df.copy()

    df_copy = df_copy.reset_index()
    df_copy["Timestamp"] = df_copy["Timestamp"].astype("int64") // 10**9
    df_copy.set_index("Timestamp", inplace=True)

    df_copy.to_csv(path)
