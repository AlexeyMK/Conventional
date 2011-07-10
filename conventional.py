from jinja2 import Template
from os import mkdir
yaml_input = {"project_name":"example", "indentation_style": "spaces", "num_spaces":"4"}

f = open("python_templates/python.vimrc.template")

mkdir(yaml_input['project_name'])
output = open(yaml_input['project_name'] + '/python.vimrc', 'w')
output.write(Template("".join(f.readlines())).render(yaml_input))
output.close()
print "Woot, it worked!"

