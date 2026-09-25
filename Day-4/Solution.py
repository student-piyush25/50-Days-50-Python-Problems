# Find the top 2 highest values in a dictionary

sales = {
    'A': 5000,
    'B': 8000,
    'C': 3000,
    'D': 7000
}

first = 0
second = 0

first_name = ""
second_name = ""

for name, value in sales.items():
    if value > first:
        second = first
        second_name = first_name
        
        first = value
        first_name = name
        
    elif value > second:
        second = value
        second_name = name
        
print(first_name, "-->", first)
print(second_name, "-->", second)