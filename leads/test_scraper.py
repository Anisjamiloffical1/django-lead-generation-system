from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("https://www.ycombinator.com/companies")

time.sleep(5)

cards = driver.find_elements(
    By.CSS_SELECTOR,
    'a[href*="/companies/"]'
)

for card in cards:

    try:
        company_name = card.find_element(
            By.CSS_SELECTOR,
            'span[class*="coName"]'
        ).text
    except:
        company_name = "N/A"

    try:
        location = card.find_element(
            By.CSS_SELECTOR,
            'span[class*="coLocation"]'
        ).text
    except:
        location = "N/A"

    try:
        description = card.find_element(
            By.CSS_SELECTOR,
            'div.text-sm span'
        ).text
    except:
        description = "N/A"

    company_url = card.get_attribute("href")

    print("Company:", company_name)
    print("Location:", location)
    print("Description:", description)
    print("URL:", company_url)
    print("-" * 80)

driver.quit()