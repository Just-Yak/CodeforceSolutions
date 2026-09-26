t = int(input())
answ = []
 
for x in range(t):
 
    n = int(input())
 
    num_list = []
    num_list.extend(map(int, input().split(" ")))
 
    min_num_count = num_list.count(min(num_list))
    max_num_count = num_list.count(max(num_list))
 
    if min_num_count > max_num_count:
        answ.append(num_list.index(max(num_list))+1)
    else:
        answ.append(num_list.index(min(num_list))+1)
 
    num_list.clear()
 
 
for i in answ:
    print(f"{i}")