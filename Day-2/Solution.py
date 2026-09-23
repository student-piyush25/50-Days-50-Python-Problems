# Remove duplicate characters from a string while maintaining their original order.
# Example: "programming" --> "progamin"

text = "programming"

def remove_duplicates(text):
    result = ""
    
    for char in text:
        if char not in result:
            result = result + char
    
    return result

print(remove_duplicates(text))