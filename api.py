import requests


def main():
    response = requests.get("https://api.artic.edu/api/v1/artowrks/search")
    print(response)


main()