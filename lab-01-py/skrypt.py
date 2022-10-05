
import sys # import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2 + 1)):
        if (num % i) == 0:
            return False
    return True


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if is_prime(int(arg)):
            print(arg)

