from json import load
from yaml import dump
from sys import argv

def getInputAndOutputFiles():
	if len(argv) ==1:
		jsonPath = input("please enter the path to your JSON file: ")
		yamlPath = input("please enter the path to your YAML file: ")
	elif len(argv) == 2:
		jsonPath = argv[1]
		yamlPath = input("please enter the path to your YAML file: ")
	elif len(argv) >= 3:
		jsonPath = argv[1]
		yamlPath = argv[2]
	return jsonPath,yamlPath

def getJSONValueFromFile(jsonPath):
	with open(jsonPath, "r") as jsonFile:
		return load(jsonFile)


jsonPath,yamlPath = getInputAndOutputFiles()
print("started to convert your file...")
jsonValue = getJSONValueFromFile(jsonPath)

yamlFile = open(yamlPath, "w")
dump(jsonValue, yamlFile)
yamlFile.close()

print(f"done, your file is now on {yamlPath}")
