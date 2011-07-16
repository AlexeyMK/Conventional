from jinja2 import Template
from os import mkdir
import sys
import yaml
import json


global_config_file = "config.json"
user_config_file = "user_config.json"

json_data = json.load(open(global_config_data)
languages = json_data["supported_languages"]

user_input = json.load(open(sys.argv[1]))

mkdir(user_input['ProjectName'])

for language in languages:
	if not (language in user_input):
		continue
  print "Creating files for " + language
  # generating vimrc
  f = open("templates/" + language + ".vimrc.template")
  output = open(user_input['ProjectName'] + '/' + language +'.vimrc', 'w')
  output.write(Template("".join(f.readlines())).render(user_input[language]))
  output.close()

print "Woot, it worked!"
