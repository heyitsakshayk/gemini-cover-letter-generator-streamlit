from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from splitter import text_to_doc_splitter

def extract_text_from_url(url):
    # Check if URL is valid
    if not url.startswith("http"):
        print("Invalid URL format. Please include 'http://' or 'https://'")
        return None

    # Setup Chrome options for headless mode and add a user-agent
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Wait for the content to load by waiting for an element that contains the description
    try:
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, "description__text"))
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        return None

    # Extract the HTML source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract the desired content
    text = []
    for lines in soup.find_all('div', {'class': 'description__text'}):
        text.append(lines.get_text(strip=True))
    
    # Clean up the extracted text
    text_content = '\n'.join(text)
    print("Extracted Text:\n", text_content)

    
    # Process the text as needed (assuming you have a text processing function)
    document = text_to_doc_splitter(text_content)
    
    driver.quit()  # Quit the driver to free resources
    return text_content  # Replace with 'document' if further processing is needed