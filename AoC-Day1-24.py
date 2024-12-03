leftList = []
rightList = []
sumA = 0
sumB = 0
with open('inputs/input01.txt') as i:
    read_list = i.read().splitlines()
for l in read_list:
    s = l.split()
    leftList.append(int(s[0]))
    rightList.append(int(s[1]))
    
leftList.sort()
rightList.sort()

for i in range(len(leftList)):
    sumA += abs(leftList[i] - rightList[i])
for i in range(len(leftList)):
    sumB += leftList[i] * rightList.count(leftList[i])

print("A: ", sumA)
print("B: ", sumB)