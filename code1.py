import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("world_happiness_2024.csv")

# Show dataset info
print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())
