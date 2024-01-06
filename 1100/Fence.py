
n, k = map(int, input().split())
heights = list(map(int, input().split()))
 
# Initialize the sum of the first k planks
current_sum = sum(heights[:k])
min_sum = current_sum
solution_index = 0
 
# Iterate over the array, updating the sum and checking for minimum
for i in range(1, n - k + 1):
    current_sum = current_sum - heights[i - 1] + heights[i + k - 1]
    if current_sum < min_sum:
        min_sum = current_sum
        solution_index = i
 
print(solution_index+1)
