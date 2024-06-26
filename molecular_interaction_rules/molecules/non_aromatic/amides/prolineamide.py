#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Prolineamide
# -----------------------------------

# Imports
# -------

import textwrap

class Prolineamide(object):

    def __init__(self):

        self.resi_name = 'PNH1'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
          'H1': self.get_monomer_a_amide_nitrogen(),
          'H2': self.get_monomer_a_sp3_carbon_one_hydrogen(),
        }

        return monomer_a_species

    def get_monomer_a_amide_nitrogen(self):

        zmatrix = '''\
            H11
            N11  H11  0.9942
            C11  N11  1.3445  H11  120.5945
            C12  C11  1.5300  N11  115.3149  H11   -8.4508
            N12  C12  1.4641  C11  112.2071  N11   20.4696
            C13  N12  1.4615  C12  105.8259  C11   99.2627
            H12  N12  1.0010  C12  109.4950  C11 -143.0365
            C14  C13  1.5322  N12  105.5222  H12  -81.1190
            C15  C12  1.5300  C11  111.9567  N11  141.5078
            O11  C11  1.2019  C12  121.1157  N12 -162.3860
            H13  C13  1.0846  N12  108.5988  C12  -81.7117
            H14  C13  1.0846  N12  110.5262  C12  160.4969
            H15  C14  1.0846  C13  112.8941  N12 -156.2638
            H16  C14  1.0846  C13  112.8941  N12   83.8645
            H17  C15  1.0846  C12  110.2896  C11   -0.3212
            H18  C15  1.0846  C12  111.1976  C11  118.1844
            H19  C12  1.0846  C11  104.5232  N11  -97.9238
            H20  N11  0.9942  C11  120.5945  C12 -179.6150
            X11  H11  1.0000  N11   90.0000  C11  180.0000
            0 1
        '''

        atom_name = [
          'H9', 'N2', 'C5', 'C1', 'N1', 'C4', 'H8', 'C3', 'C2', 'O', 'H6', 'H7', 'H4', 'H5', 'H2', 'H3', 'H1', 'H10'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_a_sp3_carbon_one_hydrogen(self):

        zmatrix = '''\
            H11
            C12  H11  1.0846
            C11  C12  1.5300  H11  104.5232
            N11  C11  1.3445  C12  115.3149  H11  -97.9238
            N12  C12  1.4641  C11  112.2071  N11   20.4696
            C13  N12  1.4615  C12  105.8259  C11   99.2627
            H12  N12  1.0010  C12  109.4950  C11 -143.0365
            C14  C13  1.5322  N12  105.5222  H12  -81.1190
            C15  C12  1.5300  C11  111.9567  N11  141.5078
            O11  C11  1.2019  C12  121.1157  N12 -162.3860
            H13  C13  1.0846  N12  108.5988  C12  -81.7117
            H14  C13  1.0846  N12  110.5262  C12  160.4969
            H15  C14  1.0846  C13  112.8941  N12 -156.2638
            H16  C14  1.0846  C13  112.8941  N12   83.8645
            H17  C15  1.0846  C12  110.2896  C11   -0.3212
            H18  C15  1.0846  C12  111.1976  C11  118.1844
            H19  N11  0.9942  C11  120.5945  C12 -179.6150
            H20  N11  0.9942  C11  120.5945  C12   -8.4508
            X11  H11  1.0000  C12   90.0000  C11  180.0000
            0 1
        '''

        atom_name = [
          'H1', 'C1', 'C5', 'N2', 'N1', 'C4', 'H8', 'C3', 'C2', 'O', 'H6', 'H7', 'H4', 'H5', 'H2', 'H3', 'H9', 'H10'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_species(self):

        '''

        Get the Monomer B Species

        '''

        monomer_b_species = {
            'H1': self.get_monomer_b_nitrogen_hydrogen_zmatrix(),
            'H2': self.get_monomer_b_hydrogen_zmatrix()
        }

        return monomer_b_species

    def get_monomer_b_nitrogen_hydrogen_zmatrix(self):

        zmatrix = '''\
            H21   :1   DISTANCE     :2  90.0000   :3   90.0000
            X21  H21    1.0000      :1  90.0000   :2    0.0000
            N21  H21  0.9942  X21   90.0000       :2  180.0000
            C21  N21  1.3445  H21  120.5945       :1  180.0000
            C22  C21  1.5300  N21  115.3149  H21   -8.4508
            N22  C22  1.4641  C21  112.2071  N21   20.4696
            C23  N22  1.4615  C22  105.8259  C21   99.2627
            H22  N22  1.0010  C22  109.4950  C21 -143.0365
            C24  C23  1.5322  N22  105.5222  H22  -81.1190
            C25  C22  1.5300  C21  111.9567  N21  141.5078
            O21  C21  1.2019  C22  121.1157  N22 -162.3860
            H23  C23  1.0846  N22  108.5988  C22  -81.7117
            H24  C23  1.0846  N22  110.5262  C22  160.4969
            H25  C24  1.0846  C23  112.8941  N22 -156.2638
            H26  C24  1.0846  C23  112.8941  N22   83.8645
            H27  C25  1.0846  C22  110.2896  C21   -0.3212
            H28  C25  1.0846  C22  111.1976  C21  118.1844
            H29  C22  1.0846  C21  104.5232  N21  -97.9238
            H21  N21  0.9942  C21  120.5945  C22 -179.6150
            X21  H21  1.0000  N21   90.0000  C21  180.0000
            0 1
        '''

        atom_name = [
          'H9', 'N2', 'C5', 'C1', 'N1', 'C4', 'H8', 'C3', 'C2', 'O', 'H6', 'H7', 'H4', 'H5', 'H2', 'H3', 'H1', 'H10'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_hydrogen_zmatrix(self):

        zmatrix = '''\
            H21    :1   DISTANCE   :2  90.0000   :3   90.0000
            X21  H21    1.0000     :1  90.0000   :2    0.0000
            C22  H21  1.0846  X21  90.0000       :2  180.0000
            C21  C22  1.5300  H21  104.5232      :1  180.0000
            N21  C21  1.3445  C22  115.3149  H21  -97.9238
            N22  C22  1.4641  C21  112.2071  N21   20.4696
            C23  N22  1.4615  C22  105.8259  C21   99.2627
            H22  N22  1.0010  C22  109.4950  C21 -143.0365
            C24  C23  1.5322  N22  105.5222  H22  -81.1190
            C25  C22  1.5300  C21  111.9567  N21  141.5078
            O21  C21  1.2019  C22  121.1157  N22 -162.3860
            H23  C23  1.0846  N22  108.5988  C22  -81.7117
            H24  C23  1.0846  N22  110.5262  C22  160.4969
            H25  C24  1.0846  C23  112.8941  N22 -156.2638
            H26  C24  1.0846  C23  112.8941  N22   83.8645
            H27  C25  1.0846  C22  110.2896  C21   -0.3212
            H28  C25  1.0846  C22  111.1976  C21  118.1844
            H29  N21  0.9942  C21  120.5945  C22 -179.6150
            H30  N21  0.9942  C21  120.5945  C22   -8.4508
            0 1
        '''

        atom_name = [
          'H1', 'C1', 'C5', 'N2', 'N1', 'C4', 'H8', 'C3', 'C2', 'O', 'H6', 'H7', 'H4', 'H5', 'H2', 'H3', 'H9', 'H10'
        ]

        return textwrap.dedent(zmatrix), atom_name
