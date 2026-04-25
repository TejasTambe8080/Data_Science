import re 
text = " THis is the my phone Number 9006018080"
nums = re.findall(r'\d+',text)
print(nums)
text = "Contact: test@gmail.com"

emails = re.findall(r"\S+@\S+", text)
print(emails)
