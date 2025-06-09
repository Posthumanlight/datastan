from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_info_case(url):
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
    finally:
        driver.quit()
    return cards
