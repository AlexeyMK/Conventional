from jinja2 import Template
from os import mkdir
import sys
import yaml

yaml_input = yaml.load(open(sys.argv[1]).read())

languages = [ 'python' ]
mkdir(yaml_input['ProjectName'])

for language in languages:
  print "Creating files for " + language
  
  # generating vimrc
  f = open("templates/" + language + ".vimrc.template")
  output = open(yaml_input['ProjectName'] + '/' + language +'.vimrc', 'w')
  output.write(Template("".join(f.readlines())).render(yaml_input))
  output.close()

print "Woot, it worked!"
