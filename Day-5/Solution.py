# Convert a list of tuples into a dictionary using loop, not dict(data).

data = [
    ("A", 100),
    ("B", 200),
    ("C", 300)
]

result = {}

for key, value in data:
    result[key] = value

print(result)
# print(type(result))