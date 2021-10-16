import requests
# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://localhost:5000/api"
IMAGE_PATH = "00dfcb22-950d-49be-a781-3551b63d8b76.png"
# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}
# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()
# ensure the request was sucessful
if r["success"]:    
    print(r)
# otherwise, the request failed
else:
	print("Request failed")