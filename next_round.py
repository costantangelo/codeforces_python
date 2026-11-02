
n,k = map(int, input().split())

s = list(map(int, input().split()))

treshold = s[k-1]
winners = [x for x in s if x>0 and x>=treshold]

print(len(winners))


