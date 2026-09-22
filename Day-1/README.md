# Day 01 — Rotate a List to the Right

## 📌 Problem
Rotate a list to the right by k positions.

Example:
[1,2,3,4,5], k=2 → [4,5,1,2,3]

## 🧠 Approach

Use list slicing.

1. Use `k % len(nums)` to handle large k.
2. Get the last k elements using `nums[-k:]`.
3. Get the remaining elements using `nums[:-k]`.
4. Join both parts using `+`.

## 💻 Solution

[code]

## 🔍 How It Works

For `k = 2`:

`nums[-2:]` → `[4,5]`

`nums[:-2]` → `[1,2,3]`

Then:

`[4,5] + [1,2,3]`

→ `[4,5,1,2,3]`

### Important Concept

Negative indexing means counting from the end.
It does NOT mean reversing.

`nums[-2:]` → `[4,5]`

`nums[::-1]` → reverses the list.

## 🧪 Example

Input:
[1,2,3,4,5], k=2

Output:
[4,5,1,2,3]

## ⏱️ Complexity

Time: O(n)
Space: O(n)

## 💡 What I Learned

I learned how list slicing, negative indexing, and modulo can be combined to rotate a list.