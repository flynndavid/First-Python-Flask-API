import requests

#Define the URL
baseURL = "http://localhost:5000/api/v1/"

# "user" to get user info. 
# "help" to learn more. 
# "ping" to get status
resource = "ping"

# set URL
url = baseURL + resource

# select the version of the API that you wish to run.
#   0 - Run with no params
#   1 - Valid Parameter & Name
#   2 - Pass Invalid Parameter, Valid Name
#   3 - Valid Parameter, Name doesn't exist
v = 0

def getparams(x):
    if x == 0:
        param = None
        return param
    if x == 1:
        param = {"name":"David"}
        return param
    if x == 2:
        param = {"user":"David"}
        return param
    if x == 3:
        param = {"name":"Savannah"}
        return param
    return None
    
params = getparams(v)

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

