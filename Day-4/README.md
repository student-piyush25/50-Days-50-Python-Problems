# Day 04 - Find the Top 2 Highest Values

## Problem

Find the top 2 highest values from a dictionary and also print the names connected to those values.

Example:

```python
sales = {
    'A': 5000,
    'B': 8000,
    'C': 3000,
    'D': 7000
}
```

Expected output:

```text
B --> 8000
D --> 7000
```

## My Approach

I used two variables to keep track of the highest and second-highest values:

```python
first
second
```

I also used two more variables to remember their names:

```python
first_name
second_name
```

Then I loop through the dictionary using `.items()`.

If the current value is greater than `first`, I move the old `first` value to `second` and make the current value the new `first`.

If the value is not greater than `first`, I check whether it is greater than `second`.

## Code

```python
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
```

## How It Works

At the beginning:

```text
first = 0
second = 0
```

When `A` is checked:

```text
5000 > 0
```

So:

```text
first = 5000
first_name = A
```

Then `B` comes:

```text
8000 > 5000
```

The old first value becomes second:

```text
second = 5000
second_name = A
```

and `B` becomes first:

```text
first = 8000
first_name = B
```

When `D` comes:

```text
7000 < 8000
```

so it doesn't become first.

But:

```text
7000 > 5000
```

so it becomes second.

Final result:

```text
B --> 8000
D --> 7000
```

## What I Learned

I learned how to keep track of the highest and second-highest values while looping through a dictionary.

I also learned that when a new highest value is found, the previous highest value needs to move to the second position.

## Complexity

Time: O(n)

Space: O(1)

The dictionary is checked only once, so the solution takes one pass through the data.