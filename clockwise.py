def rotateArray(a,d):
    n=len(a)
    a[:]=a[d:n]+a[0:d]
    return a

arr = list(map(int,input().split()))
m=int(input())

print("Rotated list is")
print(rotateArray(arr,m)) 