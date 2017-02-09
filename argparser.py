import sys

class ParserFormatter:
    def __init__(self,description=""):
        self._description=description
        self._matching={}
        self._visited=[]
        self._unmatching=[]

    def add_argument(self,option,dest,type,help):
        self._matching[option]=(dest,type,help)

    def print_argument(self,error=[],level=0):
        result="usage: {} [-h]".format(sys.argv[0])
        for key in self._matching:
                result+=" [{} {}]".format(key,self._matching[key][0].upper())
        result+="\n"
        if level==0:
            result+="\n"+self._description+"\n\n"
            result+="optional arguments:\n"
            result+="  -h, --help     show this help message and exit\n"
            for key in self._matching:
                result+=" {} {}  {}\n".format(key,self._matching[key][0].upper(),self._matching[key][2])
        elif level==1:
            result+="{}: error: unrecognized arguments: {}".format(sys.argv[0]," ".join(self._unmatching))
        elif level==2:
            result+="{}: error: argument {}: invalid int value: '{}'".format(sys.argv[0],error[0],error[1])
        else:
            result+="{}: error: no arguments have been detectioned!".format(sys.argv[0])
        print(result)
        
    def parse_args(self):
        exec_result="class option:\n"
        for index,element in enumerate(sys.argv[1:]):
            if element=="-h" or element=="--help":
                self.print_argument()
                sys.exit(0)
            if element.startswith("-"):
                result=self._matching.get(element,None)
                if result is None:
                    self._unmatching.append(element)
                else:
                    if result[1]==int:
                        try:
                            int(sys.argv[1:][index+1])
                            exec_result+="    "+result[0]+"="+sys.argv[1:][index+1]+"\n"
                            self._visited.append(sys.argv[1:][index+1])
                        except ValueError:
                            self.print_argument(error=[element,sys.argv[1:][index+1]],level=2)
                            sys.exit(0)
                    else:
                        exec_result+="    "+result[0]+"="+"'{}'".format(sys.argv[1:][index+1])+"\n"
                        self._visited.append(sys.argv[1:][index+1])
            elif element in self._visited:
                continue
            else:
                self._unmatching.append(element)
        if len(self._unmatching)!=0:
            self.print_argument(level=1)
            sys.exit(0)
        else:
            if exec_result=="class option:\n":
                self.print_argument(level=3)
                sys.exit(0)
            exec(exec_result)
            return option()
                        




                    