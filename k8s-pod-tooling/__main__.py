import argparse
from dockerfile_parse import DockerfileParser
from .instrument import instrument
#from pprint import pprint


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-instrument", help="the image dockerfile",default="Dockerfile",required=False)
	args = parser.parse_args()
	instrument( args.instrument )


if __name__ == "__main__":
    # execute only if run as a script
    main()