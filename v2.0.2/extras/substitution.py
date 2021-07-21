#!/usr/bin/python3

from string import Template
import configparser
from datetime import date

values_dict = {}
today = date.today()

config = configparser.ConfigParser()
config.read('extras/casa_values.ini')
for i in config['DEFAULT']:
    values_dict[i]=config['DEFAULT'][i]

print(values_dict)

with open('extras/cluster-register-template.txt', encoding = 'utf-8') as fh:
    data = fh.readlines()[1:]

template_data = "".join(data)
subs_string = Template(template_data)
parsed=subs_string.safe_substitute(values_dict)

with open('templates/cluster-register.yaml', "w") as fh:
    fh.writelines("# Manifest created on {}\n".format(today))
    fh.writelines("\n")
    fh.writelines(parsed)