from abc import ABC
from inspect import stack
from operator import is_not
from tokenize import Double
from turtle import left, right
from numpy import double
from abc import ABC,abstractmethod
from queue import Empty, Queue
import math


class Expression(ABC):
    @abstractmethod
    def calc(self)->double:
        pass


# implement the classes here

class BinaryExpression(Expression):
    @abstractmethod
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Num(Expression):
    def __init__(self, val):
        self.val = val
    def setVal(self,val):
        self.val=val
    def calc(self) -> double:
        return self.val

class Plus(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> double:
        return left.calc() + right.calc()
    
class Minus(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> double:
        return left.calc() - right.calc()
    
class Mul(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> double:
        return left.calc() * right.calc()

class Div(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def calc(self) -> double:
        return left.calc() / right.calc()


#implement the parser function here
def parser(expression)->double:
    q = Queue(100)
    stack1 = []
    stackExp = []
    splitExp = expression.split("(?<=[-+*/()])|(?=[-+*/()])")

    for s in splitExp:
        if isinstance(s, double):
            q.put(s)
        else:
            if s is "/" or "*" or "(":
                stack1.append(s)
                break

            elif s is "-" or "+":
                while not stack1 and stack1[-1] is not "(":
                    q.put(stack1.pop)
                stack1.append(s)
                break
            elif s is ")":
                while stack1[-1] is not "(":
                    q.put(stack1.pop)
                stack1.pop
                break

    while not stack1:
        q.put(stack1.pop)

    for s2 in q:
        if isinstance(s2, double):
            stackExp.append(Num(float(s2)))
        else:
            right1 = stackExp.pop
            left1 = stackExp.pop
            if s2 is "/":
                stackExp.append(Div(left1, right1))
                break
            elif s2 is "*":
                stackExp.append(Mul(left1, right1))
                break
            elif s2 is "+":
                stackExp.append(Plus(left1, right1))
                break
            elif s2 is "-":
                stackExp.append(Minus(left1, right1))
                break

    return double(math.floor((stackExp.pop().calc * 1000)) / 1000);