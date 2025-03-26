def calculate_total_distance(left, right):
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    return sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))

# Example input
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

# Output
print("Total Distance:", calculate_total_distance(left_list, right_list))
