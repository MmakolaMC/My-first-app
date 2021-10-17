from EurUsd import currency
import argparse

parser = argparse.ArgumentParser(description = 'Mean and Median Reversion')

parser.add_argument('--directory', action='store', dest='location', 
                    default='T:\Clive\CADJPY=X.csv',
                    help='Enter file location')                   
args = parser.parse_args()
directory = args.location

high, low, close = currency(directory)

