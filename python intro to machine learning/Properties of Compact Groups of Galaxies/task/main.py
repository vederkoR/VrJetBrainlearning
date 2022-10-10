import pandas as pd
from scipy import stats

df = pd.read_csv("data/groups.tsv", delimiter='\t')
# print(df.dropna()[df.features == 1].mean_mu.mean(), df.dropna()[df.features == 0].mean_mu.mean())
sample_1 = df.dropna()[df.features == 1].mean_mu
sample_2 = df.dropna()[df.features == 0].mean_mu

p1 = stats.shapiro(sample_1).pvalue
p2 = stats.shapiro(sample_2).pvalue
stat, p = stats.fligner(sample_1, sample_2)
anova_p = stats.f_oneway(sample_1, sample_2).pvalue
print(p1, p2, p, anova_p)
