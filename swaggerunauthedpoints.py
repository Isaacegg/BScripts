#!/usr/bin/env python3

import json, requests

url = input("please provide the URL of the swagger JSON file: ")

jsondata = requests.get(url).text  
data = json.loads(jsondata)
host = data['host']
scheme = data['schemes'][0]
basepath = data['basePath']
baseurl=f"{scheme}://{host}{basepath}"

for path in data["paths"]:
	method = next(iter(data['paths'][path]))
	rcommand = f"requests.{method}(\"{baseurl}{path}\")"
	if "{id}" in rcommand:
		rcommand = rcommand.replace("{id}","2222")
	r = eval(rcommand)
	status=r.status_code
	if status == 200:
		print(f"{baseurl}{path} IS UNAUTHENTICATED")


