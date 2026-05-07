from playwright.sync_api import sync_playwright
import re

def get_all_event_ids():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        # browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.bilesuparadize.lv/lv/search?keywords=")
        page.wait_for_load_state("networkidle")

        body = page.content()

        event_ids = re.findall(
            r',"\d{6}",',
            body
        )

        browser.close()

    for i in range(len(event_ids)):
        event_ids[i]=event_ids[i].strip('",')
    event_ids = sorted(set(int(x) for x in event_ids))

    for b in event_ids:
        print(b)
    print(len(event_ids))

    ##print(event_ids)
    return event_ids
