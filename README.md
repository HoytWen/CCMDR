# CCMDR
Source code of paper "Clinical connectivity map for drug repurposing: using laboratory results to bridge drugs and diseases"
## 1. Introduction 

In this paper, we propose a drug repositioning framework to discover the new indications of existing drugs from electronic 
clinical information, including National Health and Nutrition Examination Survey (NHANES) and Electronic Healthy Records (EHR). 

Both of NHANES and EHR data contain the laboratory test vlaue of patients, we take the laboratory test as clinical vaibales. 
We apply Wilcoxon rank sum test (Mann Whitney U test) and Continuous Self-Controlled Case Series (CSCCS) in the drug repositioning 
framework to calculate the influence of different disease conditions and existing drugs on the same clinical variables. Finally,
we use the complementarities between them to discover the new indications of existing drugs. 


## 2. Pipline

![pipline.jpg](https://github.com/HoytWen/CCM-Drug-Repositioning/blob/master/pipline.jpg)

Fig.1 Our drug repositioning framework to infer novel indications of existing drug candidates, which includes three steps. 
(1) Establishing clinical disease effect vector for each disease conditions by applying statistical analysis(Wilcoxon rank sum test) on NHANES dateset.
(2) Establishing clinical drug effect vector for each existing drugs by applying CSCCS regression analysis on EHR dataset. 
(3) Calculating therapeutic score for each drug-disease pair to infer indications based on the complmentarity between two vectors 

## 3. Dataset

The datasets used in the paper:

+ [NHANES](https://wwwn.cdc.gov/nchs/nhanes/Default.aspx): a dataset consists of interviews, physical examinations and laboratory tests.The interviews part includes demographic, socioeconomic, dietary, and health-related questions. We use the result of the health-related question (questionnaire data) and laboratory tests (laboratory data) from 1999 to 2016. 

+ EHR: a digital paper chart for patients, which contains their medical history. We use the medication history and laboratory test result in EHR dataset. It provides real-time, patient-centered records of patients. 

+ [SIDER](http://sideeffects.embl.de): a database that contains information on marketed medicines and their recorded inidications and adverse drug reactions. 

## 4. Requirement 
- Python >= 3.6.8
- numpy >= 1.20.2
- scipy >= 1.6.3
- pandas >= 1.1.4
- scikit-learn >= 0.23.1
- regressor >= 0.0.3 

## 5. Usage
Generate the disease effects on a given laboratory test
  ```sh
  python DiseaseVector.py
  ```
 Generate the drug effects on a given laboratory test
  ```sh
  python DrugVector.py
  ```
 Calculate the drug therapy scores on the diseases
  ```sh
  python score.py
  ```
## 6. Files 
We compute effects of the diseases and drugs invloved in our experiments on selected laboratory tests, then further compute the therapy scores of drugs on the diseases. The computation results is organized in the following files.
- DiseaseEffect.csv: the effects of 6 kinds of disease on 35 laboratory tests, where +1.0 means increaseing effect and -1.0 means decreasing effect. 
- DrugEffect.csv: the effects of 392 kinds of drug on 35 laboratory tests, where positive value means increaseing effect and negative value means decreasing effect. 
- Drug2Disease.csv: the therapy scores of drugs on diseases, where positive value means the drug has therapeutic effect on the disease and negative value means the drug can not treat the disease or even worsen the siutation. 
- map.txt: mapping the laboratory test names into the NHANES code. 
