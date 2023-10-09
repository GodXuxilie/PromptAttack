import sqlite3

conn = sqlite3.connect("query_log.db")

cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS my_table
                  (Q TEXT PRIMARY KEY, V TEXT)"""
)


def query(Q):
    cursor.execute("SELECT V FROM my_table WHERE Q=?", (Q,))
    result = cursor.fetchone()
    return result[0] if result else None


def insert(Q, V):
    cursor.execute("INSERT OR REPLACE INTO my_table (Q, V) VALUES (?, ?)", (Q, V))
    conn.commit()


insert("key1", "value1")
insert("key2", "value2")

print(query("key1"))
print(query("key3"))

conn.close()
