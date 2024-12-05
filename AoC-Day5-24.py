with open('inputs/input05.txt') as i: input = i.read().splitlines()
split = input.index('')
#ordering_rules = [r.split("|") for r in input[:split]]
page_updates = [u.split(",") for u in input[split+1:]]
ordering_rules_dict = {}
for r in input[:split]:
    x,y = r.split("|")
    ordering_rules_dict.setdefault(x, []).append(y)

def is_update_valid(update):
    for i,v in enumerate(update):
        if not bool(ordering_rules_dict.get(v)) and not i == len(update)-1: return False
        if not all(page in ordering_rules_dict.get(v) for page in update[i+1:]): return False
    return True

def calculate_middle(update):
    sum = 0
    for u in update:
        middle_index = len(u) // 2
        sum += int(u[middle_index])
    return sum

def fix_update(update): 
    fixed = False
    i = 0
    while not fixed:
        if i == len(update)-1: fixed = True #end
        if not bool(ordering_rules_dict.get(update[i])) or not all(page in ordering_rules_dict.get(update[i]) for page in update[i+1:]): 
            update.append(update.pop(i)) #if not in dict or not correct move to end
        else: 
            i+=1 #next value
    return update

def main():
    valid_page_updates_A = []
    valid_page_updates_B = []
    for u in page_updates:
        if is_update_valid(u):
            valid_page_updates_A.append(u)
        else:
            valid_page_updates_B.append(fix_update(u))
    
    partA = calculate_middle(valid_page_updates_A)
    partB = calculate_middle(valid_page_updates_B)
    print("A: ", partA)
    print("B: ", partB)

if __name__ == "__main__":
    main()