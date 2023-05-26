def replace_with_20(s):
    y = ""
    for i in s:
        if i == " ":
            y += "%20"
        else:
            y += i
    return y

s = "hello world"
print(replace_with_20(s))

