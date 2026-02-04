"""
Input: 
First line: n (size of array)
Second line: n space-separated integers

Output: Array in reverse order

Example:
Input:
5
1 2 3 4 5
Output:
5 4 3 2 1

Input:
3
10 20 30
Output:
30 20 10
"""

# def reverse(arr):
#     i = 0;
#     j = len(arr) - 1

#     while i < j:
#         arr[i] , arr[j] = arr[j] , arr[i]
#         i+=1
#         j-=1
#     return arr
# n = int(input())
# arr = list(map(int,input().split()))

# print(reverse(arr))


def rev(arr):
    # arr[::-1]
    i = 0;
    j = len(arr) - 1
    
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return " ".join(map(str, arr))


n = int(input())
arr = list(map(int,input().split()))

result = rev(arr)
print(result)


