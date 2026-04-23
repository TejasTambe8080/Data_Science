#  Student Data Cleaner + Analyzer
data = {
     "names": [" Tejas ", "RAHUL", "anita  "],
     "marks": [80, 40, 90]
 }
# You must:

# ✔ Clean names
# ✔ Create dictionary {name: marks}
# ✔ Find topper
# ✔ Count pass/fail
clean_names = [name.strip().lower() for name in data["names"]]
print
student_dict = dict(zip(clean_names, data["marks"]))
print(student_dict)
topper = max(student_dict, key=student_dict.get)
print("Topper:", topper)
pass_count = sum(1 for marks in student_dict.values() if marks >= 50)
print
fail_count = len(student_dict) - pass_count
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)