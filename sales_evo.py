# coding: utf-8
get_ipython().run_line_magic('save', 'script.py 1-50')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('run', 'script.py')
## EVOLUTIONS DES VENTES DANS LE TEMPS ##
### LIBRARIES 
import seaborn as sns
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
### IMPORT DES FICHIERS 
orders = pd.read_csv('/Users/maximebarbier/blinkit-sales-analysis/data/blinkit_orders.csv')
order_items = pd.read_csv("/Users/maximebarbier/blinkit-sales-analysis/data/blinkit_order_items.csv")
products = pd.read_csv("/Users/maximebarbier/blinkit-sales-analysis/data/blinkit_products.csv")
### EXPLORATION DES DONNEES 
orders.shape
order_items.shape
##### TEST
orders_bis = orders
orders_bis
orders_bis['nb_orders_by_customer'] = orders_bis.groupby('customer_id')['order_date'].rank(method='min')
orders_bis.heand()
orders_bis.head()
orders_bis[orders_bis[['customer_id'] == "45477575"]]
orders_bis[orders_bis['customer_id'] == "45477575"]
orders_bis[orders_bis['customer_id'] == 45477575]
orders_join = pd.read_csv('/Users/maximebarbier/blinkit-sales-analysis/data/blinkit_orders_join.csv')
orders_join.head()
orders['unit_price'].sum()
orders_items['unit_price'].sum()
order_items['unit_price'].sum()
orders_join['unit_price'].sum()
orders_join.shape
orders_bis.shape
orders = orders_bis
orders
def segment_lambda(row):
    if row['nb_orders_by_customer'] == 1:
        return "new"
    elif row['nb_orders_by_customer'] > 3:
        return "frequent"
    else:
        return "occasional"
       
orders[segment] = segment_lambda(orders)
orders['segment'] = orders['nb_orders_by_customer'].apply(lambda x: "new" if x == 1 else "frequent" if x > 3 else "occasional")
orders
pd.set_option("display.max_columns", None)
orders.head()
orders_join = orders.merge(order_items,on='order_id',how='inner')
orders_items['unit_price'].sum()
order_items['unit_price'].sum()
orders_join['unit_price'].sum()
orders_join['revenue'] = orders_join.unit_price * orders_join.quantity
orders_join.head()
orders_pivot = orders_join.pivot_table(values='revenue',index='order_date',columns='segment',aggfunc='sum')
orders_pivot
orders_pivot_daily = orders_pivot.resample("DE")['revenue'].sum()
orders_pivot_daily = orders_pivot.resample("D")['revenue'].sum()
orders_pivot_daily = orders_pivot.resample("day")['revenue'].sum()
orders_pivot_daily = orders_pivot.resample("D")['revenue'].sum()
orders_pivot.set_index('order_date',drop=True)
orders_pivot.set_index(orders_pivot['order_date'],drop=True)
orders_pivot.set_index(orders_pivot['orders_date'],drop=True)
orders_pivot.set_index('order_date',drop=True)
orders_pivot
orders_pivot.set_index(('segment','order_date'),drop=True)
orders_pivot_daily = orders_pivot.resample("D").sum()
orders_pivot.index = pd.to_datetime(orders_pivot.index)
orders_pivot_daily = orders_pivot.resample("D").sum()
orders_pivot_daily
orders_pivot_daily.plot(figsize=(12, 5))
plt.title("Revenus journaliers par segment")
plt.ylabel("Revenue (€)")
plt.xlabel("Date")
plt.grid(True)
plt.show()
### REVENUE MENSUEL PAR SEGMENT
orders_pivot_monthly = orders_pivot.resample("ME").sum()
orders_pivot_monthly.plot(figsize=(12,5))
plt.title("Revenus mensuels par segment")
plt.xlabel("Date")
plt.ylabel("Revenue (€)")
plt.show()
orders_pivot_daily.plot(figsize=(12, 5), marker='o')
plt.title("Revenus journaliers par segment")
plt.ylabel("Revenue (€)")
plt.xlabel("Date")
plt.grid(True)
plt.show()
orders_pivot_monthly.plot(figsize=(12, 5), marker='o')
plt.title("Revenus mensuels par segment")
plt.ylabel("Revenue (€)")
plt.xlabel("Date")
plt.grid(True)
plt.show()
orders_pivot_monthly.plot(figsize=(12, 5), marker='o')
plt.title("Revenus mensuels par segment")
plt.ylabel("Revenue (€)")
plt.xlabel("Date")
plt.grid(True)
plt.show()
