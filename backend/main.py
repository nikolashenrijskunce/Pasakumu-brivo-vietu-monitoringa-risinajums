from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="templates")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Fake data for now
events = [
    {
        "id": 1,
        "name": "Rock Concert",
        "city": "Riga",
        "availability": 120,
        "price": 45
    },
    {
        "id": 2,
        "name": "Jazz Festival",
        "city": "Tallinn",
        "availability": 35,
        "price": 60
    },
    {
        "id": 3,
        "name": "Tech Conference",
        "city": "Vilnius",
        "availability": 200,
        "price": 120
    }
]


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "events": events
        }
    )


@app.get("/event/{event_id}")
def event_details(request: Request, event_id: int):

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