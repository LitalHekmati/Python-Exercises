from abc import ABC
from inspect import stack
from operator import is_not
from tokenize import Double
from turtle import left, right
from abc import ABC,abstractmethod
from queue import Empty, Queue
import math


class Expression(ABC):
    @abstractmethod
    def calc(self)->Double:
        pass

# implement the classes here

class BinaryExpression(Expression):
    @abstractmethod
    def __init__(self, left, right):
        self.left = super()
        self.right = super()
        pass

class Num(Expression):
    def __init__(self, val):
        self.val = val
    def setVal(self,val):
        self.val=val
    def calc(self) -> Double:
        return self.val

class Plus(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left,right)
    def calc(self) -> Double:
        return left.calc() + right.calc()
    
class Minus(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> Double:
        return left.calc() - right.calc()
    
class Mul(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> Double:
        return left.calc() * right.calc()

class Div(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> Double:
        return left.calc() / right.calc()


#implement the parser function here
def parser(expression)->Double:
    q = Queue(100)
    stack1 = []
    stackExp = []
    splitExp = expression.split("(?<=[-+*/()])|(?=[-+*/()])")

    for s in splitExp:
        if isinstance(s, Double):
            q.put(s)
        else:
            if s=="/" or s=="*" or s=="(":
                stack1.append(s)
                break

            elif s=="-" or s=="+":
                while not stack1 and stack1[0]!="(":
                    q.put(stack1.pop)
                stack1.append(s)
                break
            elif s==")":
                while stack1[0]!="(":
                    q.put(stack1.pop)
                stack1.pop
                break

    while not stack1:
        q.put(stack1.pop)

    for s2 in q:
        if isinstance(s2, Double):
            stackExp.append(Num(float(s2)))
        else:
            right1 = stackExp.pop
            left1 = stackExp.pop
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