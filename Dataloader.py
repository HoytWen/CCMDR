import numpy as np 
import pandas as pd
from random import sample
import scipy 
from scipy.sparse import csr_matrix

def Intersection(nums1, nums2):
	return list(set(nums1) & set(nums2))


def compare(DU, T1, T2='NO'):
	DD = []
	if type(DU) == pd.Series:
		Time = DU['Use Time']
		if T2 == 'NO':
			if T1 >= Time:
				DD.append(DU['GeneName'])
		else:
			if T1 < Time and T2 >= Time:
				DD.append(DU['GeneName'])

	else:
		if T2 == 'NO':
			DU = DU[(DU['Use Time'] <= T1)]
			DD = DU['GeneName']
			if type(DD) == str:
				DD = DD.split('|')
			else:
				DD = DD.tolist()
		else:
			DU = DU[(DU['Use Time'] > T1) & (DU['Use Time'] <= T2)]
			DD = DU['GeneName']
			if type(DD) == str:
				DD = DD.split('|')
			else:
				DD = DD.tolist()

	return DD




##### Load dataset 
TestName = 'UREA_NITROGEN_test'
TestName = TestName[:-5]


LabTest = pd.read_csv('Patient_LabTest_Information.csv')
LabTest.set_index(['Patient ID'], inplace=True)
LabTest = LabTest[LabTest['Lab Name']==TestName]
Drug = pd.read_csv('GENNME_STAT_mapped.csv')
DrugUse = pd.read_csv('Patient_Prescription_Information.csv')
DrugUse.set_index(["Patient ID"], inplace=True)


##### Encode the gene name of drug
DrugList = list(Drug['GeneName'])
DrugNum = len(DrugList)

####### Turnn Drug to ID
DrugDict = {}
next_id = 0
for x in DrugList:
	DrugDict[x] = next_id
	next_id += 1


############## Drug embedding 
def Embedding(BatchList, DN = DrugNum):
	BatchNum = len(BatchList)
	X =  np.zeros((BatchNum, DN))

	for i in range(BatchNum):
		if not BatchList[i]:
			continue
		for d in BatchList[i]:
			X[i, DrugDict[d]] = 1.0

	return X 


##### Extract the patient ID 
PID1 = LabTest.index.tolist()
PID2 = DrugUse.index.tolist()
# PID1 = pd.value_counts(PID1).to_frame()
# PID1 = PID1.index.tolist()

PID = Intersection(PID1, PID2)
PID.sort()

LabTest  = LabTest.loc[PID]
DrugUse = DrugUse.loc[PID]


TestTime = {}

for pi in PID:
	TestTime[pi] = []
	TS = LabTest.loc[pi]['Test Time']
	if type(TS) == str:
		TestTime[pi].append(TS)
	else:
		TestTime[pi] = TestTime[pi] + TS.tolist()

X = []
for item in TestTime.items():
	DT = DrugUse.loc[item[0]]
	
	for i in range(len(item[1])):
		if i == 0:
			t1 = item[1][i]
			dd = compare(DT, t1)	
		else:
			t1 = item[1][i-1]
			t2 = item[1][i]
			dd = compare(DT, t1, t2)
		dd = list(set(dd))
		X.append(dd)
	
X = Embedding(X)
	

DF_X = pd.DataFrame(X, index=LabTest.index, columns=DrugList)
DF_X.to_csv('X/Encodding_X_'+TestName+'.csv')

LabTest.to_csv('LabTest/'+TestName+'_test.csv')





