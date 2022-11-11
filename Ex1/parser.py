from abc import ABC
from inspect import stack
from multiprocessing.dummy import Array
from operator import is_not
import queue
from tokenize import Double
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


def replaceTheMinus(array):
    array1=[]
    for i in range(len(array)):
        if array[i]=="-":
            if(array[i-1]=="(" or i==0):
                array1.append(array[i+1] * -1)

        else:
            array1.append(array[i])
            
                 



#implement the parser function here
def parser(expression)->Double:
    q = queue.Queue(1000)
    stack1 = []
    stackExp = []
    splitExp = re.split("(?<=[-+*/()])|(?=[-+*/()])", expression)
    if(splitExp[-1]==''):
        splitExp.pop()

    if(splitExp[0]==''):
        splitExp.pop(0)    

#5*(2+1)




    for s in splitExp:
        if (isfloat(s)):
            q.put(s)
        else:
            if s=="/" or s=="*" or s=="(":
                stack1.append(s)
                

            if s=="-" or s=="+":
                while  len(stack1)>0 and (stack1[-1]!="("):
                    q.put(stack1.pop())
                stack1.append(s)
                
            if s==")":
                while stack1[-1]!="(":
                    q.put(stack1.pop())
                stack1.pop()
                

    while len(stack1)>0:
        q.put(stack1.pop())

    for s2 in q.queue:
        if (isfloat(s2)):
            stackExp.append(Num(float(s2)))
        else:
            right1 = stackExp.pop()
            if(len(stackExp) > 0):
                left1 = stackExp.pop()
            else:
                if(s2=="*" or s2=="/"):
                    left1=Num(1)
                else:
                    left1=Num(0)
            if s2=="/":
                stackExp.append(Div(left1, right1))
                
            if s2=="*":
                stackExp.append(Mul(left1, right1))
                
            if s2=="+":
                stackExp.append(Plus(left1, right1))
                
            if s2=="-":
                stackExp.append(Minus(left1, right1))
                

    return float(math.floor((stackExp.pop().calc() * 1000)) / 1000);