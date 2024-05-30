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

from molecular_interaction_rules.molecules.aromatic.azulene import Azulene
from molecular_interaction_rules.molecules.aromatic.benzene import Benzene
from molecular_interaction_rules.molecules.aromatic.bipyrrole import Bipyrrole
from molecular_interaction_rules.molecules.aromatic.bromobenzene import BromoBenzene
from molecular_interaction_rules.molecules.aromatic.chlorobenzene import ChloroBenzene
from molecular_interaction_rules.molecules.aromatic.fluorobenzene import FluoroBenzene
from molecular_interaction_rules.molecules.aromatic.four_pyridinone import FourPyridinone
from molecular_interaction_rules.molecules.aromatic.furan import Furan
from molecular_interaction_rules.molecules.aromatic.imidazole import Imidazole
from molecular_interaction_rules.molecules.aromatic.imidazolium import Imidazolium
from molecular_interaction_rules.molecules.aromatic.indole import Indole
from molecular_interaction_rules.molecules.aromatic.indolizine import Indolizine
from molecular_interaction_rules.molecules.aromatic.iodobenzene import IodoBenzene
from molecular_interaction_rules.molecules.aromatic.isoxazole import Isoxazole
from molecular_interaction_rules.molecules.aromatic.methyleneoxindole import Methyleneoxindole
from molecular_interaction_rules.molecules.aromatic.nitrobenzene import Nitrobenzene
from molecular_interaction_rules.molecules.aromatic.one_phenyl_four_pyridinone import OnePhenylFourPyridinone
from molecular_interaction_rules.molecules.aromatic.phenol import Phenol
from molecular_interaction_rules.molecules.aromatic.phenoxazine import Phenoxazine
from molecular_interaction_rules.molecules.aromatic.pyridine import Pyridine
from molecular_interaction_rules.molecules.aromatic.pyridinium import Pyridinium
from molecular_interaction_rules.molecules.aromatic.pyrimidine import Pyrimidine
from molecular_interaction_rules.molecules.aromatic.pyrrolidine import Pyrrolidine
from molecular_interaction_rules.molecules.aromatic.thiophene import Thiophene
from molecular_interaction_rules.molecules.aromatic.three_amino_pyridine import ThreeAminoPyridine
from molecular_interaction_rules.molecules.aromatic.two_h_pyran import TwoHPyran
from molecular_interaction_rules.molecules.aromatic.uracil import Uracil

class MoleculerDatabase(object):

    def __init__(self):

        self.master_list = self.build_molecular_database()

    def build_molecular_database(self):

        molecules = [
            
            # Aromatics
          
            Azulene,
            Benzene,
            Bipyrrole,
            BromoBenzene,
            ChloroBenzene,
            FluoroBenzene,
            FourPyridinone,
            Furan,
            Imidazole,
            Imidazolium,
            Indole,
            Indolizine,
            IodoBenzene,
            Isoxazole,
            Methyleneoxindole,
            Nitrobenzene,
            OnePhenylFourPyridinone,
            Phenol,
            Phenoxazine,
            Pyridine,
            Pyridinium,
            Pyrimidine,
            Pyrrolidine,
            Thiophene,
            ThreeAminoPyridine,
            TwoHPyran,
            Uracil

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
      )

      monomer_b = self.get_monomer_coordinates(
        molecule_name_2,
        atom_name_2,
        monomer_b=True,
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

