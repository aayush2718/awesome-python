# NOT WORKING ATM

from requests import get
from bs4 import BeautifulSoup
from os.path import exists


def check():
    bday = input("Enter you birthday (DDMMYY): ")
    f = open('one_million_pi.txt')
    if bday in f:
        print("Your birthday appears in first million digits of pi value!")
    else:
        print("Your birthday does not appear in first million digits of pi value.")
    f.close()


if exists('one_million_pi.txt'):
    check()
else:
    res = get("https://www.piday.org/million")
    soup = BeautifulSoup(res.text, 'html.parser')
    million_pi = soup.find(id="million_pi").text
    with open('one_million_pi.txt', 'w') as f:
        f.write(million_pi)
