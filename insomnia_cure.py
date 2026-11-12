
data = []

for _ in range(5):
    data.append(int(input()))
k,l,m,n,d = data

counter = 0

for dragon in range(1, data[4]+1):
    if dragon%k==0 or dragon%l==0 or dragon%m==0 or dragon%n==0:
        counter += 1

print(counter)

