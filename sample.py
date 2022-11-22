import requests
import json


def main():
    url = 'https://vjevn1.deta.dev'
    data = {
        'x': 10,
        'y': 15
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == '__main__':
    main()
