'''
Problem n.231A on codeforces
'''


n = int(input())
team=[]
output=0

for i in range(n):
    team.append(input())
    if sum(map(int, team[i].split())) > 1:
        output += 1
print(output)