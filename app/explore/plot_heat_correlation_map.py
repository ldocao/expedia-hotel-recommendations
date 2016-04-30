import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Database
df=pd.read_csv("../../../train_etienne.csv")

column_names = df.columns.values
df_categorical_values_subset = df[column_names[[6, 13, 14, 15, 19]]]

corrmat = df_categorical_values_subset.corr()

plt.figure()
sns.heatmap(corrmat, vmax=.8, square=True)
plt.title("Correlation heat map")
plt.xticks(rotation=90)

plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("heat_map_correlation.pdf")
