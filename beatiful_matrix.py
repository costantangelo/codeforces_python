
M = []
for i in range(5):
    M.append(list(map(int, input().split())))

x,y=0,0
found = False

for i in range(5):
    if found:
        break
    for j in range(5):
        if M[i][j] == 1:
            x,y=i,j
            found = True
            break

print(abs(x-2) + abs(y-2)) # This is called the taxi cab distance between two discrete points
# -2 since a mathematical matrix has indexes from 1 to n per row/col, but in Python we go from 0 to n-1

