# Day 6: Group Words by Their First Letter

## Problem
Write a Python program to group words based on their first letter using a dictionary.

## My Approach
I used a `for` loop to go through each word in the list. For every word, I extracted its first letter using `word[0]`.

I checked whether that letter was already present in the dictionary. If it wasn't, I created a new empty list for that letter. Then I used `append()` to add the word to the corresponding list.

This way, words starting with the same letter are stored together.

## Code
```python
words = ['apple', 'ant', 'ball', 'cat', 'car']

result = {}

for word in words:
    first_letter = word[0]

    if first_letter not in result:
        result[first_letter] = []

    result[first_letter].append(word)

print(result)
```

## Output
```python
{
    'a': ['apple', 'ant'],
    'b': ['ball'],
    'c': ['cat', 'car']
}
```

## How It Works
1. First, I created a list containing the words and an empty dictionary to store the result.
2. The `for` loop takes one word at a time from the list.
3. Using `word[0]`, I get the first letter of the current word.
4. The `if` condition checks whether that letter already exists in the dictionary.
5. If the letter is new, I create an empty list for it.
6. Finally, `append()` adds the current word to the list associated with its first letter.

## Concepts Used
- For loops
- Dictionaries
- Lists
- String indexing
- Conditional statements
- `append()` method

## Time and Space Complexity
- **Time Complexity:** O(n) on average, assuming dictionary operations take constant time and words have bounded length.
- **Space Complexity:** O(n) for storing the grouped words and dictionary entries.

Here, `n` is the total number of words.

## What I Learned
I learned how to group related items using a dictionary and lists. I also got more practice with string indexing, checking dictionary keys, and adding elements to lists inside a loop.