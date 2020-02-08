import csv
import os
import numpy as np
import pandas as pd
from scipy import stats

def intersection(nums1, nums2):
	return list(set(nums1) & set(nums2))

disease_file = 'Questionnaire_combined.csv'
lab_file = 'Laboratory_combined.csv'

DCode = 'MCQ160M'

labtest = 'map.txt'
DiseaseDict = {}

with open(labtest, 'r') as f:
	rows = f.readlines()
	rows = [row.strip() for row in rows]

for x in rows:
	x = x.split(',')
	DiseaseDict[x[1][1:]] = x[0]

QD = pd.read_csv(disease_file)
QD = QD.fillna(value= 'NONE')
QD.set_index(['SEQN'], inplace=True)

# DG = QD[(QD['DIQ010'] == 1.0) | (QD['DIQ160'] == 1.0)]
DG = QD[QD[DCode] == 1.0]
DG = DG.index.tolist()

# HG = QD[(QD['DIQ010'] == 2.0) & (QD['DIQ160'] != 1.0)]
HG = QD[QD[DCode] == 2.0]
HG = HG.index.tolist()

LD = pd.read_csv(lab_file)
LD = LD.fillna(value = 'NONE')
LD.set_index(['SEQN'], inplace=True)

indexs = list(LD)
effect = []
LabName = []


for ind in indexs:

	LabName.append(DiseaseDict[ind])
	LG = LD[~LD[ind].isin(['NONE'])]
	LG = LG.index.tolist()

	DID = intersection(DG, LG)
	DID.sort()
	HID = intersection(HG, LG)
	HID.sort()

	DD = LD.loc[DID][ind].tolist()
	HD = LD.loc[HID][ind].tolist()

	P_ava = sum(DD)/len(DD)
	H_ava = sum(HD)/len(HD)

	relation = 0
	res1 = stats.mannwhitneyu(DD, HD, alternative='less')
	if res1[1] <= 0.01:
		relation = '-'


	res2 = stats.mannwhitneyu(DD, HD, alternative='greater')
	if res2[1] <= 0.01:
		relation = '+'

	effect.append(relation)



DiseaseEffect = pd.DataFrame(effect, index=LabName, columns=['Disease Effect'])
DiseaseEffect.to_csv('Result/Disease2Thyroid.csv')






