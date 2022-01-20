#coding: utf-8

def AxB(a , b):
    total = a * b
    return total

class Math2():
    
    def __init__(self ,a ,b):
        self.a = a
        self.b = b
        self.answer = 0

    def addanswer(self):
        self.answer = self.a * self.b 

    def divanswer(self):
        if self.b == 0:
            print("can't div set 0")
        else:
            self.answer = self.a / self.b
    
    def __str__(self):
        return "Answer: {ans}".format(ans = self.answer)

    def __doc__(self):
        print("addanswer(a,b) : a+b")
        print("divanswer(a,b) : a/b")


def main():
    print("this MyModule02!!!")

if __name__ == "__main__":
    main()