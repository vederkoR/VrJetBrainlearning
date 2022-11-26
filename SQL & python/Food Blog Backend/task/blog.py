import sqlite3


def main():
    conn = sqlite3.connect("food_blog.db")
    cur = conn.cursor()
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
    conn.commit()

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
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
