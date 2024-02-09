import argparse
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def csv2pandas(csv_path):
    df = pd.read_csv(csv_path)
    df['id'] = df.index
    return df

if __name__ == "__main__":
    """
    Main function for executing the .py script.
    Command:
        -p path/<filename>.csv
    """
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", type=str, default='../input/measurements.csv',
                    help="path to csv. file")
    ap.add_argument("-m", "--method", type=str, default='knn',
                    help="specify a graph creation method ['voronoi','knn','radius']")
    args = vars(ap.parse_args())

    if args['method'] == 'voronoi':
        from voronoi import create_graph
    elif args['method'] == 'knn':
        from knn import create_graph
    elif args['method'] == 'radius':
        from radius import create_graph
    else:
        print("method {} is not implemented".format(args['method']))

    df = csv2pandas(args['path'])

    create_graph(df)

    plt.savefig('{}.pdf'.format(args['method']))
