# import the library for calling the api
import requests
import json

# specify the url/endpoint
endpoint = "http://api.coincap.io/v2/assets"

# header
# authorization -> api key/token
# content-type -> application/json
# accept -> application/json
# accept-encoding -> gzip, deflate
header = {}

# payload
# POST PUT DELETE operations in APIs
# CRUD -> Create Read Update Delete
# POST -> create
# PUT -> update
# DELETE -> delete
# GET -> read
payload = {}

# you have to actually call the api
response = requests.get(endpoint, headers=header, data=payload)
jsonData = response.json()
print(json.dumps(jsonData, indent=4))

# response -> json
# javascript object notation
# json -> python dictionary


# parse the json response


# print it out