import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Database
df=pd.read_csv("../../../train_etienne.csv",nrows=10000)

plt.figure()

sns.distplot(df["posa_continent"],kde=False)
plt.yscale("log")
plt.ylabel("Counts")
plt.title("Distribution of posa_continent")
plt.savefig("posa_continent_hist.pdf")
