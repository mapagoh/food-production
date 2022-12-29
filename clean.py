import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

pd.set_option("max_columns", None)
pd.set_option("max_rows", None)
schema_name="food_production.csv"
food_production=pd.read_csv(schema_name)
food_production.head(10)
food_production.tail(10)
#food_production.drop(["Animal Feed"], axis=1) ## Eliminar columna
#food_production.rename(columns={"Total_emissions": "Emissions"}) ## Renombrar columna
#food_production["Farm"]=pd.to_datetime(food_production["Farm"])

imputer=SimpleImputer(strategy="constant")
food_production2=pd.DataFrame(imputer.fit_transform(food_production), columns=food_production.columns)
#print(food_production2)
food_production3=food_production2.groupby(["Food product", "Farm", "Animal Feed"])[["Processing", "Total_emissions"]].sum().reset_index()
#food_production3.head(10)
products=food_production3["Food product"].unique()
#print(products)
len(products)

for idx in range(0,len(products)):
  C=food_production3[food_production3["Food product"]==products[idx]].reset_index()
  print(C)
  plt.scatter(np.arange(0, len(C)), C["Farm"], color="green", label= "Granja")
  plt.scatter(np.arange(0, len(C)), C["Animal Feed"], color="black", label="Alimentación Animal")
  plt.scatter(np.arange(0, len(C)), C["Processing"], color="blue", label="Procesado")
  plt.xlabel("valor")
  plt.ylabel("valor2")
  plt.legend()
  plt.show()
