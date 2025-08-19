import mysql.connector
import transform

conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_pass",
    database = "your_db"        # should exist in your workbench
)

cursor = conn.cursor()

# cursor.execute("drop table if exists pokemon_info;")      # fk constraint fails so manually have to drop on changing schema

cursor.execute("""
create table if not exists pokemon_info (
               pokemon_id int primary key,
               name text,
               height int,
               weight int,
               base_experience int
)
""")

cursor.execute("drop table if exists abilities;")

cursor.execute("""
create table if not exists abilities (
               ability_id int auto_increment primary key,
               pokemon_id int,
               ability_name text,
               foreign key(pokemon_id) references pokemon_info(pokemon_id)
)
""")

# insert data
data = transform.transformed_data.iloc[0]

# insert base info
cursor.execute("insert into pokemon_info (pokemon_id, name, height, weight, base_experience) values (%s, %s, %s, %s, %s)",
               (int(data['id']), 
                str(data['name']), 
                int(data['height']), 
                int(data['weight']), 
                int(data['base_experience']))
              )

# insert abilities
for a in data['abilities']:
    ability_name = a['ability']['name']
    cursor.execute("insert into abilities (pokemon_id, ability_name) values (%s, %s)",
                   (int(data['id']), 
                    str(ability_name))
                   )

conn.commit()
cursor.close()
conn.close()

print("🔥ETL complete!")