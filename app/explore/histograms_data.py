import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_expedia = pd.read_csv("../../../data/train_etienne.csv")


for i in range(len(data_expedia.columns)):
	if data_expedia.dtypes[i] != 'object' :
		print(i)
		try:
			plt.figure()
			sns.distplot(data_expedia[data_expedia.columns[i]], kde=False)
			plt.title("Histogramme de "+data_expedia.columns[i])
			plt.savefig("hist_"+data_expedia.columns[i]+".pdf")
		except ValueError:
			print("Line "+str(i)+" skipped")
			pass
