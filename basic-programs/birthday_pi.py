from requests import get
from os.path import exists


def check():
    bday = input("Enter you birthday (DDMMYY): ")
    with open('one_million_pi.txt') as f:
        lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    if bday in pi_string:
        print("Your birthday appears in first million digits of pi value!")
    else:
        print("Your birthday does not appear in first million digits of pi value.")


if exists('./one_million_pi.txt'):
    check()
else:
    print("Downloading one_million_pi.txt")
    res = get(
        "https://raw.githubusercontent.com/aayush2718/awesome-python/main/basic-programs/one_million_pi.txt")
    with open('./one_million_pi.txt', 'w') as f:
        f.write(res.text)
    check()
