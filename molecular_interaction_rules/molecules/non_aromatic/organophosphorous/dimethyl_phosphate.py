#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Dimethyl Phosphate
# -----------------------------------------

# Imports
# -------

import textwrap

class DimethylPhosphate(object):

    def __init__(self):

        self.resi_name = 'DMEP'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
            'O1': self.get_double_bond_oxygen_lone_pair_donor()
        }

        return monomer_a_species

    def get_double_bond_oxygen_lone_pair_donor(self):

        zmatrix = '''\
          O11
          P11  O11  1.5085
          O12  P11  1.6377  O11  115.2694
          H11  O12  0.9709  P11  108.4278  O11  -21.0969
          O13  P11  1.6251  O12  101.1193  H11  107.3959
          O14  P11  1.6311  O12  102.5485  H11 -148.9298
          C11  O13  1.4551  P11  115.2049  O11  -50.3827
          C12  O14  1.4542  P11  115.4507  O11  -44.3740
          C13  O14  1.4542  P11  115.4507  O11  -44.3740
          H12  C11  1.0994  O13  109.8941  P11  -68.8607
          H13  C11  1.0994  O13  109.8941  P11   53.1472
          H14  C11  1.0994  O13  109.8941  P11  172.3540
          H15  C12  1.0994  O14  109.8941  P11  170.8612
          H16  C12  1.0994  O14  109.8941  P11   51.3387
          H17  C12  1.0994  O14  109.8941  P11  -70.4974
          X11  O11  1.0000  P11   90.0000  O12  180.0000
          -1 1
        '''

        atom_name = [
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_species(self):

      '''

      Get the Monomer B Species

      '''

      monomer_b_species = {
          'O1': self.get_monomer_b_oxygen_zmatrix()
      }

      return monomer_b_species

    def get_monomer_b_oxygen_zmatrix(self):

        zmatrix = '''\
              O11
              P11  O11  1.5085
              O12  P11  1.6377  O11  115.2694
              H11  O12  0.9709  P11  108.4278  O11  -21.0969
              O13  P11  1.6251  O12  101.1193  H11  107.3959
              O14  P11  1.6311  O12  102.5485  H11 -148.9298
              C11  O13  1.4551  P11  115.2049  O11  -50.3827
              C12  O14  1.4542  P11  115.4507  O11  -44.3740
              C13  O14  1.4542  P11  115.4507  O11  -44.3740
              H12  C11  1.0994  O13  109.8941  P11  -68.8607
              H13  C11  1.0994  O13  109.8941  P11   53.1472
              H14  C11  1.0994  O13  109.8941  P11  172.3540
              H15  C12  1.0994  O14  109.8941  P11  170.8612
              H16  C12  1.0994  O14  109.8941  P11   51.3387
              H17  C12  1.0994  O14  109.8941  P11  -70.4974
              X11  O11  1.0000  P11   90.0000  O12  180.0000
              -1 1
          '''

        atom_name = [
          ''
        ]

        return textwrap.dedent(zmatrix), atom_name
