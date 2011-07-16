from jinja2 import Template
from os import mkdir
import shutil
import sys
import yaml
import json

json_config_file = "config.json"
json_raw_data = open(json_config_file);
json_data = json.load(json_raw_data);
json_raw_data.close()

yaml_input = yaml.load(open(sys.argv[1]).read())
languages = json_data["supported_languages"];
output_dir = yaml_input['ProjectName']
mkdir(output_dir)

for language in (set(languages) & set(yaml_input.keys())):
  print "Creating files for " + language

  #copy necessary files (config file, this file) into output
  for file in [sys.argv[1], "conventional.py"]:
    shutil.copyfile(file, output_dir+"/"+file)

  # generating vimrc
  f = open("templates/" + language + ".vimrc.template")
  output = open(output_dir + '/' + language +'.vimrc', 'w')
  output.write(Template("".join(f.readlines())).render(yaml_input[language]))
  output.close()

  #generating pep8
  shutil.copyfile("pep8.py", output_dir+"/pep8.py")

  #generating git commit hook bindings
  #TODO
print "Woot, it worked!"
