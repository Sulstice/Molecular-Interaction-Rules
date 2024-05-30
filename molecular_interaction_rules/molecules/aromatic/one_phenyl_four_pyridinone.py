#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: 1-Phenyl, 4-Pyridinone
# ---------------------------------------------

# Imports
# -------
import textwrap

class OnePhenylFourPyridinone(object):

    def __init__(self):

        self.resi_name = '1PH4PO'

    def get_monomer_a_species(self):

        '''

        Get the Monomer A Species

        '''

        monomer_a_species = {
            'RC1': self.get_monomer_a_ring_centroid_monomer_zmatrix(),
            'N1': self.get_monomer_a_ring_centroid_nitrogen_zmatrix()
        }

        return monomer_a_species

    def get_monomer_a_ring_centroid_monomer_zmatrix(self):

        zmatrix = '''\
            X11
            C11      X11   1.3940
            N11      C11    1.4267      X11  -180.0000
            C12      C11    1.3869      N11  119.9462    X11   0.0000
            C13      C12    1.3849      C11  119.7972    N11  179.5279
            H11      C13    1.0748      C12  119.5699    C11 -179.9400
            C14      C13    1.3854      C12  120.2738    C11    0.9482
            H12      C14    1.0747      C13  120.1299    C12  179.5240
            C15      C14    1.3854      C13  119.7400    C12   -0.4759
            H13      C15    1.0748      C14  120.1502    C13 -179.5824
            C16      C11    1.3869      C12  120.1075    C13   -0.4722
            H14      C16    1.0748      C11  119.7344    N11   -1.2912
            H15      C12    1.0748      C11  119.7344    N11   -1.2909
            C17      N11    1.3725      C11  120.8952    C12  122.5385
            H16      C17    1.0725      N11  114.9734    C11   -0.9724
            C18      C17    1.3369      N11  122.8323    C11  179.8872
            H17      C18    1.0729      C17  120.2547    N11  179.4816
            C19      C18    1.4641      C17  121.4129    N11    0.2205
            O11      C19    1.2060      C18  123.3503    C17  179.8929
            C20      C19    1.4641      C18  113.2993    C17   -0.1069
            H18      C20    1.0729      C19  118.3283    C18 -179.3819
            C21      N11    1.3725      C11  120.8952    C12  -57.4613
            H19      C21    1.0725      N11  114.9734    C11   -0.9726
            0 1
        '''

        atom_name = [
          'C7', 'N1', 'C12', 'C11', 'H11', 'C10', 'H10', 'C9', 'H9', 'C8', 'H8', 'C12',
          'C6', 'H6', 'C5', 'H5', 'C4', 'O4', 'C3', 'H3', 'C2', 'H2'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_a_ring_centroid_nitrogen_zmatrix(self):

        zmatrix = '''\
            X11
            N11  X11  1.3940
            C11  N11  1.4305  X11  180.0000
            C12  C11  1.4059  N11  119.9462  X11   180.0000
            C13  C12  1.4059  C11  119.7972  N11  179.5279
            H11  C13  1.0748  C12  119.5699  C11 -179.9400
            C14  C13  1.4059  C12  120.2738  C11    0.9482
            H12  C14  1.0747  C13  120.1299  C12  179.5240
            C15  C14  1.4059  C13  119.7400  C12   -0.4759
            H13  C15  1.0748  C14  120.1502  C13 -179.5824
            C16  C11  1.4059  C12  120.1075  C13   -0.4722
            H14  C16  1.0748  C11  119.7344  N11   -1.2912
            H15  C12  1.0748  C11  119.7344  N11   -1.2909
            C17  N11  1.3725  C11  120.8952  C12  122.5385
            H16  C17  1.0725  N11  114.9734  C11   -0.9724
            C18  C17  1.3369  N11  122.8323  C11  179.8872
            H17  C18  1.0729  C17  120.2547  N11  179.4816
            C19  C18  1.4641  C17  121.4129  N11    0.2205
            O11  C19  1.2060  C18  123.3503  C17  179.8929
            C20  C19  1.4641  C18  113.2993  C17   -0.1069
            H18  C20  1.0729  C19  118.3283  C18 -179.3819
            C21  N11  1.3725  C11  120.8952  C12  -57.4613
            H19  C21  1.0725  N11  114.9734  C11   -0.9726
            0 1
        '''

        atom_name = [
          'N1', 'C7', 'C12', 'C11', 'H11', 'C10', 'H10', 'C9', 'H9', 'C8', 'H8', 'C12',
          'C6', 'H6', 'C5', 'H5', 'C4', 'O4', 'C3', 'H3', 'C2', 'H2'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_species(self):

        monomer_b_species = {
          'RC1': self.get_monomer_b_ring_centroid_zmatrix(),
          'N1': self.get_monomer_b_ring_centroid_nitrogen_zmatrix()
        }

        return monomer_b_species

    def get_monomer_b_ring_centroid_zmatrix(self):

        zmatrix = '''\
            X21    :1  DISTANCE  :2   180.0000     :3   90.0000
            C21   X21  1.3940    :1   90.0000      :2  180.0000
            N21   C21  1.4305    X21  -180.0000    :1   90.0000
            C22   C21  1.4059    N21  119.9462    X21   0.0000
            C23   C22  1.4059    C21  119.7972    N21  179.5279
            H21   C23  1.0748    C22  119.5699    C21 -179.9400
            C24   C23  1.4059    C22  120.2738    C21    0.9482
            H22   C24  1.0747    C23  120.1299    C22  179.5240
            C25   C24  1.4059    C23  119.7400    C22   -0.4759
            H23   C25  1.0748    C24  120.1502    C23 -179.5824
            C26   C21  1.4059    C22  120.1075    C23   -0.4722
            H24   C26  1.0748    C21  119.7344    N21   -1.2912
            H25   C22  1.0748    C21  119.7344    N21   -1.2909
            C27   N21  1.3725    C21  120.8952    C22  122.5385
            H26   C27  1.0725    N21  114.9734    C21   -0.9724
            C28   C27  1.3369    N21  122.8323    C21  179.8872
            H27   C28  1.0729    C27  120.2547    N21  179.4816
            C29   C28  1.4641    C27  121.4129    N21    0.2205
            O21   C29  1.2060    C28  123.3503    C27  179.8929
            C30   C29  1.4641    C28  113.2993    C27   -0.1069
            H28   C30  1.0729    C29  118.3283    C28 -179.3819
            C31   N21  1.3725    C21  120.8952    C22  -57.4613
            H29   C31  1.0725    N21  114.9734    C21   -0.9726
            0 1
        '''

        atom_name = [
          'C7', 'N1', 'C12', 'C11', 'H11', 'C10', 'H10', 'C9', 'H9', 'C8', 'H8', 'C12',
          'C6', 'H6', 'C5', 'H5', 'C4', 'O4', 'C3', 'H3', 'C2', 'H2'
        ]

        return textwrap.dedent(zmatrix), atom_name

    def get_monomer_b_ring_centroid_nitrogen_zmatrix(self):

        zmatrix = '''\
            X21    :1  DISTANCE  :2   180.0000     :3   90.0000
            N21   X21  1.3940    :1   90.0000      :2  180.0000
            C21   N21  1.4267    X21  180.0000    :1   90.0000
            C22   C21  1.3869    N21  119.9462    X21   180.0000
            C23   C22  1.3849    C21  119.7972    N21  179.5279
            H21   C23  1.0748    C22  119.5699    C21 -179.9400
            C24   C23  1.3854    C22  120.2738    C21    0.9482
            H22   C24  1.0747    C23  120.1299    C22  179.5240
            C25   C24  1.3854    C23  119.7400    C22   -0.4759
            H23   C25  1.0748    C24  120.1502    C23 -179.5824
            C26   C21  1.3869    C22  120.1075    C23   -0.4722
            H24   C26  1.0748    C21  119.7344    N21   -1.2912
            H25   C22  1.0748    C21  119.7344    N21   -1.2909
            C27   N21  1.3725    C21  120.8952    C22  122.5385
            H26   C27  1.0725    N21  114.9734    C21   -0.9724
            C28   C27  1.3369    N21  122.8323    C21  179.8872
            H27   C28  1.0729    C27  120.2547    N21  179.4816
            C29   C28  1.4641    C27  121.4129    N21    0.2205
            O21   C29  1.2060    C28  123.3503    C27  179.8929
            C30   C29  1.4641    C28  113.2993    C27   -0.1069
            H28   C30  1.0729    C29  118.3283    C28 -179.3819
            C31   N21  1.3725    C21  120.8952    C22  -57.4613
            H29   C31  1.0725    N21  114.9734    C21   -0.9726
            0 1
        '''

        atom_name = [
          'N1', 'C7', 'C12', 'C11', 'H11', 'C10', 'H10', 'C9', 'H9', 'C8', 'H8', 'C12',
          'C6', 'H6', 'C5', 'H5', 'C4', 'O4', 'C3', 'H3', 'C2', 'H2'
        ]

        return textwrap.dedent(zmatrix), atom_name
