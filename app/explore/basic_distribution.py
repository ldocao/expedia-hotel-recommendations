import numpy as np
import pandas as pd
test_path = "../../../data/test.csv.gz"


df = pd.read_csv(test_path, compression="gzip")

