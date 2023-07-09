import requests


endpoint = "http://127.0.0.1:8000/api/products/"
# http request gives html as response
# rest api http requests give json as response

data = {
    "title" : "this is done"
}
response = requests.post(endpoint, json=data)

print(response.text)