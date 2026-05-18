from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Izveido pprogrammas objektu
app = FastAPI()

# nodefine atrasanas vietu failiem, kas tiek pielietoti frontendaa
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# TODO: DELETE Fake data for now
events = [
    {
        "id": 1,
        "name": "Rock Concert",
        "date": "2026-07-21 19:30:00",
        "city": "Riga",
        "availability": 120,
        "price": 45
    },
    {
        "id": 2,
        "name": "Jazz Festival",
        "date": "2026-08-06 18:00:00",
        "city": "Tallinn",
        "availability": 35,
        "price": 60
    },
    {
        "id": 3,
        "name": "Tech Conference",
        "date": "2026-11-13 09:00:00",
        "city": "Vilnius",
        "availability": 200,
        "price": 120
    },
    {
        "id": 4,
        "name": "Food Truck Expo",
        "date": "2026-05-18 12:00:00",
        "city": "Kaunas",
        "availability": 80,
        "price": 25
    },
    {
        "id": 5,
        "name": "Indie Film Night",
        "date": "2026-09-02 20:15:00",
        "city": "Tartu",
        "availability": 50,
        "price": 18
    },
    {
        "id": 6,
        "name": "Startup Meetup",
        "date": "2026-10-27 17:45:00",
        "city": "Riga",
        "availability": 150,
        "price": 75
    },
    {
        "id": 7,
        "name": "Classical Music Gala",
        "date": "2026-12-14 19:00:00",
        "city": "Vilnius",
        "availability": 90,
        "price": 95
    },
    {
        "id": 8,
        "name": "Gaming Championship",
        "date": "2026-06-09 10:30:00",
        "city": "Tallinn",
        "availability": 300,
        "price": 40
    },
    {
        "id": 9,
        "name": "Art & Design Fair",
        "date": "2026-08-30 14:00:00",
        "city": "Liepaja",
        "availability": 65,
        "price": 22
    },
    {
        "id": 10,
        "name": "Winter Beer Festival",
        "date": "2027-01-11 16:00:00",
        "city": "Jurmala",
        "availability": 140,
        "price": 35
    },
    {
        "id": 11,
        "name": "Marathon Weekend",
        "date": "2026-04-25 07:00:00",
        "city": "Kaunas",
        "availability": 500,
        "price": 15
    },
    {
        "id": 12,
        "name": "Electronic Dance Night",
        "date": "2026-07-19 22:00:00",
        "city": "Riga",
        "availability": 220,
        "price": 55
    },
    {
        "id": 13,
        "name": "Photography Workshop",
        "date": "2027-03-07 11:00:00",
        "city": "Tallinn",
        "availability": 28,
        "price": 85
    },
    {
        "id": 14,
        "name": "Book Lovers Convention",
        "date": "2026-10-16 13:30:00",
        "city": "Vilnius",
        "availability": 110,
        "price": 20
    },
    {
        "id": 15,
        "name": "Summer Beach Party",
        "date": "2026-08-01 21:00:00",
        "city": "Jurmala",
        "availability": 400,
        "price": 30
    }
]


@app.get("/")
def home(request: Request):

    # dod index.html failu un sarakstu ar visiem notikumiem un to informacija
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"events": events}
    )


@app.get("/event/{event_id}")
def event_details(request: Request, event_id: int):

    # atrod informaciju par to event, kam atbilst doatis event_id
    event = next(
        (e for e in events if e["id"] == event_id),
        None
    )

    return templates.TemplateResponse(
        request=request,
        name="event.html",
        context={
            "event": event
        }
    )



# cd backend; uvicorn main:app --reload