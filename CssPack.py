import argparser

def Pack(data):
    result=""
    for line in data:
        line=line.replace("\n","")
        if line.endswith("{") or line.startswith("}"):
            result+=line.rstrip()
        else:
            temp=line.split(":")
            result+=temp[0].replace(" ","")+":"
            result+=temp[-1].rstrip()
    return result

if __name__=="__main__":
    parser=argparser.ParserFormatter(description="fuck!")
    parser.add_argument("-i",dest="InputFile",type=str,help="enter the input css files")
    parser.add_argument("-o",dest="OutputFile",type=str,help="enter the output css files")
    option=parser.parse_args()
    with open(option.InputFile,"r") as f:
        data=f.readlines()
    with open(option.OutputFile,"w") as f:
        f.write(Pack(data))