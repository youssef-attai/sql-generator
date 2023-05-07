import json
import requests
from bs4 import BeautifulSoup

BASE_URL = f"http://random-name-generator.info"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_names(which):
    base = f"{BASE_URL}/{which}"

    names = []

    for letter in ALPHABET:
        url = f"{base}/{letter}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        for nameList in soup.find_all('ul', class_='nameList'):
            name_list = nameList.find_all('li')
            for name in name_list:
                cleaned_name = name.text.replace(" ", "").replace("\n", "").replace("\t", "")
                names.append(cleaned_name)

    json_names = {"names": names}
    with open(f"{which}.json", "w") as f:
        f.write(json.dumps(json_names))

    return names

def get_male_names():
    return get_names("male-names")

def get_female_names():
    return get_names("female-names")

def get_last_names():
    return get_names("last-names")

