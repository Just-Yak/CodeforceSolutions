t = int(input())
mid_nums = []
 
for i in range(t):
    num_chain = []
 
    num_chain.extend(map(int, input().split(" ")))
    num_chain.sort()
    mid_nums.append(num_chain[1])
    num_chain.clear
 
for i in mid_nums:   
    print(f"{i}")