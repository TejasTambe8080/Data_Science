from datetime import datetime
now = datetime.now()    
print(now)

# 🔹 Convert String → Date

date = datetime.strptime("2024-06-01", "%Y-%m-%d")
print(date)

print(date.year)
print(date.month)       
print(date.day)