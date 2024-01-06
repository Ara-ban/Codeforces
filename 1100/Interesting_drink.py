import bisect
 
n = int(input())
prices = list(map(int, input().split()))
prices.sort()  # Sorting the list of prices
 
q = int(input())  # Number of days
 
for _ in range(q):
    coin = int(input())
    # Find the rightmost index where coin can be placed
    i = bisect.bisect_right(prices, coin)
    print(i)  # Print the number of affordable shops
