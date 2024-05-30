#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Ethenamine
# ---------------------------------

# Imports
# -------

import textwrap

class Ethenamine(object):

    def __init__(self):

        self.resi_name = 'AMET'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
            'H1': self.get_terminal_carbon_zmatrix(),
            'H2': self.get_nitrogen_zmatrix(),
            'H3': self.get_center_carbon_zmatrix()
        }

        return monomer_a_species

    def get_terminal_carbon_zmatrix(self):

        zmatrix = '''\
          H11
          C12  H11 1.0936
          C11  C12 1.3542  H11  120.0928
          N11  C11 1.4039  C12  125.9409  H11    4.2658
          H12  C12 1.0897  C11  120.0928  N11 -174.6391
          H13  C11 1.0947  C12  120.0928  H11  180.0000
          H14  N11 1.0166  C11  114.2936  C12 -148.2024
          H15  N11 1.0166  C11  114.2936  C12  -18.5744
          X11  H11 1.0000  C12   90.0000  C11  180.0000
          0 1
        '''

        atom_name = [
          'H2','C1', 'C4','N6', 'H3', 'H5','H7', 'H8'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_nitrogen_zmatrix(self):

        zmatrix = '''\
          H11
          N11  H11  1.0166
          C11  N11  1.4039  H11  114.2936
          C12  C11  1.3542  N11  125.9409  H11  -18.5744
          H12  C12  1.0897  C11  120.0928  N11    4.2658
          H13  C12  1.0897  C11  120.0928  N11 -174.6391
          H14  C11  1.0897  C12  120.0928  H11  180.0000
          H15  N11  1.0166  C11  114.2936  C12 -148.2024
          X11  H11  1.0000  N11   90.0000  C11  180.0000
          0 1
        '''

        atom_names = [
          'H7', 'N6', 'C4', 'C1', 'H2', 'H3', 'H5', 'H8'
        ]

        return textwrap.dedent(zmatrix), atom_names

    def get_center_carbon_zmatrix(self):

        zmatrix = '''\
          H11
          C11  H11  1.0897
          C12  C11  1.3542  H11  120.0928
          N11  C11  1.4039  C12  125.9409  H11  180.0000
          H12  C12  1.0897  C11  120.0928  N11    4.2658
          H13  C12  1.0897  C11  120.0928  N11 -174.6391
          H14  N11  1.0166  C11  114.2936  C12 -148.2024
          H15  N11  1.0166  C11  114.2936  C12  -18.5744
          X11  H11  1.0000  C11   90.0000  C12  180.0000
          0 1
        '''

        atom_names = [
          'H5', 'C4', 'C1', 'N6', 'H2', 'H3', 'H7','H8'
        ]

        return textwrap.dedent(zmatrix), atom_names

    def get_monomer_b_species(self):

        monomer_b_species = {
        }

        return monomer_b_species
