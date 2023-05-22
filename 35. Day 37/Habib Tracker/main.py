from datetime import datetime

# Use requests
# import requests
# All tasks done, that's why it is commented out

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "ninjacombo99"
TOKEN = "ds328skj2389ds"
CURRENT_DATE = datetime.now().strftime("%Y%m%d")

pixela_endpoint_json = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Make a user
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_endpoint_json)
# response.raise_for_status()
# print(response.text)
# Done! That's why it is commented out.

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_endpoint_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint_json = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# Make the graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_endpoint_json, headers=graph_endpoint_headers)
# print(response.text)
# Done! That's why commented out

GRAPH_ID = graph_endpoint_json['id']
GRAPH_ID_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

graph_id_endpoint_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_id_endpoint_json = {
    "date": CURRENT_DATE,
    "quantity": "10.5"
}

# Post your progress in the graph
# response = requests.post(url=GRAPH_ID_ENDPOINT, headers=graph_id_endpoint_headers, json=graph_id_endpoint_json)
# print(response.text)
# Done! That's why it is commented out

UPDATE_GRAPH_ID_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{CURRENT_DATE}"

update_graph_id_endpoint_headers = {
    "X-USER-TOKEN": TOKEN
}

update_graph_id_endpoint_json = {
    "quantity": "10"
}

# Update your data
# response = requests.put(url=UPDATE_GRAPH_ID_ENDPOINT, headers=update_graph_id_endpoint_headers,
#                         json=update_graph_id_endpoint_json)
# print(response.text)
# Done! That's why it is commented out

DELETE_GRAPH_ID_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{CURRENT_DATE}"

delete_graph_id_endpoint_headers = {
    "X-USER-TOKEN": TOKEN
}

# Delete the Pixel
# response = requests.delete(url=DELETE_GRAPH_ID_ENDPOINT, headers=delete_graph_id_endpoint_headers)
# print(response.text)
# Done! That's why it is commented out
