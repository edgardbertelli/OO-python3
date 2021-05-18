def cria_conta(numero, titular, saldo, limite):
    conta = {numero: 123, titular: "Edgard Bertelli",
             saldo: 5000.00, limite: 8000.00}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo: {}".format(conta["saldo"]))
