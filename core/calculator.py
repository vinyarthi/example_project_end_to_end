from __future__ import annotations

def add(num1: float,num2: float) -> float:
    return num1 + num2

def multiply(num1: float ,num2: float) -> float:
    return num1 * num2

def divide(num1: float,num2: float) -> float:
    if(num2!=0):
        return num1/num2
    else:
        raise Exception("Divide by zero error!")

def subtract(num1: float,num2: float) -> float:
    return num1 - num2

