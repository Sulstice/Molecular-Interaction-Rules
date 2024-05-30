#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: MethylAcetamide
# --------------------------------------

# Imports
# -------

import textwrap

class MethylAcetamide(object):

    def __init__(self):

        self.resi_name = 'NMA'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
            'N1': self.get_monomer_a_nitrogen_zmatrix()
        }

        return monomer_a_species

    def get_monomer_a_nitrogen_zmatrix(self):

        zmatrix = '''\
            H17
            N11  N11  1.0104
            C11  N11  1.3686   C11  119.5274
            C12  C11  1.5185   N11  116.1617   C12  180.000000
            H11  C12  1.0996   C11  108.5139   N11 -121.489057
            H12  C12  1.0996   C11  108.5134   N11  121.532300
            H13  C12  1.1001   C11  113.2240   N11    0.021670
            O11  C11  1.2378   C12  122.4208   H11   58.513876
            C13  N11  1.4579   C11  120.3664   C12  179.979742
            H14  C13  1.1001   N11  110.5107   C11  -59.829220
            H15  C13  1.1001   N11  110.5001   C11   59.765460
            H16  C13  1.0978   N11  108.6683   C11  179.964368
            X11  H17  1.0000   N11   90.0000   C11  180.000000
            0 1
        '''

        atom_name = [
          'HR3', 'N', 'C', 'CL', 'HL1', 'HL2', 'HL3', 'O', 'CR', 'HR1', 'HR2',
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_species(self):

        '''

        Get the Monomer B Species

        '''

        monomer_b_species = {
            'N1': self.get_monomer_b_nitrogen_zmatrix()
        }

        return monomer_b_species

    def get_monomer_b_nitrogen_zmatrix(self):

        zmatrix = '''\
              N21   :1  DISTANCE   X11   90.0000    :2  180.0000
              C21  N21  1.3686    :1  122.2041   X11    0.0000
              C22  C21  1.5185   N21  122.2041   X11  180.0000
              H21  C22  1.0996   C21  108.5139   N21  -99.3805
              H22  C22  1.0996   C21  108.5134   N21  143.3108
              H23  C22  1.1001   C21  113.2240   N21   21.4177
              O21  C21  1.2378   C22  122.4208   H21   79.8706
              C23  N21  1.4579   C21  120.3664   C22  175.1165
              H24  C23  1.1001   N21  110.5107   C21  -71.1288
              H25  C23  1.1001   N21  110.5001   C21   49.2058
              H26  C23  1.0978   N21  108.6683   C21  168.4476
              H27  N21  1.0104   C21  119.5274   C22    5.3753
              0 1
          '''

        atom_name = [
          'N', 'C', 'CL', 'HL1', 'HL2', 'HL3', 'O', 'CR', 'HR1', 'HR2', 'HR3'
        ]

        return textwrap.dedent(zmatrix), atom_name
