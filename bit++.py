
X=0
N = int(input())

for _ in range(N):
    operation = input()
    if operation=='X++' or operation=='++X':
        X+=1
    elif operation=='X--' or operation=='--X':
        X-=1
print(X)

