N = int(input())
answers=[]

for i in range(N):
    answers.append(input())
    L = len(answers[i])
    if L>10:
        answers[i]=f'{answers[i][0]}{L-2}{answers[i][L-1]}'

print('\n'.join(answers))

