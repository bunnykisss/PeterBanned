# Import the python libraies
import requests

# put post url here 

Post_url = "x"

#Create the payload (Any data you want to send )

data = {
  "content" : "Messege Sent Sussefully"
}

# authorization keys here 
headers = {
  "Authorization" : "auth keys here"
}
# Sent the post request to the webhook
res = requests.post(Post_url, data, headers=headers)

