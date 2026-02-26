import collections
import csv
from chempy.util import periodic

__all__ = ('c', 'n', 'b', 'i', 'Avo', 'Avosig', 'Avofull', 'Avofullsig')


# Misc
Avo = 6.022 * 10**23
Avosig = 6.022
Avofull = 6.02214076 * 10**23
Avofullsig = 6.02214076

# Atomic Weights
# Best references I found were
# IUPAC (International Union of Pure and Applied Chemistry) and its
# CIAAW (Commission on Isotopic Abundances and Atomic Weights)
# https://www.ciaaw.org/atomic-weights.htm
# https://iupac.org/tag/atomic-weights/
# https://iupac.org/standard-atomic-weights-of-three-technology-critical-elements-revised/
# https://www.degruyterbrill.com/document/doi/10.1515/pac-2019-0603/html


# Atomic weights from the chempy package.
# https://github.com/bjodah/chempy/blob/master/chempy/util/periodic.py
# https://en.wikipedia.org/wiki/Standard_atomic_weight#List_of_atomic_weights

chempyAtomicWeightsList = [ (periodic.symbols[n], periodic.relative_atomic_masses[n]) for n in range(118) ]

# See comments down in openstax atomic weights section for how this works.
(symbols, weights) = zip(*chempyAtomicWeightsList)
chempyWeightsType = collections.namedtuple('chempyWeightsType', symbols, defaults=weights)
c = chempyWeightsType()


