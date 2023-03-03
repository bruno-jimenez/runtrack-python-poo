def biggerNum(list):
    if len(list) == 0:
        return 0
    else:
        return max(list[0], biggerNum(list[1:]))
    
print(biggerNum([117, 343,  4, 5, 99999, 8989, 7, 8, 9909, 10]))