import mysql.connector

# Função para conexão com o banco de dados MySQL
connect_to_database = lambda: mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="av2_db"
)

user = lambda id, name, country, id_console: (
    "INSERT INTO USERS (id, name, country, id_console) VALUES (%s, %s, %s, %s)",
    (id, name, country, id_console)
)

removeUser = lambda user_id: (
    "DELETE FROM USERS WHERE id = %s",
    (user_id,)
)

list_Users = lambda: (
    "SELECT * FROM USERS",
    ()
)

videogame = lambda id_console, name, id_company, release_date: (
    "INSERT INTO VIDEOGAMES (id_console, name, id_company, release_date) VALUES (%s, %s, %s, %s)",
    (id_console, name, id_company, release_date)
)

removeVideogame = lambda game_id: (
    "DELETE FROM VIDEOGAMES WHERE id_console = %s",
    (game_id,)
)

list_Videogames = lambda: (
    "SELECT * FROM VIDEOGAMES",
    ()
)

game = lambda id_game, title, genre, release_date, id_console: (
    "INSERT INTO GAMES (id_game, title, genre, release_date, id_console) VALUES (%s, %s, %s, %s, %s)",
    (id_game, title, genre, release_date, id_console)
)

removeGame = lambda game_id: (
    "DELETE FROM GAMES WHERE id_game = %s",
    (game_id,)
)

list_games = lambda: (
    "SELECT * FROM GAMES",
    ()
)

company = lambda id_company, name, country: (
    "INSERT INTO COMPANY (id_company, name, country) VALUES (%s, %s, %s)",
    (id_company, name, country)
)

removeCompany = lambda company_id: (
    "DELETE FROM COMPANY WHERE id_company = %s",
    (company_id,)
)

list_companies = lambda: (
    "SELECT * FROM COMPANY",
    ()
)

queryExecute = lambda query, values: (
    cursor.execute(query, values)
)

results = lambda: (
    cursor.fetchall()
)

#-------------- usabilidade

connection = connect_to_database()
cursor = connection.cursor()


queryExecute(*user(2, 'usuario_teste', 'BR', 1))
connection.commit()

queryExecute(*list_Users())
users = results()
print("Users:")
for user in users:
    print(user)

# queryExecute(*list_Videogames())
#  = results()
# print("Videogames:")
# for videogame in :
#     print(videogame)

# queryExecute(*list_games())
# games = results()
# print("Games:")
# for game in games:
#     print(game)

# queryExecute(*list_companies())
# companies = results()
# print("Companies:")
# for company in companies:
#     print(company)

# Fechar conexão com o banco de dados
cursor.close()
connection.close()