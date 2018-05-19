from pll import package
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Package for AWS Lambda.')
    parser.add_argument('--config', help="path to a config file")
    args = parser.parse_args()

    package(args.__dict__.get('config'))