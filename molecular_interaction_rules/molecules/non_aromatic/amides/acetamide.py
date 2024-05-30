#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Acetamide
# --------------------------------

# Imports
# -------

import textwrap

class Acetamide(object):

    def __init__(self):

        self.resi_name = 'ACEM'

    def get_monomer_a_species(self):

        monomer_a_species = {
          'H1': self.get_monomer_a_nitrogen_zmatrix(),
        }

        return monomer_a_species

    def get_monomer_b_species(self):

        monomer_b_species = {
          'H1': self.get_monomer_b_nitrogen_zmatrix()
        }

        return monomer_b_species

    def get_monomer_a_nitrogen_zmatrix(self):

        zmatrix = '''\
            H11
            N11  H11 1.0009
            C11  N11 1.3755  H11 121.8612
            C12  C11 1.5191  N11 115.2309  H11 180.0000
            H12  C12 1.1015  C11 108.7916  N11 -89.7822
            H13  C12 1.0970  C11 108.6486  N11 152.3051
            H14  C12 1.1004  C11 112.3470  N11  30.4673
            O11  C11 1.2330  C12 122.8739  H11  89.6015
            H15  N11 1.0121  C11 118.0823  C12 173.4905
            X11  H11 1.0000  N11  90.0000  C11 180.0000
            0 1
        '''

        atom_name = [
          'HC', 'N', 'C', 'CC', 'HC1', 'HC2', 'HC3', 'O', 'HT',
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_nitrogen_zmatrix(self):

        zmatrix = '''\
              H21   :1   DISTANCE  :2   90.0000   :3   90.0000
              X21  H21    1.0000  :1   90.0000   :2    0.0000
              N21  H21    0.9316  X21  90.0000   :1  180.0000
              C21  N21    1.4349  H21 120.0000  :1  180.0000
              C22  C21 1.5191 N21 115.2309 H21 180.0000
              H22  C22 1.1015 C21 108.7916 N21 -89.7822
              H23  C22 1.0970 C21 108.6486 N21 152.3051
              H24  C22 1.1004 C21 112.3470 N21  30.4673
              O21  C21 1.2330 C22 122.8739 H21  89.6015
              H25  N21 1.0121 C21 118.0823 C22 173.4905
              0 1
          '''

        atom_name = [
          'HC', 'N', 'C', 'CC', 'HC1', 'HC2', 'HC3', 'O', 'HT',
        ]

        return textwrap.dedent(zmatrix), atom_name
