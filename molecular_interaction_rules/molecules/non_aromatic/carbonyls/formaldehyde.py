#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Formaldehyde
# -----------------------------------

# Imports
# -------

import textwrap

class Formaldehyde(object):

    def __init__(self):

        self.resi_name = 'form'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
            'O1': self.oxygen_lone_pair_donor_zmatrix(),
            'C1': self.carbon_sp2_zmatrix()
        }

        return monomer_a_species

    def get_monomer_b_species(self):

        monomer_b_species = {
        }

        return monomer_b_species

    def oxygen_lone_pair_donor_zmatrix(self):

        zmatrix = '''\
            O11
            C11 O11 1.2237
            H11 C11 1.1114 O11 121.6425
            H12 C11 1.1114 O11 121.6425 H11 180.0000
            X11 O11 1.0000 C11  90.0000 H11 180.0000
            0 1
        '''

        return textwrap.dedent(zmatrix)

    def carbon_sp2_zmatrix(self):

        zmatrix = '''\
            C11
            O11 C11 1.2237
            H11 C11 1.1114 O11 121.6425
            H12 C11 1.1114 O11 121.6425 H11 180.0000
            X11 O11 1.0000 C11  90.0000 H11 180.0000
            0 1
        '''

        return textwrap.dedent(zmatrix)
