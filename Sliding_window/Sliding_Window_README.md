# Sliding Window Template 🪟

This repository provides a **universal template** for solving a wide range of **Sliding Window problems** in Python. It's ideal for interview preparation and competitive programming.

## 🔍 Problem Type

Sliding window problems involve processing elements in a **contiguous window (subarray)** of size `k`, where the window slides one element at a time across the array.

## ✅ Template Code

```python
def func(arr, n, k):
    i, j = 0, 0
    while j < n:
        doCalculations()  # Perform current calculations to update intermediate result

        if j - i + 1 < k:
            j += 1  # Expand the window

        elif j - i + 1 == k:
            deriveRes()     # Use current window data to derive the answer
            slideWindow()   # Remove elements that are sliding out of the window
            i += 1
            j += 1

    return # final result
```

## 🛠️ Function Explanation

- `doCalculations()`: Update intermediate data (e.g., sum, frequency map) based on current `j`.
- `deriveRes()`: Save or update your final result when the window size hits `k`.
- `slideWindow()`: Clean up or update the state before sliding the window (e.g., remove the effect of `arr[i]`).

## 🔁 Use Cases

- Maximum/minimum in a sliding window
- Count of distinct elements in every window of size `k`
- Longest subarray with at most `k` distinct elements
- Average/subarray sum problems

## 📌 Tips

- Always initialize `i` and `j` to `0`.
- Make sure to handle the **condition when `j - i + 1 == k`** carefully.
- You can modify this template for **variable-sized** windows too.

## ✨ Example Problems to Practice

- LeetCode 239: Sliding Window Maximum
- LeetCode 1004: Max Consecutive Ones III
- GeeksForGeeks: First negative integer in every window of size k

---

Happy Coding! 💻🔥