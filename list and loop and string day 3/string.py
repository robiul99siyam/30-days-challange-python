# # string practice problem

# text = "hello python"

# print(text[0]) # output (h) indexing
# print(text[-1]) # negative index (n)
# print(text[0:4])
# print(len(text))

# print(text.upper())
# print(text.capitalize())
# print(text.replace("python","world"))
# print(text.split())


# =========== reverse string ==========

# def resverse_string():
#     text = input("give me a input : ")
#     resverse_text = text[::-1]
#     print(resverse_text)

# resverse_string()



# def resverse_string():
#     text = "hello bangladesh"

#     rev = ""
#     for ch in text:
#         rev = ch + rev
#     print(rev)

# resverse_string()


#==================== two pointer method ========>


# def reverse_string(value):

#     temp = []
#     for ch in value:
#         temp.append(ch)
    

#     left = 0
#     right = len(temp) - 1


#     while left < right:
#         temp[left],temp[right] = temp[right],temp[left]
#         left+=1
#         right-=1

#     text = "".join(temp)
#     print(text)
    

# reverse_string("abc")

text = ['a','b','c']

# convert the normal text 

print("".join(text))