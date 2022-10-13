import requests
data_petstore = {
  "id": 220,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Foxxy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post("https://petstore.swagger.io/v2/pet", json=data_petstore  )
print(response.text)

import requests
data_petstore = {
  "id": 220,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Doggy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put("https://petstore.swagger.io/v2/pet", json=data_petstore  )
print(response.text)

import requests
response = requests.get("https://petstore.swagger.io/v2/pet/220")
print(response.text)