def issubstring(s1, s2):
    if s1 in s2:
        return True
    else:
        return False
    
s2 = "waterjottle"
s1 = "erbottlewat"
if len(s1) == len(s2):
    s2 = s2 + s1
    print(issubstring(s1,s2))
else:
     print(False)