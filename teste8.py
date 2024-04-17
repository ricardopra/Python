while True:
    num = int(input())    
    if 0 <= num <= 10:        
        for i in range(1, 11):
            print(f"{num}x{i}={num * i}")
        break
    else:
        print("VALOR INVÁLIDO")