from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

# Setup headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Target URL
url = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y"
driver.get(url)

time.sleep(5)  # Wait for page to load

# Scroll to load more data
for _ in range(3):  # Scroll 3 times; increase if needed
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)

# Parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)
# # Find RFQ cards (the actual class name might need adjustment based on inspection)
# print(soup.text)
rfq_cards = soup.find_all("div", class_="next-row next-row-no-padding brh-rfq-item__container alife-bc-brh-rfq-list__container")
# print(rfq_cards)
rfq_data = []

# for card in rfq_cards:
#     # Title
#     title = card.find("div", class_="brh-rfq-item__subject-link")
#     title = title.get_text(strip=True) if title else "N/A"


#     #  Buyer Name

#     #  Buyer Image

#     link_tag = card.find("a", href=True)
#     rfq_id = "N/A"
#     if link_tag and "requestId=" in link_tag['href']:
#         rfq_id = link_tag['href'].split("requestId=")[-1]
#     # Inquiry Time


#     #  Buyer Name
    

#     # Country

#     # Quantity_Required
#     Quantity_Required=card.find("div", class_="brh-rfq-item__subject-link")
#     Quantity_Required= Quantity_Required.get_text(strip=True) if title else "N/A"

#     # Email Confirmed


#     # Experienced Buyer

#     # Complete Order via RFQ


#     # Typical Replies

#     # Interactive User


#     # Inquiry URL


#     #  Inquiry Date

#     # Scraping Date
#     image_tag = card.find("img", class_="user-img")
#     buyer_image = "https:" + image_tag['src'] if image_tag and image_tag.get('src') else "N/A"

#     rfq_data.append({
#         "Title": title,
#         "RFQ ID": rfq_id,
#         "Buyer Image": buyer_image
#     })

# # # Save to CSV
# # df = pd.DataFrame(rfq_data)
# # df.to_csv("rfq_output.csv", index=False)

# # print("Scraping completed. Data saved to rfq_output.csv")

# # # Clean up
# # driver.quit()






for card in rfq_cards:
    # Title
    title_tag = card.find("a", class_="brh-rfq-item__subject-link")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Buyer Name
    buyer_name_tag = card.find("div", class_="text")
    buyer_name = buyer_name_tag.get_text(strip=True) if buyer_name_tag else "N/A"

    # Buyer Image
    image_tag = card.find("img", class_="user-img")
    buyer_image = "https:" + image_tag['src'] if image_tag and image_tag.get('src') else "N/A"

    # RFQ ID

    # brh-rfq-item__subject-link
    # link_tag = card.find("img", class_="next-col brh-rfq-item__main-info")
    main_info_div = card.find("div", class_="next-col brh-rfq-item__main-info")
    link_tag = main_info_div.find("a", href=True) if main_info_div else None
    link = soup.find("a", class_="brh-rfq-item__subject-link", href=True)
    links_of_product=link['href']
    print(links_of_product)
    
    rfq_id = "N/A"
    inquiry_url = "N/A"
    # if link_tag and "requestId=" in link_tag['href']:
    #     href = link_tag['href']
    #     rfq_id = href.split("requestId=")[-1]
    #     inquiry_url = "https://sourcing.alibaba.com" + href


    # Inquiry Time
    inquiry_time_tag = card.find("div", class_="brh-rfq-item__label")
    inquiry_time = inquiry_time_tag.get_text(strip=True) if inquiry_time_tag else "N/A"

    # Country
    country_tag = card.find("div", class_="brh-rfq-item__country")
    country = country_tag.get_text(strip=True) if country_tag else "N/A"

    # Quantity Required
    quantity_tag = card.find("div", class_="brh-rfq-item__quantity")
    quantity_required = quantity_tag.get_text(strip=True) if quantity_tag else "N/A"

    # Email Confirmed
    email_confirmed = "Yes" if card.find("div", class_="next-tag-body") else "No"

    # Experienced Buyer
    experienced_buyer = "Yes" if card.find("div", class_="next-tag-body") else "No"

    # Complete Order via RFQ
    complete_order = "Yes" if card.find("div", class_="next-tag-body") else "No"

    # Typical Replies
    typical_replies = "Yes" if card.find("div", class_="next-tag-body") else "No"

    # Interactive User
    interactive_user = "Yes" if card.find("div", class_="next-tag-body") else "No"

    # Inquiry Date (convert Inquiry Time to a date if needed or leave as is)
    inquiry_date = "N/A"

    # Scraping Date
    from datetime import datetime
    scraping_date = datetime.now().strftime("%d-%m-%Y")

    rfq_data.append({
        "Title": title,
        "RFQ ID": rfq_id,
        "Buyer Name": buyer_name,
        "Buyer Image": buyer_image,
        "Inquiry Time": inquiry_time,
        "Country": country,
        "Quantity Required": quantity_required,
        "Email Confirmed": email_confirmed,
        "Experienced Buyer": experienced_buyer,
        "Complete Order via RFQ": complete_order,
        "Typical Replies": typical_replies,
        "Interactive User": interactive_user,
        "Inquiry URL": inquiry_url,
        "Inquiry Date": inquiry_date,
        "Scraping Date": scraping_date
    })




# Save to CSV
df = pd.DataFrame(rfq_data)
df.to_csv("rfq_output.csv", index=False)

print("Scraping completed. Data saved to rfq_output.csv")

# Clean up
driver.quit()