import numpy as np
import pandas as pd
import os

DiseaseEffect = pd.read_csv('DiseaseEffect.csv', low_memory=False)
DiseaseEffect.set_index(['Disease Name'], inplace=True)
DrugEffect = pd.read_csv('DrugEffect3.csv', low_memory=False)
DrugEffect.set_index(['Generic Name'], inplace=True)

LabName = list(DiseaseEffect)
threshold = 1.0


def ComputeScore(DiV, DrV):
	effect = 0
	for lab in LabName:
		DrE = DrV.loc[lab]
		if DrE !=0:
			DrE = DrE/abs(DrE)
		DiE = DiV.loc[lab]

		# effect = effect + DrE*DiE

		if (DiE==1.0 and DrE==-1.0) or (DiE==-1.0 and DrE==1.0):
			effect = effect + 1.0
		# elif (DiE==1.0 and DrE==1.0) or (DiE==-1.0 and DrE==-1.0):
		# 	effect = effect + 1.0
		# elif (DiE==0.0 and DrE==1.0) or (DiE==0.0 and DrE==-1.0):
		# 	effect = effect + 0.5

	return effect


DiseaseName = DiseaseEffect.index.tolist()
DiseaseName.sort()
DrugName = DrugEffect.index.tolist()
DrugName.sort()

score = []

for din in DiseaseName:
	s = []
	DiseaseVector = DiseaseEffect.loc[din]
	for drn in DrugName:
		DrugVector = DrugEffect.loc[drn]
		e = ComputeScore(DiseaseVector, DrugVector)
		s.append(e)

	score.append(s)

score = np.array(score).transpose()

score = pd.DataFrame(score, index=DrugName, columns=DiseaseName)

score.index.name = 'Generic Name'

score.to_csv('Drug2Disease5.csv')






