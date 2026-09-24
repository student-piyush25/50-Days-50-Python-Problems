# Day 03 - Merge Two Dictionaries

## Problem

Merge two dictionaries into one.

If the same key is present in both dictionaries, add their values together.

Example:

```python
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 10, 'd': 15}
```

Expected result:

```python
{'a': 10, 'b': 25, 'c': 40, 'd': 15}
```

## My Approach

I first copy all the values from `dict1` into a new dictionary called `result`.

Then I loop through `dict2`.

For every key in `dict2`, I check if that key is already in `result`.

* If the key is already there, I add the two values.
* If the key is not there, I simply add the new key and value.

This way I can handle both common keys and new keys.

## Code

```python
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 10, 'd': 15}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    if key in result:
        result[key] = result[key] + dict2[key]
    else:
        result[key] = dict2[key]

print(result)
```

## How It Works

First, `dict1` is copied into `result`:

```python
{'a': 10, 'b': 20, 'c': 30}
```

Then we check the keys from `dict2`.

For `b`:

```text
20 + 5 = 25
```

For `c`:

```text
30 + 10 = 40
```

`d` is not already in `result`, so it is added directly:

```text
d = 15
```

Finally:

```python
{'a': 10, 'b': 25, 'c': 40, 'd': 15}
```

## What I Learned

I learned how to check whether a key already exists in a dictionary using `in`.

I also understood how I can use a separate dictionary to build the final result while comparing values from two dictionaries.

## Complexity

Time: O(n + m)

Space: O(n + m)

Here, `n` and `m` are the number of keys in the two dictionaries.
