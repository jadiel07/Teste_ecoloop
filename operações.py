def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def analisar_numero(n):
    par_ou_impar = "par" if n % 2 == 0 else "ímpar"
    primo_ou_nao = "primo" if eh_primo(n) else "não primo"
    return par_ou_impar, primo_ou_nao

def main():
    print("=== analise de operações matematicas ===")
    try:
        a = int(input("digite o primeiro numero inteiro: "))
        b = int(input("digite o segundo numero inteiro: "))
    except ValueError:
        print("digite apenas números inteiros.")
        return

    # operações
    print("\n--- operações ---")
    print(f"soma: {a + b}")
    print(f"subtração: {a - b}")
    print(f"multiplicação: {a * b}")
    
    if b != 0:
        print(f"divisão: {a / b}")
    else:
        print("divisão: não é possivel dividir por zero.")

    # analise dos numeros
    print("\n--- analise dos Números ---")
    for n in [a, b]:
        paridade, primalidade = analisar_numero(n)
        print(f"numero {n}: {paridade}, {primalidade}")

if __name__ == "__main__":
    main()
