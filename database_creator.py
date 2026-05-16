import psycopg2

# izveido savienojumu ar datubazi
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='jojosiwa',
)
cur = conn.cursor()



# izpilda komandas, kas izveido tabulas
cur.execute("""
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(200),
    longitude FLOAT,
    latitude FLOAT
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    title VARCHAR(300),
    date TIMESTAMP,
    sales_start TIMESTAMP,
    sales_end TIMESTAMP,
    description TEXT,
    language VARCHAR(50),
    venue_id INTEGER,
    FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    event_id INTEGER,
    category TEXT,
    price NUMERIC,
    count INTEGER,
    checked_on TIMESTAMP DEFAULT NOW(),
    UNIQUE(event_id, price),
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);
""")



# izpilda izmainas
conn.commit()

# beidz savienojumu
cur.close()
conn.close()