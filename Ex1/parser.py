from abc import ABC
from inspect import stack
from operator import is_not
from tokenize import Double
from turtle import left, right
from abc import ABC,abstractmethod
from queue import Empty, Queue
import math
import re



class Expression(ABC):
    @abstractmethod
    def calc(self)->Double:
        pass

# implement the classes here

class BinaryExpression(Expression,ABC):
    @abstractmethod
    def __init__(self, left, right):
        self.left = left
        self.right = right
        pass
   

class Num(Expression):
    def __init__(self, val) :
        self.val = val
    def setVal(self,val):
        self.val=val
    def calc(self) -> Double:
        return self.val


class Plus(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left,right)
    def calc(self) -> Double:
        return self.left.calc() + self.right.calc()
    
class Minus(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left,right)
    def calc(self) -> Double:
        return self.left.calc() - self.right.calc()
    
class Mul(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left,right)
    def calc(self) -> Double:
        return self.left.calc() * self.right.calc()

class Div(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left,right)
    def calc(self) -> Double:
        return self.left.calc() / self.right.calc()


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False



#implement the parser function here
def parser(expression)->Double:
    q = Queue(1000)
    stack1 = []
    stackExp = []
    splitExp = re.split("(?<=[-+*/()])|(?=[-+*/()])", expression)
    print("split is "+splitExp[-1])
    if(splitExp[-1]==''):
        splitExp.pop()

    if(splitExp[0]==''):
        splitExp.pop(0)    
    print(splitExp)


    
    for s in splitExp:
        print("s is "+s)
        if (isfloat(s)):
            q.put(s)
        else:
            print("first1 check")
            if s=="/" or s=="*" or s=="(":
                stack1.append(s)
                

            if s=="-" or s=="+":
                print(stack1)
                while  len(stack1)>0 and (stack1[-1]!="("):
                    q.put(stack1.pop())
                    print("+/-")
                stack1.append(s)
                
            if s==")":
                while stack1[-1]!="(":
                    q.put(stack1.pop())
                stack1.pop()
                

    while len(stack1)>0:
        q.put(stack1.pop())


    for s2 in q:
        if (isfloat(s2)):
            stackExp.append(Num(float(s2)))
        else:
            right1 = stackExp.pop()
            left1 = stackExp.pop()
            if s2=="/":
                stackExp.append(Div(left1, right1))
                break
            elif s2=="*":
                stackExp.append(Mul(left1, right1))
                break
            elif s2=="+":
                stackExp.append(Plus(left1, right1))
                break
            elif s2=="-":
                stackExp.append(Minus(left1, right1))
                break

    return Double(math.floor((stackExp.pop().calc() * 1000)) / 1000);