# Atomic weights downloaded from NIH PubChem
# https://pubchem.ncbi.nlm.nih.gov/periodic-table/
with open('PubChemElements_all.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    nihAtomicWeightsList = [ (row['Symbol'], float(row['AtomicMass'])) for row in reader ]
(symbols, weights) = zip(*nihAtomicWeightsList)
nihWeightsType = collections.namedtuple('nihWeightsType', symbols, defaults=weights)
n = nihWeightsType()


# Some atomic weights from Appendix A periodic table in OpenStax Chem 2e.
openstaxAtomicWeightsTuple = (
        ('H', 1.008),
        ('He', 4.003),
        ('Li', 6.94),
        ('Be', 9.012),
        ('B', 10.81),
        ('C', 12.01),
        ('N', 14.01),
        ('O', 16.00),
        ('F', 19.00),
        ('Ne', 20.18),
        ('Na', 22.99),
        ('Mg', 24.31),
        ('Al', 26.98),
        ('Si', 28.09),
        ('P', 30.97),
        ('S', 32.06),
        ('Cl', 35.45),
        ('Ar', 39.95),
        ('K', 39.10),
        ('Ca', 40.08),
        ('Sc', 44.96),
        ('Ti', 47.87),
        ('V', 50.94),
        ('Cr', 52.00),
        ('Mn', 54.94),
        ('Fe', 55.85),
        ('Co', 58.93),
        ('Ni', 58.69),
        ('Cu', 63.55),
        ('Zn', 65.38),
        ('Ga', 69.72),
        ('Ge', 72.63),
        ('As', 74.92),
        ('Se', 78.97),
        ('Br', 79.90),
        ('Kr', 83.80),
        ('Rb', 85.47),
        ('Sr', 87.62),
        ('Y', 88.91),
        ('Zr', 91.22),
        ('Nb', 92.91),
        ('Mo', 95.95),

        ('Ag', 107.9),

        ('Sn', 118.7),

        ('I', 126.9),
        ('Xe', 131.3),
        ('Cs', 132.9),
        ('Ba', 137.3),

        ('La', 138.9),
        ('Ce', 140.1),
        ('Pr', 140.9),
        ('Nd', 144.2),

        ('W', 183.8),

        ('r', 192.2),
        ('Pt', 195.1),
        ('Au', 197.0),
        ('Hg', 200.6),
        ('Tl', 204.4),
        ('Pb', 207.2),
        ('Bi', 209.0),

        ('Th', 232.0),
        ('Pa', 231.0),
        ('U', 238.0),
    )

# Essentially unzip (*) and rezip but like (('H', 'He', ...), (1.008, 4.003, ...))
(symbols, weights) = zip(*openstaxAtomicWeightsTuple)
BookWeightsType = collections.namedtuple('BookWeightsType', symbols, defaults=weights)
b = BookWeightsType()


# Some atomic weights from IUPAC Periodic table 4 May 2022.
# This is from their periodic table PDF, not their detailed data set or papers.
iupacAtomicWeightsTuple = (
        ('H', 1.0080),
        ('He', 4.0026),
        ('Li', 6.94),
        ('Be', 9.0122),
        ('B', 10.81),
        ('C', 12.011),
        ('N', 14.007),
        ('O', 15.999),
        ('F', 18.998),
        ('Ne', 20.180),
        ('Na', 22.990),
        ('Mg', 24.305),
        ('Al', 26.982),
        ('Si', 28.085),
        ('P', 30.974),
        ('S', 32.06),
        ('Cl', 35.45),
        ('Ar', 39.95),
        ('K', 39.098),
        ('Ca', 40.078),
        ('Sc', 44.956),
        ('Ti', 47.867),
        ('V', 50.942),
        ('Cr', 51.996),
        ('Mn', 54.938),
        ('Fe', 55.845),
        ('Co', 58.993),
        ('Ni', 58.693),
        ('Cu', 63.546),
        ('Zn', 65.38),
        ('Ga', 69.723),
        ('Ge', 72.630),
        ('As', 74.922),
        ('Se', 78.971),
        ('Br', 79.904),
        ('Kr', 83.798),
        ('Rb', 85.468),
        ('Sr', 87.62),
        ('Y', 88.906),
        ('Zr', 91.224),
        ('Nb', 92.906),
        ('Mo', 95.95),

        ('Ag', 107.87),

        ('Sn', 118.71),

        ('I', 126.90),
        ('Xe', 131.29),
        ('Cs', 132.91),
        ('Ba', 137.33),

        ('La', 138.91),
        ('Ce', 140.12),
        ('Pr', 140.91),
        ('Nd', 144.24),

        ('W', 183.84),

        ('Ir', 192.22),
        ('Pt', 195.08),
        ('Au', 196.97),
        ('Hg', 200.59),
        ('Tl', 204.38),
        ('Pb', 207.2),
        ('Bi', 208.98),

        ('Th', 232.04),
        ('Pa', 231.04),
        ('U', 238.03),
    )

(symbols, weights) = zip(*iupacAtomicWeightsTuple)
IUPACWeightsType = collections.namedtuple('UPACWeightsType', symbols, defaults=weights)
i = IUPACWeightsType()


# Some atomic weights from Appendix A periodic table in OpenStax Chem 2e
# H = 1.008
# He = 4.003
# Li = 6.94
# Be = 9.012
# Bo = 10.81
# C = 12.01
# N = 14.01
# O = 16.00
# F = 19.00
# Ne = 20.18
# Na = 22.99
# Mg = 24.31
# Al = 26.98
# Si = 28.09
# P = 30.97
# S = 32.06
# Cl = 35.45
# Ar = 39.95
# K = 39.10
# Ca = 40.08
# Sc = 44.96
# Ti = 47.87
# V = 50.94
# Cr = 52.00
# Mn = 54.94
# Fe = 55.85
# Co = 58.93
# Ni = 58.69
# Cu = 63.55
# Zn = 65.38
# Ga = 69.72
#
# Br = 79.90
# Kr = 83.80
# Rb = 85.47
# Sr = 87.62
# Y = 88.91
# Zr = 91.22
#
# Ag = 107.9
#
# Sn = 118.7
#
# I = 126.9
# Xe = 131.3
# Cs = 132.9
# Ba = 137.3
#
# Ce = 140.1
#
# Ir = 192.2
# Pt = 195.1
# Au = 197.0
# Hg = 200.6
#
# Pb = 207.2


# Some atomic weights from IUPAC Periodic table 4 May 2022

# iH = 1.0080
# iLi = 6.94
# iBe = 9.0122
# iB = 10.81
# iC = 12.011
# iN = 14.007
# iO = 15.999
# iF = 18.998
# iNe = 20.180
# iNa = 22.990
# iMg = 24.305
# iAl = 26.982
# iSi = 28.085
# iP = 30.974
# iS = 32.06
# iCl = 35.45
# iAr = 39.95
# iK = 39.098
# iCa = 40.078
# iSc = 44.956
# iTi = 47.867
#
# iFe = 55.845
# iCo = 58.993
# iNi = 58.693
# iCu = 63.546
# iZn = 65.38
#
# iBr = 79.904
# iKr = 83.798
#
# iSe = 78.791
#
# iAg = 107.87
#
# iSn = 118.71
#
# iI = 126.90
#
# iBa = 137.33
#
# iIr = 192.22
# iPt = 195.08
# iAu = 196.97
# iHg = 200.59
#
# iPb = 207.2

