#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Dimethylether
# ------------------------------------

# Imports
# -------

import textwrap

class Dimethylether(object):

    def __init__(self):

        self.resi_name = 'DMEE'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
          'O1': self.get_monomer_a_oxygen_zmatrix()
        }

        return monomer_a_species

    def get_monomer_a_oxygen_zmatrix(self):

        zmatrix = '''\
          O11
          C11 O11 1.4535
          C12 O11 1.4535 C11  59.5066
          H11 C12 1.0934 C11 119.3094 O11 -102.7509
          H11 C12 1.0934 C11 119.3094 O11  102.7509
          H11 C11 1.0934 C12 119.3094 H11  154.4981
          H11 C11 1.0934 C12 119.3094 H11    0.0000
          X11 C11 1.0000 O11  90.0000 C12  180.0000
          0 1
        '''

        atom_name = [
            'O2', 'C1', 'C3', 'H11', 'H12', 'H13', 'H31', 'H32', 'H33'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_species(self):

        monomer_b_species = {
            'O1': self.get_monomer_b_oxygen_zmatrix()
        }

        return monomer_b_species

    def get_monomer_b_oxygen_zmatrix(self):

        zmatrix = '''\
          O21  :1  DISTANCE  :2  180.0000  :3    90.0000
          C21 O21 1.4535     :1  180.0000  :2   180.0000
          C22 O21 1.4535 C21  59.5066      :1     0.0000
          H21 C22 1.0934 C21 119.3094 O21 -102.7509
          H21 C22 1.0934 C21 119.3094 O21  102.7509
          H21 C21 1.0934 C22 119.3094 H21  154.4981
          H21 C21 1.0934 C22 119.3094 H21    0.0000
          X21 C21 1.0000 O21  90.0000 C22  180.0000
          0 1
        '''

        atom_name = [

        ]

        return textwrap.dedent(zmatrix), atom_name
