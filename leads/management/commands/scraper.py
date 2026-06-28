from django.core.management.base import BaseCommand
from leads.models import Lead
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
from django.http import HttpResponse



class Command(BaseCommand):
    help = 'Scrape leads from a website and save them to the database'

    def handle(self, *args, **kwargs):
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

            # Create a Lead object and save it to the database
            lead = Lead(
                company_name=company_name,
                website=company_url,
                description=description,
                email="N/A",  # Email scraping not implemented
                phone="N/A",  # Phone scraping not implemented
                location=location
            )
            lead.save()
        
            
        
        

        # Then create Lead objects and save them to the database
        self.stdout.write(self.style.SUCCESS('Successfully scraped leads'))