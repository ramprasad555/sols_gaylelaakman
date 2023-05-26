def check_unique_characters(x):
    for j in range(len(x)):
        for i in range(j+1,len(x)):
            if i < len(x)-1:
                if x[j] == x[i]:
                    return False
    return True

s = "hello"
print(check_unique_characters(s))