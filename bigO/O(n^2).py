def print_items(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                print(i, j, k)

print_items(10)

# This Program
# Time Complexity O(n^2)