import sqlite3


def first_stage_db_creation(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS meals(
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT UNIQUE NOT NULL 
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS ingredients(
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT UNIQUE NOT NULL 
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS measures(
    measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    measure_name TEXT UNIQUE 
    )
    """)


def first_stage_db_fill_up(cur):
    for i in ["breakfast", "brunch", "lunch", "supper"]:
        cur.execute(f"""
        INSERT INTO meals(meal_name)
        VALUES (\"{i}\")
        """)

    for i in ["milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"]:
        cur.execute(f"""
        INSERT INTO ingredients(ingredient_name)
        VALUES (\"{i}\")
        """)

    for i in ["ml", "g", "l", "cup", "tbsp", "tsp", "dsp", ""]:
        cur.execute(f"""
        INSERT INTO measures(measure_name)
        VALUES (\"{i}\")
        """)


def second_stage_create_receipt_table(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS recipes(
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_name TEXT NOT NULL,
    recipe_description TEXT
    )
    """)


def second_stage_fill_receipt_table(cur):
    while True:
        name = input("Recipe name:")
        if name == '':
            break
        description = input("Recipe description:")
        cur.execute(f'''
        INSERT INTO recipes(recipe_name, recipe_description)
        VALUES (\"{name}\", \"{description}\")
        ''')


def main():
    conn = sqlite3.connect("food_blog.db")
    cursor = conn.cursor()
    first_stage_db_creation(cursor)
    conn.commit()
    first_stage_db_fill_up(cursor)
    conn.commit()
    second_stage_create_receipt_table(cursor)
    conn.commit()
    second_stage_fill_receipt_table(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()