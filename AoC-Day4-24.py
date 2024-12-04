with open('inputs/input04.txt') as i: input = i.read().splitlines()
word_search = [list(line) for line in input]




def find_xmas(row,line):
    count = 0
    north_bound = row >= 3
    south_bound = row <= len(word_search)-4
    for i,c in enumerate(line):
        if c != "X" : continue
        west_bound = i >= 3
        east_bound = i <= len(line)-4    
        if east_bound: 
            if line[i+1] == "M" and line[i+2] == "A" and line[i+3] == "S": count += 1 # east
            if south_bound:
                if word_search[row+1][i+1] == "M" and word_search[row+2][i+2] == "A" and word_search[row+3][i+3] == "S": count += 1 # southeast
            if north_bound:
                if word_search[row-1][i+1] == "M" and word_search[row-2][i+2] == "A" and word_search[row-3][i+3] == "S": count += 1 # northeast
        if west_bound:
            if line[i-1] == "M" and line[i-2] == "A" and line[i-3] == "S": count += 1 # west
            if south_bound:
                if word_search[row+1][i-1] == "M" and word_search[row+2][i-2] == "A" and word_search[row+3][i-3] == "S": count += 1 # southwest
            if north_bound:
                if word_search[row-1][i-1] == "M" and word_search[row-2][i-2] == "A" and word_search[row-3][i-3] == "S": count += 1 # northwest
        if south_bound:
            if word_search[row+1][i] == "M" and word_search[row+2][i] == "A" and word_search[row+3][i] == "S": count += 1 # south
        if north_bound:
            if word_search[row-1][i] == "M" and word_search[row-2][i] == "A" and word_search[row-3][i] == "S": count += 1 # north
    return count

def find_mas(row,line):
    count = 0
    for i,c in enumerate(line):
        if c != "A" or row == 0 or row == len(word_search)-1 or i == 0 or i == len(line)-1: continue
        diag1 = (word_search[row+1][i+1] == "M" and word_search[row-1][i-1] == "S") or (word_search[row+1][i+1] == "S" and word_search[row-1][i-1] == "M") # /
        diag2 = (word_search[row+1][i-1] == "M" and word_search[row-1][i+1] == "S") or (word_search[row+1][i-1] == "S" and word_search[row-1][i+1] == "M") # \
        if diag1 and diag2: count += 1
    return count
def main():
    print("A: ", sum(find_xmas(row,line) for row,line in enumerate(word_search)))
    print("B: ", sum(find_mas(row,line) for row,line in enumerate(word_search)))

if __name__ == "__main__":
    main()