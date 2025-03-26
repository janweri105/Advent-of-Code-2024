# 🎄 Advent of Code 2024 - Day 1: Historian Hysteria

> Solving the mystery of the missing Chief Historian — one distance at a time!

## 📜 Problem Description

The Chief Historian is missing just before the big Christmas sleigh launch! As the Elvish Senior Historians search his office, they uncover two mismatched lists of **location IDs**, one per team. Your job is to help reconcile them by calculating the **total distance** between paired entries.

### Example Input
Left List Right List 3 4 4 3 2 5 1 3 3 9 3 3


### Pairing Strategy

Sort both lists and pair the smallest with the smallest, second smallest with second smallest, and so on. The **distance** is the absolute difference between paired values.

### Sample Calculation

Sorted Left List: `1, 2, 3, 3, 3, 4`  
Sorted Right List: `3, 3, 3, 4, 5, 9`

Paired Differences:

- |1 - 3| = 2  
- |2 - 3| = 1  
- |3 - 3| = 0  
- |3 - 4| = 1  
- |3 - 5| = 2  
- |4 - 9| = 5  

**Total Distance: `2 + 1 + 0 + 1 + 2 + 5 = 11`**

---

## 🧠 Solution Approach

1. Parse input into two separate lists.
2. Sort both lists in ascending order.
3. Use `zip()` to pair each corresponding element.
4. Calculate the absolute difference for each pair.
5. Sum all distances.

---

## 🧪 Sample Code (Python)

```python
def calculate_total_distance(left, right):
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    return sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))

# Example input
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

# Output
print("Total Distance:", calculate_total_distance(left_list, right_list))


