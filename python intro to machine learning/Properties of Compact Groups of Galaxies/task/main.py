import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# df = pd.read_csv("data/groups.tsv", delimiter='\t')
# # print(df.dropna()[df.features == 1].mean_mu.mean(), df.dropna()[df.features == 0].mean_mu.mean())
# sample_1 = df.dropna()[df.features == 1].mean_mu
# sample_2 = df.dropna()[df.features == 0].mean_mu
#
# p1 = stats.shapiro(sample_1).pvalue
# p2 = stats.shapiro(sample_2).pvalue
# stat, p = stats.fligner(sample_1, sample_2)
# anova_p = stats.f_oneway(sample_1, sample_2).pvalue
# print(p1, p2, p, anova_p)

isolated_gals = pd.read_csv("data/isolated_galaxies.tsv", delimiter='\t')
gal_morph = pd.read_csv("data/galaxies_morphology.tsv", delimiter='\t')

# print(isolated_gals.head(5))
# print(gal_morph.head(5))
# plt.hist([isolated_gals.n, gal_morph.n],
#          stacked=True,
#          label=["isolated galaxies", "groups galaxies"],
#          color=['red', '#00958B'],  # data color
#          edgecolor="black",  # edge color
#          lw=0.5,  # width of edge color
#          rwidth=0.8,  # set bar width (with bargaps),
#          alpha=0.7  # set transparent color
#          )
#
#
# plt.ylabel("Count")
# plt.xlabel("n")
# plt.legend()
# plt.show()

frac_1 = len(gal_morph[gal_morph.n > 2].n) / len(gal_morph.n)
frac_2 = len(isolated_gals[isolated_gals.n > 2].n) / len(isolated_gals.n)
p = stats.ks_2samp(isolated_gals.n, gal_morph.n).pvalue
print(frac_1, frac_2, p)
