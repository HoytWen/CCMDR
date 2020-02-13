# Clinical Connectivity Mapping For Drug Repositioning
## 1. Introduction 
This repository contains source code for paper “”

In this paper, we propose a drug repositioning framework to discover the new indications of existing drugs from electronic 
clinical information, including National Health and Nutrition Examination Survey (NHANES) and Electronic Healthy Records (EHR). 

Both of NHANES and EHR data contain the laboratory test vlaue of patients, we take the laboratory test as clinical vaibales. 
We apply Wilcoxon rank sum test (Mann Whitney U test) and Continuous Self-Controlled Case Series (CSCCS) in the drug repositioning 
framework to calculate the influence of different disease conditions and existing drugs on the same clinical variables. Finally,
we use the complementarities between them to discover the new indications of existing drugs. 


## 2.Pipline

![pipline.jpg](https://github.com/HoytWen/CCM-Drug-Repositioning/blob/master/pipline.jpg)

Fig.1 Our drug repositioning framework to infer new uses of existing drug candidates, which includes three steps. 
(1) Establishing clinical disease effect vector for each disease conditions by applying statistical analysis(Wilcoxon rank sum test) on NHANES dateset.
(2) Establishing clinical drug effect vector for each existing drugs by applying CSCCS regression analysis on EHR dataset. 
(3) Calculating therapeutic score for each drug-disease pair to infer indications based on the complmentarity between two vectors 
