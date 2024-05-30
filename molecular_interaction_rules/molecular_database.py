#!/usr/bin/env python3
#
# Molecular Interation Rules: MoleculerDatabase
# ---------------------------------------------

# Imports
# -------

import os, sys

# Reconfigurations
# ----------------

if os.name == 'nt':
   sys.stdin.reconfigure(encoding='utf-8')
   sys.stdout.reconfigure(encoding='utf-8')

# Molecules

## Aromatics

from molecular_interaction_rules.molecules.aromatic.benzene import Benzene

class MoleculerDatabase(object):

    def __init__(self):

        self.master_list = self.build_molecular_database()

    def build_molecular_database(self):

        molecules = [

            Benzene

        ]

        return molecules

    def get_atom_names(self, monomer):

        '''

        Retrieve Atom Names of Molecule

        '''

        atom_names = []

        for molecule in self.master_list:

            name = str(molecule.__name__).lower()

            if name == monomer:
                molecule = molecule()
                atom_names = list(molecule.get_monomer_a_species().keys())

        return atom_names

    def get_monomer_coordinates(
      self,
      monomer,
      atom_name,
      monomer_b=False,
      functional_group_family=False
    ):


      '''

      Get the Coordinates of a Monomer

      '''

      coordinates = ''

      for molecule in self.master_list:

        name = str(molecule.__name__).lower()

        if name == monomer:

            molecule = molecule()
            fg_family = molecule.__module__.split('.')[-2]

            if functional_group_family:
                return fg_family
            try:
              if monomer_b:
                coordinates = molecule.get_monomer_b_species()[atom_name][0]
                rank_order = molecule.get_monomer_b_species()[atom_name][1]
              else:
                coordinates = molecule.get_monomer_a_species()[atom_name][0]
                rank_order = molecule.get_monomer_a_species()[atom_name][1]

            except KeyError as e:
                print ('Missing Entry: %s | %s' % (name, atom_name))
                return coordinates

            return coordinates

    def form_dimer_coordinates(
      self,
      molecule_name_1,
      atom_name_1,
      molecule_name_2,
      atom_name_2,
    ):

      '''

      Get the Dimer Coordinates

      '''

      monomer_a = self.get_monomer_coordinates(
        molecule_name_1,
        atom_name_1,
        xyz=False,
        verbose=True,
      )

      monomer_b = self.get_monomer_coordinates(
        molecule_name_2,
        atom_name_2,
        monomer_b=True,
        xyz=False,
        verbose=True
      )

      # Fetch First 3 Atoms from Monomer A

      monomer_atom_one = monomer_a.split('\n')[0]
      monomer_atom_two = monomer_a.split('\n')[1].split()[0]
      monomer_atom_three = monomer_a.split('\n')[2].split()[0]

      # Replace Monomer B Connections with Atoms from Monomer A

      monomer_b = monomer_b.replace(':1', monomer_atom_one)
      monomer_b = monomer_b.replace(':2', monomer_atom_two)
      monomer_b = monomer_b.replace(':3', monomer_atom_three)

      dimer = monomer_a + '--\n' + monomer_b

      return dimer

