reports = []
with open('inputs/input02.txt') as i:
    read_list = i.read().splitlines()
for l in read_list:
    level = [int(item) for item in l.split()]
    reports.append(level)
def isSafe(level):
    deltas = [level[i]-level[i-1] for i in range(1,len(level))]
    direction = deltas[0] > 0 #increasing (True) or decreasing (False)
    return all(1 <= abs(d) <= 3 for d in deltas) and all((d > 0) == direction for d in deltas[1:])

def isSafeRemove(level):
    return isSafe(level) or any(isSafe(level[:i] + level[i+1:]) for i in range(len(level)))

print("A: ", sum(isSafe(r) for r in reports))
print("B: ", sum(isSafeRemove(r) for r in reports))