import pandas as pd 
db = pd.read_csv('sales_data.csv')   
print(db) 
TotalRevenue = db.groupby('Product')['Price'].sum() 
print(TotalRevenue)