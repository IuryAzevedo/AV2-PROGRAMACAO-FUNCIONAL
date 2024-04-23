import mysql.connector2

connect_to_database = lambda: mysql.connector2.connect(
    host="localhost",
    user="root",
    password="root",
    database="av2_db"
)

join = lambda table1, table2, column1, column2: (
    f"INNER JOIN {table2} ON {table1}.{column1} = {table2}.{column2}",
)

generate_select = lambda columns: (
    f"SELECT {', '.join(columns)}",
)

# Exemplo de Uso;
join_State1 = join('GAMES', 'VIDEOGAMES', 'id_console', 'id_console')
join_State2 = join('VIDEOGAMES', 'COMPANY', 'id_company', 'id_company')
select_State = generate_select(['GAMES.title', 'GAMES.release_date', 'COMPANY.name', 'VIDEOGAMES.name'])

generate_query = lambda select_State, join_State1, join_State2: (
    f"{select_State[0]} FROM GAMES {join_State1[0]} {join_State2[0]}"
)

query = generate_query(select_State, join_State1, join_State2)

conn = connect_to_database()

cur = conn.cursor()

cur.execute(query)

results = cur.fetchall()
print(results)

for result in results:
    print(result)

cur.close()
conn.close()