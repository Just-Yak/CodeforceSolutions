n = int(input())
answ = []
 
for i in range(n):
    w = str(input())
    if len(w) > 10:
        text = f"{w[0]}{len(w)-2}{w[len(w)-1]}"
        answ.append(text)
    else:
        text = f"{w}"
        answ.append(text)
 
for x in answ:
    print(f"{x}")