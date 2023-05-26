cstring = "abcd\0"
x = ""
for i in range(len(cstring)-1, -1, -1):
   x += cstring[i]
print(x)


