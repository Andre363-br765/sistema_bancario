from utils.helpers import ler_float
from operacoes.operacoes import depositar, sacar, exibir_extrato
from contas.contas import criar_usuario, criar_conta, listar_contas
from menu.menu import menu

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        # Loop principal reorganizado
        opcao = menu()

        if opcao == "1":  # Novo usuário
            criar_usuario(usuarios)

        elif opcao == "2":  # Nova conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "3":  # Depositar
            valor = ler_float("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "4":  # Sacar
            valor = ler_float("Informe o valor do saque: ")
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "5":  # Extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":  # Listar contas
            listar_contas(contas)

        elif opcao == "0":  # Sair
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
