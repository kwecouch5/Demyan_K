from random import randint


def rand10(self):
    f=(randint(1,7)+randint(1,7)+randint(1,7))%10
    if f==0:
        f=10
    return f
print(rand10(2))