"""
4
1 2 3 4
output :- 4
"""


def maxValueFind(arr):
    mx = -1

    for i in arr:
        if i > mx:
            mx = i
       

    return mx

# input part here

n = int(input())
arr = list(map(int,input().split()))

result = maxValueFind(arr)
print(result)