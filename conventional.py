from jinja2 import Template
from os import mkdir
import sys
import yaml

yaml_input = yaml.load(open(sys.argv[1]).read())

print yaml_input

f = open("python_templates/python.vimrc.template")

mkdir(yaml_input['project_name'])
output = open(yaml_input['project_name'] + '/python.vimrc', 'w')
output.write(Template("".join(f.readlines())).render(yaml_input))
output.close()
print "Woot, it worked!"
