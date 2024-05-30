#!/usr/bin/env python3
#
# Lennard-Jones-Drill-2: Monomers
# -------------------------------

class MolecularInteractionRules(object):

    def __init__(self):

        self.master_list = []

        self.functional_group_mapping = {
          'aromatics': self.get_aromatics(),
          'alcohols': self.get_alcohols(),
          'alkanes': self.get_alkanes(),
          'alkenes': self.get_alkenes(),
          'alkynes': self.get_alkynes(),
          'amides': self.get_amides(),
          'amines': self.get_amines(),
          'carbonyls': self.get_carbonyls(),
          'ethers': self.get_ethers(),
          'halogens': self.get_halogens(),
          'imines': self.get_imines(),
          'nitriles': self.get_nitriles(),
          'organophosphorous': self.get_organophosphorous(),
          'organosulfur': self.get_organosulfur(),
        }

    def get_ions(self):

        from molecular_interaction_rules.ions import __all__

        return __all__

    def get_aromatics(self):

        from molecular_interaction_rules.aromatic import __all__

        return __all__

    def get_alcohols(self):

        from molecular_interaction_rules.molecules.non_aromatic.alcohols import __all__

        return __all__

    def get_alkanes(self):

        from molecular_interaction_rules.molecules.non_aromatic.alkanes import __all__

        return __all__

    def get_alkenes(self):

        from molecular_interaction_rules.molecules.non_aromatic.alkenes import __all__

        return __all__

    def get_alkynes(self):

        from molecular_interaction_rules.molecules.non_aromatic.alkynes import __all__

        return __all__

    def get_amides(self):

        from molecular_interaction_rules.molecules.non_aromatic.amides import __all__

        return __all__

    def get_amines(self):

        from molecular_interaction_rules.molecules.non_aromatic.amines import __all__

        return __all__

    def get_carbonyls(self):

        from molecular_interaction_rules.molecules.non_aromatic.carbonyls import __all__

        return __all__

    def get_ethers(self):

        from molecular_interaction_rules.molecules.non_aromatic.ethers import __all__

        return __all__

    def get_halogens(self):

        from molecular_interaction_rules.molecules.non_aromatic.halogens import __all__

        return __all__

    def get_imines(self):

        from molecular_interaction_rules.molecules.non_aromatic.imines import __all__

        return __all__

    def get_nitriles(self):

        from molecular_interaction_rules.molecules.non_aromatic.nitriles import __all__

        return __all__

    def get_organophosphorous(self):

        from molecular_interaction_rules.molecules.non_aromatic.organophosphorous import __all__

        return __all__

    def get_organosulfur(self):

        from molecular_interaction_rules.molecules.non_aromatic.organosulfur import __all__

        return __all__

    def get_master_list(self):

        '''

        Get the Full Master List

        '''

        self.master_list.append(self.get_aromatics())
        self.master_list.append(self.get_alcohols())
        self.master_list.append(self.get_alkanes())
        self.master_list.append(self.get_alkenes())
        self.master_list.append(self.get_alkynes())

        self.master_list.append(self.get_amides())
        self.master_list.append(self.get_amines())

        self.master_list.append(self.get_carbonyls())
        self.master_list.append(self.get_ethers())
        self.master_list.append(self.get_halogens())

        self.master_list.append(self.get_imines())
        self.master_list.append(self.get_nitriles())
        self.master_list.append(self.get_organophosphorous())
        self.master_list.append(self.get_organosulfur())
        self.master_list.append(self.get_ions())

        master_list = sum(self.master_list, [])

        return master_list

    def get_monomer(self, key):

        '''

        Retrieve a monomer class by it's key

        '''

        master_list = self.get_master_list()

        return master_list[key]

    def get_ion(self, key):

        '''

        Retrieve a ion class by it's key

        '''

        ions = self.get_ions()

        return ions[key]


    def get_monomer_coordinates(
      self,
      monomer,
      atom_name,
      monomer_b=False,
      functional_group_family=False
    ):


      '''

      Get the Coordinates of a Monomer in Different Formats

      '''

      coordinates = ''

      for molecule in self.get_master_list():

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

            return coordinates, molecule.resi_name, rank_order

    def get_dimer_coordinates(
      self,
      molecule_name_1,
      atom_name_1,
      molecule_name_2,
      atom_name_2,
    ):

      '''

      Get the Dimer Coordinates

      '''

      monomer_a, resi_name_a, rank_order_a = self.get_monomer_coordinates(
        molecule_name_1,
        atom_name_1,
        xyz=False,
        verbose=True,
      )

      monomer_b, resi_name_b, rank_order_b = self.get_monomer_coordinates(
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

