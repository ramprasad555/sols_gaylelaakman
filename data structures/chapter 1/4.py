def check_anagrams(x,y):
    if len(x) == len(y):
        xl = list(x)
        yl = list(y)
        for i in xl :
            for j in yl:
                if j == i:
                    yl.remove(i)
        if len(yl) == 0:
            return True
        else:
            return False
    else:
        return False
    
x = "cinema"
y = "iceman"
print(check_anagrams(x,y))

