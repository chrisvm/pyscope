import argparse


def parse_arguments():
	# create the parser
	parser = argparse.ArgumentParser()

	# add the extra arguments
	parser.add_argument('-f', '--filename')
def main():
	args = parse_arguments()
