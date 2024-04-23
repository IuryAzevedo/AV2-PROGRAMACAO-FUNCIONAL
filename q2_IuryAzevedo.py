from q1_IuryAzevedo import *
import threading
# Descomente as funcoes para testa-las
# Testes

# assert("completed" in cashFunction("Iury", "tete001", 100))

# assert("completed" in fundTrasfFunction("Iury", "tete001", 100, "Larissa"))

# assert("completed" in cashFunction("Larissa", "tete001", 100))

# Money

pbranchesCash = 100
threadsCash = []
for i in range(pbranchesCash):
    t = threading.Thread(target=cashFunction, args=("Larissa", "tete001", 1))
    threadsCash.append(t)
    t.start()
for t in threadsCash:
    t.join()


# # Fundos
# pbranchesFund = 100
# threadsFund = []
# for i in range(pbranchesFund):
#     t = threading.Thread(target=fundTrasfFunction, args=("Iury", "tete001", 1, "Angelo"))
#     threadsFund.append(t)
#     t.start()
# for t in threadsFund:
#     t.join()


# Crédito
# pbranchesCredit = 1500
# threadsCredit = []
# for i in range(pbranchesCredit):
#     t = threading.Thread(target=creditFunction, args=("Iury", "tete001", 1))
#     threadsCredit.append(t)
#     t.start()
# for t in threadsCredit:
#     t.join()
