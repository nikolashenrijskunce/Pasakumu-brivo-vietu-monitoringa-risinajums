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
    date DATE,
    sales_start DATE,
    sales_end DATE,
    description VARCHAR(10000),
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
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

""")

# ievada informaciju tabula
cur.execute("""
INSERT INTO venues (id, name, address, longitude, latitude) VALUES (%s, %s, %s, %s, %s)""", (249,'BTA Daugavas Stadions','Rīga, Augšiela 1', 56.953675, 24.157391)
)

# izpilda izmainas
conn.commit()

# izvada visas rindas
cur.execute("""
SELECT * FROM venues;
""")

rows = cur.fetchall()

for row in rows:
    print(row)

# beidz savienojumu
cur.close()
conn.close()