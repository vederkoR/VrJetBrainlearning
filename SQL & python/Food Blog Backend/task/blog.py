import sqlite3


def first_stage_db_creation(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS meals(
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT UNIQUE NOT NULL 
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS ingredients(
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT UNIQUE NOT NULL 
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS measures(
    measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    measure_name TEXT UNIQUE 
    );
    """)


def first_stage_db_fill_up(cur):
    for i in ["breakfast", "brunch", "lunch", "supper"]:
        cur.execute(f"""
        INSERT INTO meals(meal_name)
        VALUES (\"{i}\");
        """)

    for i in ["milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"]:
        cur.execute(f"""
        INSERT INTO ingredients(ingredient_name)
        VALUES (\"{i}\");
        """)

    for i in ["ml", "g", "l", "cup", "tbsp", "tsp", "dsp", ""]:
        cur.execute(f"""
        INSERT INTO measures(measure_name)
        VALUES (\"{i}\");
        """)


def second_stage_create_receipt_table(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS recipes(
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_name TEXT NOT NULL,
    recipe_description TEXT
    );
    """)


def second_and_third_stage_fill_receipt_table(cur):
    while True:
        name = input("Recipe name:")
        if name == '':
            break
        description = input("Recipe description:")
        insert_query = cur.execute(f'''
        INSERT INTO recipes(recipe_name, recipe_description)
        VALUES (\"{name}\", \"{description}\");
        ''')
        receipt_id = insert_query.lastrowid
        print("1) breakfast  2) brunch  3) lunch  4) supper")
        when_serve = input("When the dish can be served:").split(" ")
        for meal_id in when_serve:
            cur.execute(f'''
            INSERT INTO serve(recipe_id, meal_id)
            VALUES (\"{receipt_id}\", \"{meal_id}\")
            ''')




def third_stage_enable_fk(cur):
    cur.execute("""
    PRAGMA foreign_keys = ON;
    """)


def third_stage_create_intermediate_table(cur):
    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS serve(
    serve_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL REFERENCES recipes(recipe_id),
    meal_id INTEGER NOT NULL REFERENCES meals(meal_id))
    """)



def main():
    conn = sqlite3.connect("food_blog.db")
    cursor = conn.cursor()

    # enable foreign keys
    third_stage_enable_fk(cursor)
    conn.commit()

    # create all tables
    first_stage_db_creation(cursor)
    second_stage_create_receipt_table(cursor)
    conn.commit()
    third_stage_create_intermediate_table(cursor)
    conn.commit()
    first_stage_db_fill_up(cursor)
    conn.commit()
    second_and_third_stage_fill_receipt_table(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()