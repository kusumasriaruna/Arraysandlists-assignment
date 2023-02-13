frequency = list(map(int,input().split()))
k = 0
number = frequency
for i in frequency:
    value = frequency.count(i)
    if(value> k):
        k = value
        number = i
 
print(number)
 

# def most_frequent(List):
#     return max(set(List), key = List.count)
 
# List = [2, 1, 2, 2, 1, 3,1,2,1,1] 
# print(most_frequent(List))