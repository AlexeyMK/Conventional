import json
import yaml
from collections import defaultdict

def dictify(d):
	new_d = {}
	for k, v in d.items():
		new_d[str(k)] = dictify(v) if isinstance(v, dict) else str(v)
	return new_d

json_config_file = "config.json"
user_config_file = "user_config.json"

json_raw_data = open(json_config_file);
json_data = json.load(json_raw_data);
json_raw_data.close()

user_file = open(user_config_file, "w")

response = raw_input("Project name? default: ");
if (response == ""):
	response = "default"

dd = lambda: defaultdict(dd)
user_dict = dd()
user_dict["ProjectName"] = response

for convention in json_data["conventions"]:
	print "[" + convention["id"] + "]: " + convention["question"]
	possible_values = "( "
	for possible_value in convention["values"]:
		possible_values += str(possible_value) + " "
	possible_values += ")"
	# Get first response and set the default to that
	default_response = ""
	for language in json_data["supported_languages"]:	
		convention_path = language + "/" + convention["id"]
		while True:
			response = raw_input(possible_values + "[" + language + "] " + default_response + ": ")
			if response in convention["values"]:
				split_path = convention_path.split('/')
				reduce(lambda d, key: d[key], split_path[:-1], user_dict)[split_path[-1]] = response
				default_response = response
				break
			if response == "" and default_response != "":
				split_path = split(language + "/" + convention["id"], "/")
				reduce(lambda d, key: d[key], split_path[:-1], user_dict) [split_path[-1]] = default_response
				break

json.dump(dictify(user_dict), user_file)
