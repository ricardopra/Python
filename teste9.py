while True:    
    num = int(input())    
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)
        break
    else:
        print("VALOR INVÁLIDO")

