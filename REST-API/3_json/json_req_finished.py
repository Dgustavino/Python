# using the requests library to access internet data

#import the requests library
import requests
import json


def main():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/json"
    response = requests.get(url)

    # Use the built-in JSON function to return parsed data
    data_obj = response.json()
    print(json.dumps(data_obj,indent=4))

    # Access data in the python object
    print(list(data_obj.keys()))

    print(data_obj['slideshow']['author'])
    print("There are {0} slides".format(len(data_obj['slideshow']['slides'])))


if __name__ == "__main__":
    main()
