# using the requests library to access internet data

#import the requests library
import requests as request

def main():
    # TODO: Use requests to issue a standard HTTP GET request

    url = "http://httpbin.org/xml"

    response = request.head(url) # HEAD

    printResults(response)

    data_values = {
        "key1": "valor1",
        "llave2": "valor2"
    }

    # PUT
    response_de_mi_HTTPput = request.put('https://httpbin.org/put', data = {'key':'mi_valor3'})
    printResults(response_de_mi_HTTPput)

    # POST
    response_de_mi_HTTPpost = request.post('https://httpbin.org/post',headers={"User-Agent":"Adrian Badilla API / 1.5.9"}, params = data_values)
    printResults(response_de_mi_HTTPpost)

    # DELETE
    response_de_mi_HTTPdelete = request.delete('https://httpbin.org/delete')
    printResults(response_de_mi_HTTPdelete)

    # GET
    response_de_mi_HTTPget = request.get('https://httpbin.org/get', params=data_values)
    printResults(response_de_mi_HTTPget)

    # OPTIONS
    response_de_mi_HTTPoptions = request.options('https://httpbin.org/get')
    printResults(response_de_mi_HTTPoptions)
    
    # TODO: Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding


    # TODO: Pass a custom header to the server

    

def printResults(response):
    print("CODE: {0} FROM: {1}".format(response.status_code, response.url))
    print("\n")

    print("Headers: ----------------------")
    print(response.headers)
    print("\n")

    print("Returned data: ----------------------")
    print(response.text, "\n\n")
    print("NEW METHOD CALL ----------------------")


if __name__ == "__main__":
    main()
