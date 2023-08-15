"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Aleksei Gusev
email: aleksgus@seznam.cz
discord: alexvonhus
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import argparse


def main_page(url: str, output_file: str) -> None:
    """
    The main function that performs the whole process of extracting data from the specified URL
    and saving it to a CSV file.
    """
    def load_page(page_url: str) -> BeautifulSoup:
        """
        Loads the page using the GET request and converts it to the BeautifulSoup object.
        """
        r = requests.get(page_url).text
        return BeautifulSoup(r, html_parser)

    def get_rows_with_values(web_page_soup: BeautifulSoup) -> list:
        """
        Retrieves rows with values from a page using BeautifulSoup.
        """
        rows_list = []
        rows = web_page_soup.find_all("tr")

    # Konstanty
    html_parser = "lxml"
    url = "https://volby.cz/pls/ps2017nss/"
    headers_pattern = re.compile(r".*sa2.*sb3")

    # Definování CSV
    district_data = []
    code_column = "Code"
    name_column = "Location"
    registered_column = "Registered"
    envelopes_column = "Envelopes"
    valid_column = "Valid"

    # [ ZÍSKÁNÍ DAT ]
    print("Loading data...")
    district_page = load_page(url)
    municipalities_table = get_rows_with_values(district_page)

    # Sledování průběhu
    total_municipalities = len(municipalities_table)
    completed_municipalities = 0

    # Získání dat z každé obce
    for municipality in municipalities_table:
        municipality_data = {}

        # Získání kódu a názvu
        municipality_data[code_column] = municipality.find("td", class_="cislo").text
        municipality_data[name_column] = municipality.find("td", class_="overflow_name").text

        # Získání dat o hlasování
        link = url + municipality.find("a")["href"]
        municipality_page = load_page(link)

        municipality_data[registered_column] = municipality_page.find("td", headers="sa2").text
        municipality_data[envelopes_column] = municipality_page.find("td", headers="sa5").text
        municipality_data[valid_column] = municipality_page.find("td", headers="sa6").text

        # Získat data pro každého kandidáta
        votes_table = get_rows_with_values(municipality_page)
        for political_party in votes_table:
            party_name_column = political_party.find("td", class_="overflow_name").text
            valid_votes_number = political_party.find("td", headers=headers_pattern).text.replace("\xa0", "")
            municipality_data[party_name_column] = valid_votes_number

        district_data.append(municipality_data)

        # Vypočítat procent pokroku
        completed_municipalities += 1
        percentage_completion = (completed_municipalities / total_municipalities) * 100
        print(f"{percentage_completion:.2f}%")

    # [ ULOŽENÍ ZÍSKANÝCH DAT DO CSV ]
    data_frame = pd.DataFrame(district_data)
    data_frame.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Data saved to {output_file}")


if __name__ == "_main_page_":
    while True:
        try:
            # Přidání argumentů
            parser = argparse.ArgumentParser(description="Scrap data from given URL and save it to a CSV file.")
            parser.add_argument('url', type=str, help="URL to scrap data from")
            parser.add_argument('output_file', type=str, help="Output CSV file name")

            args = parser.parse_args()

            # Zkontroluje, zda zadané URL začíná očekávanou základní URL
            if not args.url.startswith("https://volby.cz/pls/ps2017nss/"):
                raise ValueError("URL must start with 'https://volby.cz/pls/ps2017nss/'")

            main_page(args.url, args.output_file)
            break

        # Pokud dojde k chybě v bloku try, spustí se tento blok except
        except Exception as e:
            print(f"ERROR: {e}")
            print("Please, try again...")
