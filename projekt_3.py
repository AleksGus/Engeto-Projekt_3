"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Aleksei Gusev
email: aleksgus@seznam.cz
discord: alexvonhus
"""

import requests
import csv
from bs4 import BeautifulSoup as BP
import sys

def get_info(district_url, main_code):
    """
Funkce pro získání informací o výsledcích hlasování v obci na základě URL a kódu obce.
"""
    try:
        # Získání HTML stránky z URL
        electweb = requests.get("https://volby.cz/pls/ps2017nss/" + district_url)
        # Inicializace parseru BeautifulSoup
        html_parser = BP(electweb.text, "html.parser")
        el_data = [main_code]  # Inicializace seznamu pro data
    except requests.exceptions.ConnectionError as e:
        sys.exit(f"Problem with connection: {e}")

    for i in html_parser.find_all("h3"):
        if "Obec" in i.text:
            # Získání názvu obce a přidání ho do seznamu
            el_data.append(i.text.split(":")[-1].strip())
            break
    # Získání dalších údajů o hlasování a jejich přidání do seznamu
    el_data.append(html_parser.find("td", attrs={"headers": "sa2"}).text.replace("\xa0", ""))
    el_data.append(html_parser.find("td", attrs={"headers": "sa3"}).text.replace("\xa0", ""))
    el_data.append(html_parser.find("td", attrs={"headers": "sa6"}).text.replace("\xa0", ""))
    for x in html_parser.find_all("td", attrs={"headers": "t1sa2 t1sb3"}):
        el_data.append(x.text.replace("\xa0", " "))
    for x in html_parser.find_all("td", attrs={"headers": "t2sa2 t2sb3", "class": "number"}):
        el_data.append(x.text.replace("\xa0", " "))
    return el_data

# Funkce pro zápis dat do CSV souboru.
def write_csv(header, el_data, filename):
    with open(filename + ".csv", "w", newline="\n", encoding="utf-8") as f:
        entry = csv.writer(f)
        entry.writerow(header)  # Zápis hlavičky
        entry.writerows(el_data)  # Zápis dat

# Funkce pro načtení HTML stránky ze zadaného URL.
def source(url):
    source = requests.get(url)
    soup = BP(source.text, "html.parser")
    return soup

# Funkce pro získání hlavičky s informacemi o hlasování v okrese.
def header(district_url):
    electweb = requests.get("https://volby.cz/pls/ps2017nss/" + district_url)
    html_parser = BP(electweb.text, 'html.parser')
    district_data = ["code", "Location", "registered voters", "envelopes", "valid"]
    for x in html_parser.find_all("td", attrs={"headers": "t1sa1 t1sb2"}):
        district_data.append(x.text)
    for x in html_parser.find_all("td", attrs={"headers": "t2sa1 t2sb2", "class": ""}):
        district_data.append(x.text)
    return district_data

# Funkce pro získání výsledků hlasování v obcích.
def el_data(source):
    el_data = [get_info(x.find("a")["href"], x.text) for x in source.find_all("td", attrs={"class": "cislo"})]
    district_data = header(source.find("td", attrs={"class": "cislo"}).find("a")["href"])
    return (district_data, el_data)

# Funkce pro kontrolu URL odkazu na výběr okresu.
def checkurl(url):
    if "https://volby.cz/pls/ps2017nss/ps32" not in url:
        print("No reference to district selection page, please try again")
        return False
    else:
        return True

# Hlavní blok kódu pro spuštění skriptu.
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Scrap data from given URL and save it to a CSV file.")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    if not checkurl(url):
        sys.exit(1)

    print("Processing ...")
    header_data, el_data = el_data(source(url))
    write_csv(header_data, el_data, output_file)
    print(f"Done. The output is in file {output_file}.csv.")
