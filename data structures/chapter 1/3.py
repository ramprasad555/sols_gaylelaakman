def check_unique_characters(x):
    y = ""
    for j in range(len(x)):
        flag = False
        for i in range(j+1,len(x)):
            if i < len(x)-1:
                if x[j] == x[i]:
                    flag = True
                    break
        if not flag:
            y += (x[j])
    print(y)
    return True

s = "helo"
print(check_unique_characters(s))