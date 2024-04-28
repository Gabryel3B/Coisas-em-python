import time

b = int(input("Insira o valor: "))

while b > 0:
    print(b)
    b-=1
    time.sleep(1)

print("cabou")