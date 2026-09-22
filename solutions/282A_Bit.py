x = 0
n = int(input())
 
for i in range(n):
 
    c = str(input())
 
    if c == "++X" or c == "X++":
        x += 1
    if c == "--X" or c == "X--":
        x -= 1
 
print(x)