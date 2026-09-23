# Day 02 — Remove Duplicate Characters

## 📌 Problem

Remove duplicate characters from a string while keeping the **original order** of the characters.

### Example

```text
Input:  "programming"
Output: "progamin"
```

The first occurrence of each character should be kept, and repeated occurrences should be removed.

---

## 🧠 Approach

I create an empty string called `result`.

Then I go through the input string one character at a time.

For every character:

1. Check whether the character is already present in `result`.
2. If it is not present, add it to `result`.
3. If it is already present, skip it.

This keeps only the first occurrence of each character while maintaining the original order.

---

## 💻 Solution

```python
text = "programming"

def remove_duplicates(text):
    result = ""

    for char in text:
        if char not in result:
            result = result + char

    return result

print(remove_duplicates(text))
```

### Output

```text
progamin
```

---

## 🔍 How It Works

For `"programming"`:

```text
Character     Result

p             "p"
r             "pr"
o             "pro"
g             "prog"
r             "prog"       ← r already exists
a             "proga"
m             "progam"
m             "progam"     ← m already exists
i             "progami"
n             "progamin"
g             "progamin"   ← g already exists
```

The important part is:

```python
if char not in result:
```

It asks:

> "Does this character already exist in my result?"

If the answer is **no**, we add it.

If the answer is **yes**, we skip it.

---

## 🐍 Python Concepts Used

* Strings
* `for` loop
* `if` condition
* `not in` membership operator
* String concatenation
* Functions
* `return`

### Important Concept: `not in`

```python
char not in result
```

checks whether `char` does **not** exist inside `result`.

For example:

```python
result = "prog"
char = "r"
```

Then:

```python
char not in result
```

is:

```text
False
```

because `"r"` is already present.

---

## ⏱️ Time Complexity

The solution takes **O(n²)** time in the general case.

Why?

* The `for` loop processes `n` characters.
* `char not in result` may scan the result string.
* String concatenation can also require creating a new string.

So the overall complexity can be quadratic.

---

## 💾 Space Complexity

The `result` string can contain up to `n` characters.

Therefore, the additional space used is:

```text
O(n)
```

---

## ⚠️ Common Mistake

A common mistake is using a `set` without thinking about order.

A set is useful for checking whether something exists, but the main requirement here is:

> Remove duplicates **while maintaining original order**.

Our solution directly preserves that order because characters are processed from left to right.

---

## 💡 What I Learned

I learned how to iterate through a string character by character and use the `not in` operator to check whether a character has already been added.

I also learned how this simple approach can remove duplicates while preserving the original order of the characters.
