# Definição da função que soma dois números
def soma(num1, num2):
    return num1 + num2

# Fluxo principal do programa
if __name__ == "__main__":
    # Definindo dois números
    numero1 = 10
    numero2 = 20
    
    # Chamando a função soma e armazenando o resultado
    resultado = soma(numero1, numero2)
    
    # Exibindo o resultado
    print(f"A soma de {numero1} e {numero2} é: {resultado}")
