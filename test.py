import psycopg2

try:
    conn = psycopg2.connect(
        dbname='driftwooddb',
        user='driftwooddb',
        password='driftwooddb',
        host='localhost',
        port='5432'
    )
    print("✅ Подключение к PostgreSQL успешно!")
    
    # Проверим кодировку
    cur = conn.cursor()
    cur.execute("SHOW server_encoding;")
    encoding = cur.fetchone()[0]
    print(f"✅ Кодировка сервера: {encoding}")
    
    conn.close()
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")