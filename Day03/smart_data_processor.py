data = ["10", "20", "abc", "40"]
# ✔ Convert to integers
# ✔ Skip invalid values
# ✔ Square numbers using map
# ✔ Filter values > 500


# Step 1: Convert to integers (skip invalid)
def to_int(x):
    try:
        return int(x)
    except ValueError:
        return None

nums = list(map(to_int, data))
print(nums)

# Step 2: Remove invalid (None values)
nums = list(filter(lambda x: x is not None, nums))
print(nums)

# Step 3: Square numbers
squares = list(map(lambda x: x*x, nums))
print(squares)

# Step 4: Filter values > 500
result = list(filter(lambda x: x > 500, squares))

print(result)
