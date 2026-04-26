import numpy as np 

sales = [100, 200, 300, 400]
sales_array = np.array(sales)

print(sales_array * 1.10)

np_avg = np.mean(sales_array)
print(np_avg)
np_max = np.max(sales_array)
print(np_max)
np_min = np.min(sales_array)
print(np_min)