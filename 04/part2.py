with open("./input.txt","r") as fin:
    data = fin.read()
    lines = data.strip().split("\n")
    winner_nums = []
    card_nums = []

for line in lines:
    line_winner_nums = line.strip().split(": ")[1].split("|")[0]
    line_card_nums = line.strip().split(": ")[1].split("|")[1]
    winner_nums.append(line_winner_nums)
    card_nums.append(line_card_nums)


def get_nums(scratch:list[str]) ->list[str]:
    nums = []
    num = ""
    for v in scratch:
        ns = []
        for i, val in enumerate(v):
            if val.isdigit():
                num += val
            if (not val.isdigit() or i+1 >= len(v)) and len(num)>0:
                ns.append(num)
                num = ""
        nums.append(ns)
    return nums
    
    

card_nums = get_nums(card_nums)
winner_nums = get_nums(winner_nums)
ans = 0
n = len(lines)
copies = [[] for _ in range(n)]
for i,line in enumerate(lines):
    score = 0
    for num in card_nums[i]:
        if num in winner_nums[i]:
            score += 1
    for j in range(i+1,i+score+1):
        copies[i].append(j)

score = [1 for _ in range(n)]

for i in range(n-1,-1,-1):
    for j in copies[i]:
        score[i] += score[j]
ans = sum(score)    

print(ans)