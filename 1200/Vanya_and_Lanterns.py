n, l = map(int, input().split())
lanterns = list(map(int, input().split()))
lanterns.sort()

# Initialize sol to the maximum of the distances from the ends of the street
sol = max(lanterns[0], l - lanterns[-1])

for i in range(1, n):
    # Find the maximum gap between consecutive lanterns
    gap = (lanterns[i] - lanterns[i-1]) / 2
    if gap > sol:
        sol = gap

print(sol)
