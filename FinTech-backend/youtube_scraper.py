from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re

# Configure Chrome for headless scraping
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(), options=options)
driver.set_page_load_timeout(30)

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
driver.get(video_url)

# 1. Extract title from <title> tag
title = driver.find_element("tag name", "title").get_attribute("textContent")

# 2. Extract page HTML source
html = driver.page_source

# 3. Regex to find view count
match = re.search(r'([\d.,]+)\s*views', html)
views = match.group(1) + " views" if match else "N/A"

print("📄 Title:", title)
print("👁️  Views:", views)

driver.quit()
