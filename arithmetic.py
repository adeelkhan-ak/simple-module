import sys
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
if __name__ == "__main__":
    v= str(input())
    valOne=int (input())
    valTwo=int(input ())
    if v == "a":
        print(add(valOne, valTwo))
    elif v == "d":
        print(div(valOne, valTwo))
    elif v == "m":
        print(mul(valOne, valTwo))
    elif v == "s":
        print(sub(valOne, valTwo))
    else:
        pass