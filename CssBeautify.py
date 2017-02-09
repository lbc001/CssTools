import argparser

def Beautify(data):
    result=""
    while data.find("}")!=-1:
        index=data.find("{")
        result+=data[:index+1]+"\n"
        data=data[index+1:]
        while data.find(";")!=-1 and data.find(";")<data.find("}"):
            result+="    "+data[:data.find(";")]+";"+"\n"
            data=data[data.find(";")+1:]
        result+="    "+data[:data.find("}")]+"\n"
        result+="}"+"\n"
        data=data[data.find("}")+1:]
    return result

if __name__=="__main__":
    parser=argparser.ParserFormatter(description="fuck!")
    parser.add_argument("-i",dest="InputFile",type=str,help="enter the input css files")
    parser.add_argument("-o",dest="OutputFile",type=str,help="enter the output css files")
    option=parser.parse_args()
    with open(option.InputFile,"r") as f:
        data=f.read()
    with open(option.OutputFile,"w") as f:
        f.write(Beautify(data))