import requests
import datetime as dt


current_date = ( dt.datetime.now().date())

USERNAME = "aryan1739"
TOKEN = "akjdlfhiuahiuhwe"
pixela_end_point = "https://pixe.la/v1/users"

# user_params = {
#     "token" : TOKEN,
#     "username" : USERNAME,
#     "agreeTermsOfService" : "yes"
#     ,"notMinor" : "yes"
# }

# response = requests.post(url=pixela_end_point , json=user_params)
# print(response.text)
GRAPH_ID = "aryan4234"
graph_params = {
    "id" : GRAPH_ID
    ,"name" : "Daily Study",
    "unit" : "days",
    "type" : "int",
    "color" : "momiji"
}
graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"

# For https Authentication we need header key to make it secure otherwise it will be visible on the search page....
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# graph_response = requests.post(url=graph_end_point, json=graph_params , headers=headers)

# print(graph_response.text)


pixel_header = {
    'X-USER-TOKEN': TOKEN
}

# current_date = current_date.replace("-" ,"")
# The date must be string for this method....
# print(current_date)
# alternate way to format our date:

# The method (strftime("%y%m%d")): The date must not be the string for this method....

current_date = current_date.strftime("%Y%m%d")
pixel_params = {
    "date" : current_date,
    "quantity": input("How many hours did u study today?\n")
}

pixel_end_point = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}"

response3 = requests.post(url = pixel_end_point , json=pixel_params , headers=pixel_header)
print(response3.text)


# Updating the pixel in the graph:

# update_end_point = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"

# update_params = {
#     "quantity": "8"
# }


# Deleting the pixel data in the graph
# response4 = requests.delete(url=update_end_point , headers=pixel_header)

# print(response4.text)


# # updating the graph:
# update_days = { "unit":"hours"
# }
# response5 = requests.put(url=pixel_end_point , json= update_days , headers=pixel_header)

# print(response5.text)


