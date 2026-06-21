from playwright.sync_api import sync_playwright
from time import sleep
from datetime import datetime

print("Starting the Playwright script...")
print(f"script started at: {datetime.now()}")

 #Cricinfo URL bot
 #chromium -> Cricbuzz -> latest score of the match -> screenshot of the score -> save the screenshot -> final text file

with sync_playwright() as p:
    print("Launching the browser...")
    browser = p.chromium.launch(headless=False)
    print("Browser launched successfully.")
    
    print("Opening a new page...")
    page = browser.new_page()
    print("Page opened successfully.")
    
    print("Navigating to Cricbuzz...")
    page.goto("https://www.cricbuzz.com/")
    print("Navigation successful.")
    
    sleep(5)  # Wait for the page to load completely
    
    print("Locating the latest match score...")
    score_element = page.query_selector(".cb-ovr-flo.cb-hmscg.cb-ovr-flo-hm")
    
    if score_element:
        score_text = score_element.inner_text()
        print(f"Latest match score: {score_text}")
        
        # Save the score to a text file
        with open("latest_score.txt", "w") as file:
            file.write(score_text)
        print("Score saved to latest_score.txt")
        
        # Take a screenshot of the score element
        score_element.screenshot(path="latest_score.png")
        print("Screenshot saved as latest_score.png")
    else:
        print("Could not locate the latest match score.")
    
    print("Closing the browser...")
    browser.close()
    print(f"Script completed at: {datetime.now()}")