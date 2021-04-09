def missing_char(str, n):
    return str[:n] + str[n+1:]
y=input("Write any Word ...")
n=input("write a number within the range of the word")
print (missing_char(y, int(n)))
