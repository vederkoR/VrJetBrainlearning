import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from astropy.cosmology import FlatLambdaCDM
from astropy import units as u
from astropy.coordinates import SkyCoord
import itertools

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

# isolated_gals = pd.read_csv("data/isolated_galaxies.tsv", delimiter='\t')
# gal_morph = pd.read_csv("data/galaxies_morphology.tsv", delimiter='\t')

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

# frac_1 = len(gal_morph[gal_morph.n > 2].n) / len(gal_morph.n)
# frac_2 = len(isolated_gals[isolated_gals.n > 2].n) / len(isolated_gals.n)
# p = stats.ks_2samp(isolated_gals.n, gal_morph.n).pvalue
# print(frac_1, frac_2, p)
# gal_wo_name = gal_morph.drop(columns=['Name']).set_index("Group")
# df.set_index("Group", inplace=True)
# groups = gal_wo_name.groupby("Group").agg({"n": "mean", "T": "mean"}).rename(
#     columns={"n": "mean_n", "T": "mean_T"})
# merged_groups = pd.concat([df, groups], axis=1).dropna()
# print(gal_wo_name.head())
# print(df.head())
# print(merged_groups.head())
# fig, axes = plt.subplots(1, 2, figsize=(16, 8))
#
# axes[0].scatter(x=merged_groups.mean_n, y=merged_groups.mean_mu, c='red')
# axes[1].scatter(x=merged_groups.mean_T, y=merged_groups.mean_mu, c='red')
# axes[0].set_xlabel('n', fontsize=22)
# axes[0].set_ylabel('mu', fontsize=22)
# axes[1].set_xlabel('T', fontsize=22)
# axes[1].set_ylabel('mu', fontsize=22)
# plt.show()
# p1 = stats.shapiro(merged_groups.mean_mu).pvalue
# p2 = stats.shapiro(merged_groups.mean_n).pvalue
# p3 = stats.shapiro(merged_groups.mean_T).pvalue
# p4 = stats.pearsonr(merged_groups.mean_mu, merged_groups.mean_n).pvalue
# p5 = stats.pearsonr(merged_groups.mean_mu, merged_groups.mean_T).pvalue
# print(p1, p2, p3, p4, p5)


# my_cosmo = FlatLambdaCDM(H0=67.74, Om0=0.3089)
# z = 0.06
# angular_diameter_distance = my_cosmo.angular_diameter_distance(z).to(u.kpc)
# print(angular_diameter_distance)
#
# p1 = SkyCoord(ra=6.52971 * u.degree, dec=25.72519 * u.degree, frame="fk5")
# p2 = SkyCoord(ra=6.52479 * u.degree, dec=25.71933 * u.degree, frame="fk5")
# print(p1.separation(p2))

df_1 = pd.read_csv('data/galaxies_coordinates.tsv', sep="\t")
df_2 = pd.read_csv("data/groups.tsv", delimiter='\t')
my_cosmo = FlatLambdaCDM(H0=67.74, Om0=0.3089)
diam_array = my_cosmo.angular_diameter_distance(np.array(df_2.z)).to(u.kpc)
df_2['diams'] = diam_array.value
# print(df_2.head(10))
# print('______')
# print(int(df_2[df_2.Group == 'HCG 8'].diams))
df_2['r_norm'] = [-1] * len(df_2)
df_2['r'] = [-1] * len(df_2)
for group in list(df_2.Group):
    if group in list(df_1.Group):
        list_ = df_1[df_1.Group == group]
        r_list = []
        r_norm_list = []
        for inx1, inx2 in itertools.combinations(range(len(list_)), 2):
            p1 = SkyCoord(ra=list_.iloc[inx1].RA * u.degree, dec=list_.iloc[inx1].DEC * u.degree, frame="fk5")
            p2 = SkyCoord(ra=list_.iloc[inx2].RA * u.degree, dec=list_.iloc[inx2].DEC * u.degree, frame="fk5")
            r_list.append(p1.separation(p2).to(u.rad).value)
            r_norm_list.append(p1.separation(p2).value)
        df_2.loc[df_2.Group == group, 'r'] = np.median(np.array(r_list))
        df_2.loc[df_2.Group == group, 'r_norm'] = np.median(np.array(r_norm_list))

df_2['real_r'] = df_2.r * df_2.diams
val1 = float(df_2[df_2.Group == 'HCG 2'].real_r)
p_val2 = stats.shapiro(df_2.dropna().real_r).pvalue
p_val3 = stats.shapiro(df_2.dropna().mean_mu).pvalue
p_val4 = stats.pearsonr(df_2.dropna().real_r, df_2.dropna().mean_mu).pvalue
print(f"{val1:.4f}", f"{p_val2:.4e}", f"{p_val3:.4f}", f"{p_val4:.4f}")

# print(df_2)