import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_expedia = pd.read_csv("../../../data_expedia/train_etienne.csv", nrows=100000)

regions=data_expedia['user_location_region']

sns.distplot(regions)
plt.title("Histogramme des origines geographiques")
plt.savefig('plot_regions.pdf')

