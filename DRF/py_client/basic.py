import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
# http request gives html as response
# rest api http requests give json as response


response = requests.get(endpoint, params={"abc":123}, json={"product_id": "123"})
print(response.text)