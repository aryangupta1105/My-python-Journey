import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

# Raising exception for invalid codes...
response.raise_for_status()

# Converting to json format:

data = response.json()
print(data)
print()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude , latitude)
print(iss_position)






