def palindromeCheckFunction(values):

    #======= palindorme check ===========
    orginalValue = str(values)
    resverseString = orginalValue[::-1]

    for v in resverseString:
        if v == "0":
            continue
        else:

            print(v, end="")
    
    print()
    if  resverseString == orginalValue:
        print("YES") 
    else:
        print("NO")
         


userInput = int(input())
palindromeCheckFunction(userInput)

