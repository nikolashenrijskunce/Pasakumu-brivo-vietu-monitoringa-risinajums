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