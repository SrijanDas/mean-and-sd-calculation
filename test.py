import pandas as pd

file = "D:\\project\\10_07_20\\dataWithMonths\\output_jenbenka_tweets.csv"

df = pd.read_csv(file)
sd = df.std(axis=0, skipna=True)
print(sd)