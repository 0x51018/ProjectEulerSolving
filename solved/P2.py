arr = [1,2]
while(arr[-1]+arr[-2]<4000000):
    arr.append(arr[-1]+arr[-2])
print(sum(x for x in arr if x%2 == 0))