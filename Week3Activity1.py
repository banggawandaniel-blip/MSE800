from ucimlrepo import fetch_ucirepo

# fetch dataset
iris = fetch_ucirepo(id=53)

# data (as pandas dataframes)
X = iris.data.features
y = iris.data.targets

# metadata
print(iris.metadata)

# variable information
print(iris.variables)

# Initial data processing
print("\nTotal number of records:", len(X))
print("Total number of different flowers:", y["class"].nunique())
print("Names of all different flowers:")
print(y["class"].unique())
