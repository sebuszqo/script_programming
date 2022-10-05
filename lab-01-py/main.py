# 1 
# def sum(arg1, arg2):
#     return arg1 + arg2

# 2
def sum(arg1, arg2):
    if type(arg1) is complex or type(arg2) is complex:
        sum = complex(arg1.real + arg2.real, arg1.imag + arg2. imag)
        return sum
    
    return float(arg1) + float(arg2)


# print(f'__name__ = {__name__}')
# __name__ = main --> przy import main

# 9
if __name__ == "__main__":
    print(f'suma = {sum(2,3)}')
    print(f'__name__ = {__name__}')
    
# typowanie silne i dynamiczne --> 2 + '2' = error

#  2 + 2  - 4 int
#  2 + 2.0 - 4.0 float
#  2 + '2' - TypeError: unsupported operand type(s) for +: 'int' and 'str'
#  
# zmienna = 2 
# type(zmienna) - <class 'int'>
# 
# zmienna = '2'
# type(zmienna) - <class 'str'>

