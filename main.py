import pandas as pd
import numpy as np
import openpyxl

dataFrame = pd.read_excel("27-SalarySheet.xlsx")
my_data_frame = pd.DataFrame(dataFrame)

#1) Toplamda kaç satır veri vardır?
print("Q1) Number of row : ",(my_data_frame.shape[0]))

#2) Bu firma ortalama ne kadar maaş vermektedir?
print("Q2) Avarage Salary : ",dataFrame["Salary"].mean())

#3) Bu firmada departmanlara göre ortalama maaş karşılaştırması nasıldır?
print("Q3) Compare avarage salary according to department :\n",dataFrame.groupby("Department")["Salary"].mean())

#4) Bu firmada title (senior - junior) durumuna göre ortalama maaş karşılaştırması nasıldır?
print("Q4) Compare avarage salary according to senior-junior :")
print("Avarage Senior : ",round(dataFrame[dataFrame["Title"] == "Senior"]["Salary"].mean(),2))
print("Avarage Junior : ",round(dataFrame[dataFrame["Title"] == "Junior"]["Salary"].mean(),2))

#5) Senior bir kişinin junior bir kişiye göre maaşı ortalama yüzde kaç fazladır?
senior_avarage = dataFrame[dataFrame["Title"] == "Senior"]["Salary"].mean()
junior_avarage = dataFrame[dataFrame["Title"] == "Junior"]["Salary"].mean()
ratio = (senior_avarage-junior_avarage)*100/junior_avarage
print(f"Q5) The average salary of a senior person is {round(ratio,2)} percent higher than a junior person")

#6) Software development departmanında senior bir kişinin junior bir kişiye göre maaşı ortalama ne kadar fazladır?
filtre1 = (dataFrame["Department"] == "Software Development") & (dataFrame["Title"] == "Senior")
ort_senior = dataFrame.loc[filtre1,"Salary"].mean()
filtre2 = (dataFrame["Department"] == "Software Development") & (dataFrame["Title"] == "Junior")
ort_junior = dataFrame.loc[filtre2,"Salary"].mean()
print(f"Q6) The average salary of a senior person in the software development department is {round(ort_senior-ort_junior,2)} more than a junior person.")

#7) Finance departmanında c-level bir kişinin mid-senior bir kişiye göre maaşı ortalama ne kadar fazladır?
filtre1 = (dataFrame["Department"] == "Finance") & (dataFrame["Title"] == "C-level")
ort_clevel = dataFrame.loc[filtre1,"Salary"].mean()
filtre2 = (dataFrame["Department"] == "Finance") & (dataFrame["Title"] == "Mid-Senior")
ort_midsenior = dataFrame.loc[filtre2,"Salary"].mean()
print(f"Q7) In the finance department, a c-level person earns an average of {round(ort_clevel-ort_midsenior)} more than a mid-senior person.")

#8) Software development departmanında c-level çalışan sayısı marketing departmanında çalışana oranla kaç kat fazladır?
filtre1 = (dataFrame["Department"] == "Software Development") & (dataFrame["Title"] == "C-level")
ort_clevel_sayısı = dataFrame[filtre1].count()
ort_marketing_sayısı = dataFrame[dataFrame["Department"] == "Marketing"].count()
a = ort_clevel_sayısı[0]
b = ort_marketing_sayısı[0]
print(f"Q8) The number of c-level employees in the software development department is {round((b-a)/a,2)} times higher than the number of employees in the marketing department")

