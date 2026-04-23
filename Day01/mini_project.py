name = "Tejas"
age = 20 
marks = [90, 98, 95,97, 99]
n = len(marks)

for i in marks:
    print(i)
total_marks = sum(marks)
print("Total Marks:", total_marks)
## AVerage 
average_marks = total_marks / len(marks)
print("Average Marks:", average_marks)
##✅ Q1: Find maximum
max_num = 0 
for i in range(1, n):
    if marks[i] > marks[i-1]:
        max_num = marks[i]
    else :
        max_num = marks[i-1]
print("Maximum Marks:", max_num)
##✅ Q2: Find minimum
min_num = marks[0]

for i in range(1, len(marks)):
    if marks[i] < min_num:
        min_num = marks[i]

print("Minimum Marks:", min_num)
## fimd even number count 
count = 0 
for i in marks:
    if i%2 ==0:
        count = count + 1
print("Even number count is:",count)


## reverse the above string 
 
p = len(name)-1
reversed_text = ""
while p >= 0:
    reversed_text = reversed_text + name[p]
    p = p - 1
print("Reversed Name:", reversed_text)