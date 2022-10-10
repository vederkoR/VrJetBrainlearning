import pandas as pd

df = pd.read_csv("data/groups.tsv", delimiter='\t')
print(df.dropna()[df.features == 1].mean_mu.mean(), df.dropna()[df.features == 0].mean_mu.mean())
