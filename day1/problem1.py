"""
Input: Two integers separated by space
Output: Their sum

Example:
Input: 5 3
Output: 8

Input: -10 20
Output: 10

Input: 100 200
Output: 300
"""


# old


# firstInput = int(input("Enter a First Num : "))
# sceoundInput = int(input("Enter a sceound Num : "))



# print(firstInput + sceoundInput)



# def solve():
#     try:
#         a,b = map(int,input("Enter a number : ").split())
#         print(a+b)
#     except ValueError:
#         print("Invalid number")

# solve()


"""
5
1,2,3,-4,5

output : 11
"""

def solve_positive():
    try:
        userInput = int(input("userFirst Input :- "))
        lst = list(map(int,input().split()))

        total = 0

        for num in lst:
            if num > 0:
                total+=num
        print(total)
    

    except ValueError:
        print("Invaild")

solve_positive()
