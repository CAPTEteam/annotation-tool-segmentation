import os
import json


path = "P2S2/"
example = {}

example["labels"] = ["Background","Vegetation","Organ","Don't know"]
example["models"] = []

dirs = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path,item))]

print(dirs)

for dir_ in dirs:
	if dir_ == "images":

		example["imageURLs"] = ["data/images/"+item for item in os.listdir(os.path.join(path,"images")) if item.endswith(".png")]
	elif dir_ =="annotations":
		example["annotationURLs"] = ["data/annotations/"+item for item in os.listdir(os.path.join(path,"annotations")) if item.endswith(".png")]
	else:
		example["models"].append(dir_)

with open(path+'example.json', 'w') as fp:
    json.dump(example, fp)