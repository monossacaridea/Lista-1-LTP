# Exercício 3: Escreva um programa que imprima os primeiros 10 números da sequência de Fibonacci.

a = 0
b = 1
print(a)
print(b)

for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c
