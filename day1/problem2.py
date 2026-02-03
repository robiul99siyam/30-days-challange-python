"""
Input: A single integer
Output: "Even" or "Odd"

Example:
Input: 4
Output: Even

Input: 7
Output: Odd

Input: 0
Output: Even

Input: -3
Output: Odd
"""


numberInput = int(input("Enter a number : "))

if numberInput < 0:
    print("odd")
elif numberInput % 2!= 0:
    print("odd")
else:
    print("even")
