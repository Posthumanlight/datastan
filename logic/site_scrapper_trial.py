from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Setup headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    url = "https://casehug.com/cases/bombix"
    driver.get(url)

    # Wait for the case content to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="case-content-card"]'))
    )

    # Parse the rendered HTML
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all skin cards
    cards = soup.select('[data-testid="case-content-card"]')

    for card in cards:
        chance = card.select_one('[data-testid="case-content-card-grid-item-odds-percentage"]')
        name = card.select_one('[data-testid="case-content-card-grid-item-name"]')
        category = card.select_one('[data-testid="case-content-card-grid-item-category"]')
        price = card.select_one('[data-testid="case-content-card-grid-item-single-price"]')

        print(f"Name: {name.text.strip() if name else 'N/A'}")
        print(f"Skin: {category.text.strip() if category else 'N/A'}")
        print(f"Price: {price.text.strip() if price else 'N/A'}")
        print(f"Chance: {chance.text.strip() if chance else 'N/A'}")
        print("-" * 40)

finally:
    driver.quit()
