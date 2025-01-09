"""
curl -X 'POST' \
  'http://5.63.153.31:5051/v1/account' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "login": "string",
  "email": "string",
  "password": "string"
}'
"""

import requests
import pprint


# url = 'http://5.63.153.31:5051/v1/account'
# headers = {
#     'accept': '*/*',
#     'Content-Type': 'application/json'
# }
# json = {
#     "login": "linara",
#     "email": "linara@mail.ru",
#     "password": "linara"
# }
# response = requests.post(
#     url=url,
#     headers=headers,
#     json=json
# )

url = 'http://5.63.153.31:5051/v1/account/1e1d9914-80b7-4e59-b2cc-fe6bdcb1bf2e'
headers = {
     'accept': 'text/plain'
}
response = requests.put(
    url=url,
    headers=headers
)

print(response.status_code)
pprint.pprint(response.json())