import requests
from datetime import datetime

USERNAME = "mikebike"
TOKEN = "206480220aB"
GRAPH_ID = "testgraph1"

pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{graph_value_endpoint}/{20220519}"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
graph_params = {
    "id" : GRAPH_ID,
    "name" : "Coding-graph",
    "unit" : "hrs",
    "type" : "int",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

today = datetime.now()

graph_value_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you code today? ")
}

update_params = {
    "quantity" : "10"
}

#To create the pixela user account
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
#To create the graph were using to track
response2 = requests.post(url=graphs_endpoint, json=graph_params, headers=headers)
print(response2.text)
#To post the value to the graph
response3 = requests.post(url=graph_value_endpoint, json=graph_value_params, headers=headers)
print(response3.text)



