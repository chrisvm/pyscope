import sys 
import os 
import json


# get directory containing this file 
# create config depending on location and user
containing = os.path.split(__file__)[0]
config_file = os.path.join(containing, 'json/conf.json')

def config():
	# parse the config and return 
	try:
		with open(config_file) as f:
			conf = json.loads(f.read())
	except Exception as e:
		print('Error type %s' % type(e))
		print('Error opening config(%s), exiting...' % config_file)
		sys.exit()
	return conf