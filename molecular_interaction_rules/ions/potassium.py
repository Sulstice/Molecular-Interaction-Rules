#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Potassium
# --------------------------------

# Imports
# -------

import textwrap

class Potassium(object):

    def __init__(self):

        pass

    def get_monomer_a_species(self):

        ion_a_species = {
            'ion': self.get_ion_a()
        }

        return ion_a_species

    def get_ion_a(self):

        zmatrix = '''\
            K11
            1 1
        '''

        return textwrap.dedent(zmatrix)


    def get_ion_b_species(self):

        ion_b_species = {
            'K': self.ion_b_zmatrix()
        }

        return ion_b_species

    def ion_b_zmatrix(self):

        zmatrix = '''\
            K21  :1  DISTANCE  :2  120.0000  :3    0.0000
            1 1
        '''

        return textwrap.dedent(zmatrix)
