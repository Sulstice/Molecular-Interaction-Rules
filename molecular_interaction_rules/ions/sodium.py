#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Sodium
# ------------------------------

# Imports
# -------

import textwrap

class Sodium(object):

    __CGENFF_ATOM_TYPES__ = {
    }

    def __init__(self):

        pass

    def get_monomer_a_species(self):

        ion_a_species = {
            'ion': self.get_ion_a()
        }

        return ion_a_species

    def get_ion_a(self):

        zmatrix = '''\
            NA11
            1 1
        '''

        return textwrap.dedent(zmatrix)


    def get_ion_b_species(self):

       ion_b_species = {
         'NA': self.ion_b_zmatrix()
       }

       return ion_b_species

    def ion_b_zmatrix(self):

        zmatrix = '''\
            NA21  :1  DISTANCE  :2  120.0000  :3    0.0000
            1 1
        '''

        return textwrap.dedent(zmatrix)
