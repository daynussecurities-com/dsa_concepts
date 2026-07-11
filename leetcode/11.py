# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""
width = r - l
container_height = min(height[l], height[r])
area = width * container_height
print(area)
"""
height = [1,8,6,2,5,4,8,3,7]

l = 0
r = len(height)-1
max_area = 0

while l < r:
    width = r - l
    container_height = min(height[l], height[r])
    area = width * container_height
    if max_area < area:
        max_area = area
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(max_area)