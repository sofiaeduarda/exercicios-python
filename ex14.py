print("Classificação do produto: ")
print("1 - Peso ideal e sem defeitos")
print("2 - Pequenas variações")
print("3 - Fora dos padrões")

opcao = int(input("Digite o número da classificação: "))

if opcao == 1:
    print("Produto PREMIUM")
elif opcao == 2:
    print("Produto STANDARD")
elif opcao == 3:
    print("Produto REJEITADO")
else:
    print("Opção inválida.")