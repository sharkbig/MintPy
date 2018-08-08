#!/usr/bin/env python3
############################################################
# Program is part of PySAR                                 #
# Copyright(c) 2018, Zhang Yunjun                          #
# Author:  Zhang Yunjun                                    #
############################################################


import os
import argparse
import h5py


###########################################################################################
EXAMPLE = """Example:
  remove_hdf5_dataset.py  ./INPUTS/ifgramStack.h5  unwrapPhase_unwCor
  remove_hdf5_dataset.py  velocity.h5  velocityStd
"""

def create_parser():
    parser = argparse.ArgumentParser(description='Remove an existing dataset from HDF5 file',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=EXAMPLE)

    parser.add_argument('file', type=str, help='HDF5 file of interest')
    parser.add_argument('dset', type=str, help='dataset to be removed.')
    return parser

def cmd_line_parse(iargs=None):
    parser = create_parser()
    inps = parser.parse_args(args=iargs)
    if os.path.splitext(inps.file)[1] not in ['.h5', '.he5']:
        raise ValueError('input file is not HDF5: {}'.format(inps.file))
    return inps


###########################################################################################
def main(iargs=None):
    inps = cmd_line_parse(iargs)
    with h5py.File(inps.file, 'r') as f:
        dset_list = list(f.keys())
    if inps.dset not in dset_list:
        raise ValueError(('input dataset do not exists: {}'
                          '\navailable datasets:\n{}').format(inps.dset, dset_list))

    with h5py.File(inps.file, 'a') as f:
        print('delete {} from file {}'.format(inps.dset, inps.file))
        del f[inps.dset]
    print('Done.')
    return inps.file


###########################################################################################
if __name__ == '__main__':
    main()