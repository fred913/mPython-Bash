#coding:utf-8
#Bash on Python
#内置环境pip（准确说是仿pip，是upip的命令行套壳）
#内置软件包ls cd pwd touch fedit（自制简易文本覆盖修改器）

import upip,os

welcome_string = '''
Bash on mPython v1.4
By FredTools
'''
user = 'root'
hostname = "mPython"

class pip():
    def __init__(self):
        self.name = "pip"
    def use(self,args):

        if args == []:
            return "This is a Command format of upip. "
        if args[0] == "install":
            if len(args) == 1:
                return "Usage: pip install [Package Name]"
            pkgs = args[1:]
            for pkg in pkgs:
                upip.install(pkg)
        return ""

class ls():
    def __init__(self):
        self.name = "ls"
    def use(self,args):
        output = ''
        if args == []:
            for thing in os.listdir("."):
                output += thing + "\n"
        return output

class pwd():
    def __init__(self):
        self.name = "pwd"
    def use(self,args):
        return os.getcwd()


class cd():
    def __init__(self):
        self.name = "cd"
    def use(self,args):
        if args == []:
            return "This is a Command format of chdir. "
        else:
            os.chdir(' '.join(args))
            return ""

class touch():
    def __init__(self):
        self.name = "touch"
    def use(self,args):
        if args == []:
            return "This is a Command format of touch. "
        elif os.path.isfile(' '.join(args)):
            return ""
        elif os.path.isdir(' '.join(args)):
            return "touch: %s: Is dir" % (' '.join(args))
        else:
            f = open(' '.join(args),"w")
            f.close()

class fedit():
    def __init__(self):
        self.name = "fedit"
    def use(self,args=[]):
        if args == []:
            return "This is a Eazy-to-Use text editor by FredTools. \nUsage: fedit filename [End-Target]\nFor Example:\nfedit a.txt EOF"
        else:
            if len(args) == 1:
                args.append('EOF')
            print("-----Fedit-----")
            print("--Enter %s to exit.-" % (args[1]))
            f = open(args[0],'w')
            a=input()
            while a!=args[1]:
                f.write(a)
            f.close()
            return "Wrote. "





def command(cmd):
    try:
        l = cmd.split(' ')
        print(l)
        cmdname = l[0]
        del l[0]
        print(eval(cmdname + "()").use(l))
    except:
        print("Bash: %s: Bad command. " % (cmd.split(' ')[0]))

def main():
    print(welcome_string)
    while True:
        try:
            cmd = input("%s@%s: %s%s " % (user,hostname,os.getcwd(),"#" if (user=='root') else "$"))
            if cmd == "":
                continue
            command(cmd)
            print("")
        except KeyboardInterrupt:
            print("Exited. ")
            break
        except:
            print("Error! Please cheak. ")
    print("Exited. ")


if __name__ == "__main__":
    main()
