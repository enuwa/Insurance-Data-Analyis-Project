#Data Analytics with Python
#Insurance Data Analysis


#Steps to Be Followed
#1.Import libraries such as Pandas, matplotlib, NumPy, and seaborn and load the insurance dataset
#2.Check the shape of the data along with the data types of the column
#3.Check missing values in the dataset and find the appropriate measures to fill in the missing values
#4.Explore the relationship between the feature and target column using a count plot of categorical columns and a scatter plot of numerical columns
#5.Perform data visualization using plots of feature vs feature
#6.Check if the number of premium charges for smokers or non-smokers is increasing as they are aging
#7.After each step, specify the observations.

#1.Import libraries such as Pandas, matplotlib, NumPy, and seaborn and load the insurance dataset.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("insurance.csv")

df = data
df

#2. Checking the chape the dataset. Observation: there are 1338 rows, 7 columns in the insurance dataset
data.shape  
data.info() # Checking the data types of the columns. Observation:  There are int64 == (4), object == (3) dtypes

# 3.Check missing values in the dataset and find the appropriate measures to fill in the missing values
data.isna().sum()

# 4.Explore the relationship between the features and target column
#using a count plot of categorical columns and a scatter plot of numerical columns


#count plot for categorical columns : smoker,sex--- charges
plt.figure(figsize=(6,4))
sns.countplot(x="smoker",data=data)
plt.title("count of smokers and non-smokers")
plt.xlabel("smoker")
plt.ylabel("count")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="region",data=data,hue="smoker")
plt.title("count of smokers and non-smokers")
plt.xlabel("smoker")
plt.ylabel("count")
plt.show()

sns.scatterplot(x="age", y='charges', data=data)

sns.scatterplot(x="children", y='charges', data=data)
#Observation
#Age vs charges: There is a noticeable upward trend; charges tend to increase with age, especially for older people.

#BMI vs charges: A slight upward trend can be seen, but it’s not very strong. Some high charges appear at higher BMI levels.

#Children vs charges: No clear correlation between number of children and charges.

# 5. Perform data visualization using plots of feature vs feature

fig, axs = plt.subplots(2, 3, figsize=(18, 10))
sns.scatterplot(x="age", y="bmi", hue="smoker", data=data, ax=axs[0, 0])
axs[0, 0].set_title("Age vs BMI")
sns.scatterplot(x="age", y="children", hue="smoker", data=data, ax=axs[0, 1])
axs[0, 1].set_title("Age vs Children")
sns.scatterplot(x="age", y="charges", hue="smoker", data=data, ax=axs[0, 2])
axs[0, 2].set_title("Age vs Charges")
sns.scatterplot(x="bmi", y="children", hue="smoker", data=data, ax=axs[1, 0])
axs[1, 0].set_title("BMI vs Children")
sns.scatterplot(x="bmi", y="charges", hue="smoker", data=data, ax=axs[1, 1])
axs[1, 1].set_title("BMI vs Charges")
sns.scatterplot(x="children", y="charges", hue="smoker", data=data, ax=axs[1, 2])
axs[1, 2].set_title("Children vs Charges")
plt.tight_layout()

#Observation
#Age vs Charges: Charges increase significantly with age, especially for smokers. A clear upward trend is visible for smokers, indicating a strong age-related risk factor.
#BMI vs Charges: Some smokers with high BMI are charged significantly more, but the correlation is weaker than with age.

#Children vs Charges: No clear pattern; the number of children has little visible effect on charges.

#Age vs BMI / Children: No strong relationship—BMI and number of children appear fairly independent of age.

#BMI vs Children: Again, little to no trend here.

#6. Check if the number of premium charges for smokers or non-smokers is increasing as they are ageing.
plt.figure(figsize=(10,10))
sns.lineplot(data=data,x="age", y ="charges" , hue="smoker",estimator="mean")
plt.title("Average insurance charges vs age by smoking status")
plt.xlabel("Age")
plt.ylabel("Average Charges")
plt.grid(True)

# Observation
#For a smoker, charges rise steeply with age, especially after age 30. This suggests an accelerating cost with age for smokers. 

#Non-smokers' charges also increase with age, but at a much lower rate than you know and more gradually.

#Summary:  this confirms there is a strong age related rise in premium cost, significantly pronounced for smokers after age 30
plt.show()