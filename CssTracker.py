stack=[]
globaldict={}
with open("test.css","r") as f:
    data=f.readlines()

for line in data:
    line=line.replace("\n","")
    if line.endswith("{"):
        if len(stack)!=0:
            raise ValueError("it is not a great format of css file!")
        temp=[]
        if "," in line[:-1]:
            for name in line[:-1].split(","):
                temp.append(name)
            stack.append(temp)
        else:
            temp.append(line[:-1])
            stack.append(temp)
    elif line=="":
        continue
    elif line.endswith("}"):
        if len(stack)==0:
            raise ValueError("it is not a great format of css file!")
        else:
            stack.pop(0)
    else:
        names=stack[-1]
        for name in names:
            temp=globaldict.get(name,{})
            temp[line[:-1].lstrip().split(":")[0]]=line[:-1].lstrip().split(":")[1]
            globaldict[name]=temp
result=""
for key in globaldict:
    result+=key+"{"+"\n"
    for element in globaldict[key]:
        result+="    "+element+":"+globaldict[key][element]+";\n"
    result+="}\n"

print(result)
