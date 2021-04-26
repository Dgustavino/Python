# using urllib to request data

# HTTP METHODS / URL (https:www.google.com/search?) - 
# |REQUEST - RESPONSE| HTTP 200 / 300 / 400 / 500 


#import the urllib request class
import urllib.request

def main():
    # the URL to retrieve our sample data from 
    url = "http://httpbin.org/xml"

    # open the URL and retrieve some data
    response = urllib.request.urlopen("http://google.com")

    # Print the result code from the request, should be 200 OK
    print("Result code: {0}".format(response.status))

    # print the returned data headers
    print("Headers: ----------------------")
    print(response.getheaders())

    # print the returned data itself
    print("Returned data: ----------------------")
    print(response.read().decode("utf-8"))

if __name__ == "__main__":
    main()
