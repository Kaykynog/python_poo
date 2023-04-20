
# num = 10
# while num > 0:
#     print(num)
#     num -= 1
numero = 5
def recursividade(num):

    if num == 0:
        return 1
    print(f"{num}", end=' ' )
    print("X" if num > 1 else "=", end=' ')
    

    num *= recursividade(num-1)
    return num 
resultado = recursividade(numero)
print(resultado)


