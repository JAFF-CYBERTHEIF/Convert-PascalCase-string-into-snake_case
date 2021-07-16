def to_underscore(st):
    string=str(st)
    res=""
    for i in range(len(string)):
        if string[i].isupper()==True:
            if i==0:
                res=res+string[i].lower()
            if i!=0:
                res=res+"_"
                res=res+string[i].lower()
        else:
            res=res+string[i]
    return res
print("Enter a CamelCase string to get  snake_case notation")
st=input()
print(to_underscore(st))
