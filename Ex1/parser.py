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
    stack = []
    stackExp = []		
    splitExp = expression.split("(?<=[-+*/()])|(?=[-+*/()])")

    for s in splitExp:
        if isinstance(s, double):
            q.put(s)
        else:
            match s:
                case "/":
                    stack.append(s)
                    break
                case "*":
                    stack.append(s)
                    break
                case "(":
                    stack.append(s)
                    break
                case "+":
                    while not stack and stack[-1] is not "(":
                        q.put(stack.pop)
                    stack.append(s)
                    break
                case "-":
                    while not stack and stack[-1] is not "(":
                        q.put(stack.pop)
                    stack.append(s)
                    break
                case ")":
                    while stack[-1] is not "(":
                        q.put(stack.pop)
                    stack.pop
                    break
                
    while not stack:
        q.put(stack.pop) 
    
    for str in q:
        if isinstance(str, double):
            stackExp.append(Num(float(str)))
        else:
            right = stackExp.pop
            left = stackExp.pop
            match str:
                case "/":
                    stackExp.append(Div(left,right))
                    break
                case "*":
                    stackExp.append(Mul(left,right))
                    break
                case "+":
                    stackExp.append(Plus(left,right))
                    break
                case "-":
                    stackExp.append(Minus(left,right))
                    break


    return math.floor((stackExp.pop().calc * 1000)) /1000; 


