"""
このファイルに解答コードを書いてください
"""
Dict = dict()
S = ""

count = 0
with open("") as f: #使用するファイルを入力
    for x in f:
        count += 1
n = count

#入力を行う

for x in range(n-1):
    i, s = input().split(':')
    i = int(i)
    Dict[i] = s

m = int(input())

List = sorted(Dict.items())

for i, s in List :
    if m % i == 0:
        S += s
    else:
        continue

if S :
    print(S)
else :
    print(m)



