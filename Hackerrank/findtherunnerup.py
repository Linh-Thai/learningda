n = int(input())
arr = map(int, input().split())
mlist = sorted(set(arr), reverse= True)
print(mlist[1])