a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

conta = input("Qual operação deseja realizar? (+, -, *, /): ")

if conta == "+":
    print("Resultado:", a + b)

elif conta == "-":
    print("Resultado:", a - b)

elif conta == "*":
    print("Resultado:", a * b)

elif conta == "/":
    print("Resultado:", a / b)

else:
    print("Operação inválida!")