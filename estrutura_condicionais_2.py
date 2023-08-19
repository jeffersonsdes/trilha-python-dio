saldo = 500
saque = 501

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque")