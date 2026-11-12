
t = int(input())

answers = []

for _ in range(t):
    n = int(input())

    if n==0 or n==1:
        answers.append(0)
    elif n%2==0:
        answers.append((n//2)-1)
    else:
        answers.append(n//2)

for a in answers:
    print(a)

