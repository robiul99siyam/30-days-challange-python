# strList = ['JS','REACT','PYTHON','JAVA']

# longestValue = ''
# longestValueCount = 0

# for value in strList:
#     if len(value) > len(longestValue):
#         longestValue = value

# print(longestValue)
# print(len(longestValue))
# # 





swapList = [5,2,1,3]


left,right = 0,len(swapList) - 1

while left < right:
    swapList[left],swapList[right] = swapList[right],swapList[left]
    print(f"Swapping: swapList[{left}]={swapList[left]} ↔ arr[{right}]={swapList[right]}")
    left+=1
    right-=1

print(swapList)

