import collections
import csv
from decimal import *
from chempy.util import periodic

__all__ = ('c', 'n', 'b', 'i', 'Avo', 'Avosig', 'Avofull', 'Avofullsig')


# Misc
Avosig = Decimal('6.022')
Avo = Avosig * Decimal('10') ** Decimal('23')
Avofullsig = Decimal('6.02214076')
Avofull = Avofullsig * Decimal('10') ** Decimal('23')

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
(symbols, weights) = (symbols, map(lambda w: Decimal(str(w)), weights)) # The str() avoids false floating values.
chempyWeightsType = collections.namedtuple('chempyWeightsType', symbols, defaults=weights)
c = chempyWeightsType()


# Atomic weights downloaded from NIH PubChem
# https://pubchem.ncbi.nlm.nih.gov/periodic-table/
with open('PubChemElements_all.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    nihAtomicWeightsList = [ (row['Symbol'], Decimal(row['AtomicMass'])) for row in reader ]
(symbols, weights) = zip(*nihAtomicWeightsList)
nihWeightsType = collections.namedtuple('nihWeightsType', symbols, defaults=weights)
n = nihWeightsType()


# Some atomic weights from Appendix A periodic table in OpenStax Chem 2e.
openstaxAtomicWeightsTuple = (
        ('H', Decimal('1.008')),
        ('He', Decimal('4.003')),
        ('Li', Decimal('6.94')),
        ('Be', Decimal('9.012')),
        ('B', Decimal('10.81')),
        ('C', Decimal('12.01')),
        ('N', Decimal('14.01')),
        ('O', Decimal('16.00')),
        ('F', Decimal('19.00')),
        ('Ne', Decimal('20.18')),
        ('Na', Decimal('22.99')),
        ('Mg', Decimal('24.31')),
        ('Al', Decimal('26.98')),
        ('Si', Decimal('28.09')),
        ('P', Decimal('30.97')),
        ('S', Decimal('32.06')),
        ('Cl', Decimal('35.45')),
        ('Ar', Decimal('39.95')),
        ('K', Decimal('39.10')),
        ('Ca', Decimal('40.08')),
        ('Sc', Decimal('44.96')),
        ('Ti', Decimal('47.87')),
        ('V', Decimal('50.94')),
        ('Cr', Decimal('52.00')),
        ('Mn', Decimal('54.94')),
        ('Fe', Decimal('55.85')),
        ('Co', Decimal('58.93')),
        ('Ni', Decimal('58.69')),
        ('Cu', Decimal('63.55')),
        ('Zn', Decimal('65.38')),
        ('Ga', Decimal('69.72')),
        ('Ge', Decimal('72.63')),
        ('As', Decimal('74.92')),
        ('Se', Decimal('78.97')),
        ('Br', Decimal('79.90')),
        ('Kr', Decimal('83.80')),
        ('Rb', Decimal('85.47')),
        ('Sr', Decimal('87.62')),
        ('Y', Decimal('88.91')),
        ('Zr', Decimal('91.22')),
        ('Nb', Decimal('92.91')),
        ('Mo', Decimal('95.95')),

        ('Ag', Decimal('107.9')),

        ('Sn', Decimal('118.7')),

        ('I', Decimal('126.9')),
        ('Xe', Decimal('131.3')),
        ('Cs', Decimal('132.9')),
        ('Ba', Decimal('137.3')),

        ('La', Decimal('138.9')),
        ('Ce', Decimal('140.1')),
        ('Pr', Decimal('140.9')),
        ('Nd', Decimal('144.2')),

        ('W', Decimal('183.8')),

        ('r', Decimal('192.2')),
        ('Pt', Decimal('195.1')),
        ('Au', Decimal('197.0')),
        ('Hg', Decimal('200.6')),
        ('Tl', Decimal('204.4')),
        ('Pb', Decimal('207.2')),
        ('Bi', Decimal('209.0')),

        ('Th', Decimal('232.0')),
        ('Pa', Decimal('231.0')),
        ('U', Decimal('238.0')),
    )

# Essentially unzip (*) and rezip but like (('H', 'He', ...), (1.008, 4.003, ...))
(symbols, weights) = zip(*openstaxAtomicWeightsTuple)
BookWeightsType = collections.namedtuple('BookWeightsType', symbols, defaults=weights)
b = BookWeightsType()


# Some atomic weights from IUPAC Periodic table 4 May 2022.
# This is from their periodic table PDF, not their detailed data set or papers.
iupacAtomicWeightsTuple = (
        ('H', Decimal('1.0080')),
        ('He', Decimal('4.0026')),
        ('Li', Decimal('6.94')),
        ('Be', Decimal('9.0122')),
        ('B', Decimal('10.81')),
        ('C', Decimal('12.011')),
        ('N', Decimal('14.007')),
        ('O', Decimal('15.999')),
        ('F', Decimal('18.998')),
        ('Ne', Decimal('20.180')),
        ('Na', Decimal('22.990')),
        ('Mg', Decimal('24.305')),
        ('Al', Decimal('26.982')),
        ('Si', Decimal('28.085')),
        ('P', Decimal('30.974')),
        ('S', Decimal('32.06')),
        ('Cl', Decimal('35.45')),
        ('Ar', Decimal('39.95')),
        ('K', Decimal('39.098')),
        ('Ca', Decimal('40.078')),
        ('Sc', Decimal('44.956')),
        ('Ti', Decimal('47.867')),
        ('V', Decimal('50.942')),
        ('Cr', Decimal('51.996')),
        ('Mn', Decimal('54.938')),
        ('Fe', Decimal('55.845')),
        ('Co', Decimal('58.993')),
        ('Ni', Decimal('58.693')),
        ('Cu', Decimal('63.546')),
        ('Zn', Decimal('65.38')),
        ('Ga', Decimal('69.723')),
        ('Ge', Decimal('72.630')),
        ('As', Decimal('74.922')),
        ('Se', Decimal('78.971')),
        ('Br', Decimal('79.904')),
        ('Kr', Decimal('83.798')),
        ('Rb', Decimal('85.468')),
        ('Sr', Decimal('87.62')),
        ('Y', Decimal('88.906')),
        ('Zr', Decimal('91.224')),
        ('Nb', Decimal('92.906')),
        ('Mo', Decimal('95.95')),

        ('Ag', Decimal('107.87')),

        ('Sn', Decimal('118.71')),

        ('I', Decimal('126.90')),
        ('Xe', Decimal('131.29')),
        ('Cs', Decimal('132.91')),
        ('Ba', Decimal('137.33')),

        ('La', Decimal('138.91')),
        ('Ce', Decimal('140.12')),
        ('Pr', Decimal('140.91')),
        ('Nd', Decimal('144.24')),

        ('W', Decimal('183.84')),

        ('Ir', Decimal('192.22')),
        ('Pt', Decimal('195.08')),
        ('Au', Decimal('196.97')),
        ('Hg', Decimal('200.59')),
        ('Tl', Decimal('204.38')),
        ('Pb', Decimal('207.2')),
        ('Bi', Decimal('208.98')),

        ('Th', Decimal('232.04')),
        ('Pa', Decimal('231.04')),
        ('U', Decimal('238.03')),
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

