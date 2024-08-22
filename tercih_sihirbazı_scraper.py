import time
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re

load_dotenv()

hostname = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
pwd = os.getenv('DB_PWD')
port_id = os.getenv('DB_PORT')

db_url = f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}'

engine = create_engine(db_url)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

puan_turu = "dil"

url = f"https://yokatlas.yok.gov.tr/tercih-sihirbazi-t4-tablo.php?p={puan_turu}"
driver.get(url)

table_xpath = '//*[@id="mydata"]'

pagination_xpath = '//*[@id="mydata_paginate"]/ul'
pagination_element = driver.find_element(By.XPATH, pagination_xpath)


page_numbers = pagination_element.find_elements(By.TAG_NAME, 'a')
total_pages = int(page_numbers[-2].text)


for page in range(1, total_pages + 1):
    time.sleep(5)

    table = driver.find_element(By.XPATH, table_xpath)
    rows = table.find_elements(By.XPATH, ".//tbody/tr")

    program_data = []
    year_data = []

    years = ["2024", "2023", "2022", "2021"]

    for row in rows:
        cols = row.find_elements(By.XPATH, ".//td")

        row_data = []
        for col in cols:
            cell_html = col.get_attribute('innerHTML').strip()
            soup = BeautifulSoup(cell_html, "html.parser")
            cell_text = soup.get_text(separator="\n").strip()

            cell_text = re.sub(r'\s*\n\s*', '\n', cell_text)
            cell_text = re.sub(r'\s*\t\s*', ' ', cell_text)
            cell_text = re.sub(r'\xa0', ' ', cell_text)
            cell_text = re.sub(r' {2,}', ' ', cell_text)

            cell_text = cell_text.strip()
            row_data.append(cell_text)

        print(row_data)
        universite_fakulte_raw = row_data[2].split('\n')
        universite = universite_fakulte_raw[0].strip()
        fakulte = universite_fakulte_raw[1].strip() if len(universite_fakulte_raw) > 1 else ""

        program_adi_raw = row_data[3].split('\n')
        program_adi = program_adi_raw[0].strip()

        program_info = {
            "yop_kodu": row_data[1].split('\n')[0].strip(),
            "universite": universite,
            "fakulte": fakulte,
            "program_adi": program_adi,
            "sehir": row_data[4].strip(),
            "universite_turu": row_data[5].strip(),
            "ucret_burs": row_data[6].strip(),
            "puan_turu": puan_turu,
            "ogretim_turu": row_data[7].strip()
        }

        program_data.append(program_info)

        kontenjanlar = row_data[8].split('\n')
        yerlesenler = row_data[10].split('\n')
        tbsler = row_data[11].split('\n')
        taban_puanlar = []

        for p in row_data[12].split('\n'):
            try:
                taban_puanlar.append(float(p.replace(',', '.')))
            except ValueError:
                taban_puanlar.append(None)

        for i in range(len(years)):
            year_info = {
                "yop_kodu": row_data[1].split('\n')[0].strip(),
                "yil": years[i],
                "kontenjan": kontenjanlar[i].strip() if i < len(kontenjanlar) else None,
                "yerlesen": yerlesenler[i].strip() if i < len(yerlesenler) else None,
                "tbs": tbsler[i].strip() if i < len(tbsler) else None,
                "taban_puan": taban_puanlar[i] if i < len(taban_puanlar) else None,
                "doluluk_statu": row_data[9].strip() if len(row_data) > 9 else None
            }
            year_data.append(year_info)

    program_columns = ["yop_kodu", "universite", "fakulte", "program_adi", "sehir", "universite_turu", "ucret_burs", "puan_turu", "ogretim_turu"]
    program_df = pd.DataFrame(program_data, columns=program_columns)

    year_columns = ["yop_kodu", "yil", "kontenjan", "yerlesen", "tbs", "taban_puan", "doluluk_statu"]
    year_df = pd.DataFrame(year_data, columns=year_columns)

    program_df.to_sql('tercih_sihirbazi_programs', engine, if_exists='append', index=False)
    year_df.to_sql('tercih_sihirbazi_years', engine, if_exists='append', index=False)
    print(f"{page} sayfası db'ye yüklendi.")
    if page < total_pages:
        next_button_xpath = '//*[@id="mydata_paginate"]/ul/li[@class="paginate_button next"]/a'
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        next_button.click()
        print("Diğer sayfaya geçildi")
        time.sleep(2)

driver.quit()
