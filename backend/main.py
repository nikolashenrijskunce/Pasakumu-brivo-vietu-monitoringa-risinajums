from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import psycopg2
from psycopg2.extras import RealDictCursor
from database import get_connection

# Izveido pprogrammas objektu
app = FastAPI()

# nodefine atrasanas vietu failiem, kas tiek pielietoti frontendaa
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
def home(request: Request):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
    SELECT
    e.id AS id,
    e.title AS name,
    e.date AS date,
    v.address AS address,
    SUM(t.count) AS availability,
    MIN(t.price) AS min_price,
    MAX(t.price) AS max_price

    FROM events e
    JOIN venues v ON v.id = e.venue_id
    JOIN tickets t ON t.event_id = e.id
    
    GROUP BY e.id, e.title, e.date, v.address
    ORDER BY e.date;""")

    events = cur.fetchall()
    cur.close()
    conn.close()

    # dod index.html failu un sarakstu ar visiem notikumiem un to informacija
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"events": events}
    )


@app.get("/event/{event_id}")
def event_details(request: Request, event_id: int):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
                SELECT e.id,
                       e.title,
                       e.description,
                       e.date,
                       e.sales_start,
                       e.sales_end,
                       e.language,

                       v.name AS venue_name,
                       v.address,
                       v.latitude,
                       v.longitude

                FROM events e
                         JOIN venues v ON v.id = e.venue_id

                WHERE e.id = %s
                """, (event_id,))

    event = cur.fetchone()

    cur.execute("""
                SELECT category,
                       price,
                       count,
                       checked_on

                FROM tickets

                WHERE event_id = %s

                ORDER BY price
                """, (event_id,))

    tickets = cur.fetchall()

    cur.close()
    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="event.html",
        context={
            "event": event,
            "tickets": tickets
        }
    )



# cd backend; uvicorn main:app --reload