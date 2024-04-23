


# users
IuryCash = lambda : {
    "name": "Iury",
    "password": "tete001",
    "money": 300,
    "creditLimit": 100000,
    "tStatus": "No transaction yet",
}

BetimCash = lambda : {
    "name": "Betim",
    "password": "tete001",
    "money": 150,
    "creditLimit": 5000,
    "tStatus" : "No transaction yet",
}

BigasCash = lambda : {
    "name": "Bigas",
    "password": "tete001",
    "money": 150,
    "creditLimit": 5000,
    "tStatus" : "No transaction yet",
}

AdalbertoCash = lambda : {
    "name": "Adalberto",
    "password": "tete001",
    "money": 150,
    "creditLimit": 5000,
    "tStatus" : "No transaction yet",
}

AngeloCash = lambda : {
    "name": "Angelo",
    "password": "tete001",
    "money": 150,
    "creditLimit": 5000,
    "tStatus" : "No transaction yet",
}

LarissaCash = lambda : {
    "name": "Larissa",
    "password": "tete001",
    "money": 150,
    "creditLimit": 5000,
    "tStatus" : "No transaction yet",
}


# Parte 1

arrayUsers = lambda : [IuryCash(), BetimCash(), BigasCash(), AdalbertoCash(), AngeloCash(), LarissaCash()]
userName = lambda name: [user for user in arrayUsers() if user["name"] == name][0]


login = users = lambda name, password: [user for user in arrayUsers() if user["name"] == name and user["password"] == password][0]

createTransaction = lambda user: user.update({"tStatus": "created"})

delMoney = lambda user, amount: user.update({"money": user["money"] - amount, "tStatus" : "transaction completed successfully"}) if user["money"] >= amount else user.update({"tStatus" : "transaction failed!"})

addMoney = lambda user, amount: user.update({"money": user["money"] + amount, "tStatus" : "transaction completed successfully"})






# Parte 2

cash = lambda amount : amount

receiveCash = lambda user, amount: delMoney(user, amount)

printPaymentReceipt = lambda user: print(f"Payment receipt printed for transaction by {user['name']}\n")

returnPaymentReceipt = lambda user: f"Payment receipt returned for transaction by {user['name']}"

completeTransaction = lambda user: user.update({"tStatus": "completed"})





# Parte 3

removeCredit = lambda user, amount: user.update({"creditLimit": user["creditLimit"] - amount, "tStatus" : "transaction in credit executed"}) if user["creditLimit"] >= amount else user.update({"tStatus" : "transaction failed, not credit enough"})

def fundTransfer(user1, user2, amount):
    delMoney(user1, amount)
    addMoney(user2, amount)

def cashFunction(name, password, amount):
    user = login(name, password)
    createTransaction(user)
    print(f"Cash user -> \n{user}\n")
    cashTest =  cash(amount)
    receiveCash(user, cashTest)
    print(f"Cash executed for user -> \n{user}\n")
    printPaymentReceipt(user)
    returnPaymentReceipt(user)
    completeTransaction(user)
    print(f"Cash completed for user -> \n{user}\n")
    return user["tStatus"]


def creditFunction(name, password, amount):
    user = login(name, password)
    createTransaction(user)
    print(f"Credit user -> \n{user}\n")
    removeCredit(user, amount)
    print(f"Credit executed for user -> \n{user}\n")
    completeTransaction(user)
    print(f"Credit completed for user -> \n{user}\n")
    return user["tStatus"]

def fundTrasfFunction(nameToTransefer, password, amount, nameToReceive):
    user1 = login(nameToTransefer, password)
    user2 = userName(nameToReceive)
    createTransaction(user1)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    fundTransfer(user1, user2, amount)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    completeTransaction(user1)
    completeTransaction(user2)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    return user1["tStatus"]


# Testando as funções
cashFunction("Iury", "tete001", 100)
# fundTrasfFunction("Paulo", "tete001", 100, "Capelo")
# creditFunction("Larissa", "tete001", 100)