from math import  *
def quicksort(a):
    if len(a) <= 1:
        return a
    left = []
    right = []
    i = int(len(a) / 2)
    for n in range(0,i):
        if a[n] < a[i]:
            left.append(a[n])
        elif a[n] >= a[i]: 
            right.append(a[n])
    for n in range(i+1, len(a)):
        if a[n] < a[i]:
            left.append(a[n])
        else: right.append(a[n])
    return quicksort(left) + [a[i]] + quicksort(right)
n = 1000
array = [sqrt(log(n,4)) , log(log(n,2),2) , log(n,3) , sqrt(n), pow(log(n,2),2) , n/log(n,5)]
print(array)    