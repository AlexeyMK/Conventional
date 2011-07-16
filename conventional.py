from jinja2 import Template
from os import mkdir
import shutil
import sys
import json

def get_rule(rule_path):
  convention_json = json.load(open("user_config.json"))
  lookup_path = rule_path.split("/") 
  try:
    #TODO: better code than random try/catch here
    return reduce(lambda d, key: d[key], lookup_path, convention_json)
  except:
    return False

def main():
  question_config_file = "questions.json"
  convention_json = json.load(open(sys.argv[1]))
  languages = json.load(open(question_config_file))["supported_languages"];
  output_dir = convention_json['ProjectName']
  #TODO: check if exists, delete or warn if so
  mkdir(output_dir)

  for language in (set(languages) & set(convention_json.keys())):
    print "Creating files for " + language

    #copy necessary files (config file, this file) into output
    for file in [sys.argv[1], "conventional.py"]:
      shutil.copyfile(file, output_dir+"/"+file)

    # generating vimrc
    f = open("templates/" + language + ".vimrc.template")
    output = open(output_dir + '/' + language +'.vimrc', 'w')
    output.write(Template("".join(f.readlines())).render(convention_json[language]))
    output.close()

    #generating pep8
    shutil.copyfile("pep8.py", output_dir+"/pep8.py")

    #generating git commit hook bindings
    #TODO
  print "Woot, it worked!"

if __name__ == "__main__":
  main()
