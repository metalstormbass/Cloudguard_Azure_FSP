import requests

#remove https warning
requests.packages.urllib3.disable_warnings()

def post(target, user_input):

   response = requests.post(target, data=data,verify=False)
   print (response.content)

#Input target
target = input("Target: ")
selection = input("Select 1 for Bening Input and 2 for Malicious Input: ")
if selection == "1":
     data = "{\n  \"name\": \"Cloudguard Workload\"\n}"
if selection == "2" :
     data = { "name" : "<script>alert('This is malicious input')</script>" }

post(target, data)
