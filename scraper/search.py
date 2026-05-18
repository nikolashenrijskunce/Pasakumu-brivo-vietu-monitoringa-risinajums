from playwright.sync_api import sync_playwright
import re

def get_all_event_ids():
    with sync_playwright() as p:

        # inicialize headless parluku, un atver bilesu paradizes lapu ar lietotaja agentu, lai apietu bot filter
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36'
            )
        )

        all_ids = []
        past_ids = []
        page_number = 1
        while True:
            page.goto(f'https://www.bilesuparadize.lv/lv/search?page={page_number}')
            print(page_number)
            # pagaida lidz lapa ir ieladejusies un iegust visu pasakumu norises vietu id
            page.wait_for_load_state('networkidle')
            body = page.content()
            location_ids = re.findall(r'href="/lv/event/\d+"',body)

            # apstrada iegutos pasakuma vietu id un parveido to vertibu par integer
            for i in range(len(location_ids)):
                location_ids[i]=location_ids[i].strip('href="/lv/event/')
            location_ids = sorted(set(int(x) for x in location_ids))
            if past_ids == location_ids:
                break
            all_ids.extend(location_ids)
            past_ids = location_ids
            page_number+=1

        browser.close()

    # testesanai izvada iegutos id un to skaitu
    # for x in location_ids:
    #     print(x)
    # print(len(location_ids))

    return all_ids