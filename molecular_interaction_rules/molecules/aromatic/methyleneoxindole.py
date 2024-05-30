#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Indole
# -----------------------------

# Imports
# -------
import textwrap

class Methyleneoxindole(object):

  def __init__(self):

      self.resi_name = 'MEOI'

  def get_monomer_a_species(self):

    monomer_a_species = {
      'RC1': self.monomer_a_aromatic_zmatrix()
    }

    return monomer_a_species

  def get_monomer_b_species(self):

    monomer_b_species = {
        'RC1': self.monomer_b_aromatic_zmatrix()
    }

    return monomer_b_species

  def monomer_a_aromatic_zmatrix(self):

      zmatrix = '''\
          X11
          N11  X11 1.0122
          C11  N11  1.3836  X11   59.0000
          C12  C11  1.4104  N11  130.4152  X11  180.0000
          C13  C12  1.4006  C11  117.2345  N11 -180.0000
          C14  C13  1.4233  C12  121.2757  C11   -0.0000
          C15  C14  1.3990  C13  121.3172  C12    0.0000
          C16  C11  1.4341  C12  122.4965  C13   -0.0000
          C17  C16  1.4395  C11  107.0716  C12 -180.0000
          C18  C17  1.3901  C16  106.8762  C15  180.0000
          H11  N11  1.0122  C11  125.2840  C12  0.0000
          H12  C14  1.0940  C13  119.0452  C12  180.0000
          H13  C15  1.0943  C14  120.6975  C13  180.0000
          H14  C17  1.0889  C16  127.5288  C11  180.0000
          H15  C18  1.0890  C17  130.1570  C16 -180.0000
          H16  C13  1.0939  C12  119.3067  C11  180.0000
          H17  C12  1.0944  C13  121.1026  C14 -180.0000
          0 1
      '''

      atom_name = [
        'NE1', 'CE2', 'CZ2', 'CH2', 'CZ3', 'CE3', 'CD2', 'CG', 'CD1',
        'HE1', 'HZ2', 'HH2', 'HZ3', 'HE3', 'HG', 'HD1'
      ]

      return textwrap.dedent(zmatrix), atom_name

  def monomer_b_aromatic_zmatrix(self):

    zmatrix = '''\
       X11
       N11  X11 1.1020
       C11  N11  1.3836  X11   59.0000
       C12  C11  1.4104  N11  130.4152  X11  180.0000
       C13  C12  1.4006  C11  117.2345  N11 -180.0000
       C14  C13  1.4233  C12  121.2757  C11   -0.0000
       C15  C14  1.3990  C13  121.3172  C12    0.0000
       C16  C11  1.4341  C12  122.4965  C13   -0.0000
       C17  C16  1.4395  C11  107.0716  C12 -180.0000
       C18  C17  1.3901  C16  106.8762  C15  180.0000
       H11  N11  1.0122  C11  125.2840  C12  0.0000
       H12  C14  1.0940  C13  119.0452  C12  180.0000
       H13  C15  1.0943  C14  120.6975  C13  180.0000
       H14  C17  1.0889  C16  127.5288  C11  180.0000
       H15  C18  1.0890  C17  130.1570  C16 -180.0000
       H16  C13  1.0939  C12  119.3067  C11  180.0000
       H17  C12  1.0944  C13  121.1026  C14 -180.0000
       0 1
    '''

    atom_name = [
        'NE1', 'CE2', 'CZ2', 'CH2', 'CZ3', 'CE3', 'CD2', 'CG', 'CD1',
        'HE1', 'HZ2', 'HH2', 'HZ3', 'HE3', 'HG', 'HD1'
    ]

    return textwrap.dedent(zmatrix), atom_name

