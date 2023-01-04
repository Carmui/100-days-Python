import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "carmui159"
TOKEN = "ABEWG8777FDEEE90213"
GRAPH_ID = "graph123145"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POINT_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
TODAY_DATE = datetime.now().strftime("%Y%m%d")
DAILY_QUANT = "65"

## Change today_date parameter to delete checkpoint from another date
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY_DATE}"

### Creating user
user_params = {
    ## TOKEN FREE TO USE
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## Uncoment to create your user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

### Creating graphs
graph_params = {
    ## TOKEN FREE TO USE
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

## Uncoment to create new graph
# response_2 = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response_2.text)


### Creating points
point_params = {
    "date": TODAY_DATE,
    "quantity": DAILY_QUANT
}

## Uncoment to add new checkpoint
# response_3 = requests.post(url=POINT_ENDPOINT, json=point_params, headers=headers)
# print(response_3.text)

### Deleting points
response_4 = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response_4.text)
