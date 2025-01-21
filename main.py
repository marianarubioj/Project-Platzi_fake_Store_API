import requests

import data

response = requests.get(data.url)
response_body = response.content

print(response)
print(response_body)

