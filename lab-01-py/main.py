
def sum(arg1, arg2):
    if type(arg1) is complex or type(arg2) is complex:
        sum = complex(arg1.real + arg2.real, arg1.imag + arg2. imag)
        return sum
    
    return float(arg1) + float(arg2)


if __name__ == "__main__":
    sum = sum(2,3)
    print(f'suma = {sum}')
    print(f'__name__ = {__name__}')
    
# typowanie slabe i dynamiczne

