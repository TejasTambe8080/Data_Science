list = [10,25,33,30,40,50,61,77,80,90,100]
print(list)
## even 
for i in list:
    if i%2 ==0:
        print(i)
## odd
for i in list:
    if i%2 !=0:
        print(i)
##greater than 30
filtered_list = []
for i in list:
    if i > 30:
        filtered_list.append(i)
print(filtered_list)