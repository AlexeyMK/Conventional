from jinja2 import Template
from os import mkdir
import sys
import yaml
import json


json_config_file = "config.json"
json_raw_data = open(json_config_file);
json_data = json.load(json_raw_data);
json_raw_data.close()

yaml_input = yaml.load(open(sys.argv[1]).read())

languages = json_data["supported_languages"];

mkdir(yaml_input['ProjectName'])

for language in languages:
	if not (language in yaml_input):
		continue
  print "Creating files for " + language
  # generating vimrc
  f = open("templates/" + language + ".vimrc.template")
  output = open(yaml_input['ProjectName'] + '/' + language +'.vimrc', 'w')
  output.write(Template("".join(f.readlines())).render(yaml_input[language]))
  output.close()

print "Woot, it worked!"
