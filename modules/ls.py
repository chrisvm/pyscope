import argparse


def main():
	parse_arguments()

def parse_arguments():
	# create the parser and parse arguments for this
	# module. 
	parser = argparse.ArgumentParser() 
	parser.add_argument('-a', '--all', help='do not ignore entries starting with .')
	args = parser.parse_args()

	# change the Namespace obj to a python dictionary and 
	# return the dictionary 
	return vars(args)