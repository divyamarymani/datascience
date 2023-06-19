## Q1 ##    a.   Cars speed and distance


import pandas as pd

cars = pd.read_csv(r"D:\Personal\Study\Data Science\Assignments\Work\08 Graphical Representation\Q1_a.csv")

cars.info()
cars.shape

#Exloratory data analysis
# to calculate mean median and mode variance standard deviation 

cars.speed.mean()   
cars.speed.median()
cars.speed.mode() 
cars.speed.var() 
cars.speed.std()
cars.speed.skew()
cars.speed.kurt()

cars.dist.mean() 
cars.dist.median() 
cars.dist.mode() 
cars.dist.var()
cars.dist.std()
cars.dist.skew() 
cars.dist.kurt()

cars.describe()

#histogram

import matplotlib.pyplot as plt 

plt.hist(cars.speed, color= 'blue')
plt.hist(cars.dist, color = 'red') 

#boxplot 

import seaborn as sns

sns.boxplot(cars.dist) 
sns.boxplot(cars.speed) 

import numpy as np

IQR = cars['dist'].quantile(.75) - cars['dist'].quantile(.25)
lower_limit = cars['dist'].quantile(.25) - 1.5 * IQR 
upper_limit = cars['dist'].quantile(.75) + 1.5 * IQR 
cars['dist'] = np.where(cars['dist'] >= upper_limit, upper_limit,cars['dist'])

sns.boxplot(cars.dist)


## b. Top Speed (SP) and Weight (WT)

import pandas as pd

top = pd.read_csv(r"D:\Personal\Study\Data Science\Assignments\Work\08 Graphical Representation\Q2_b.csv")

top.shape

top.describe()

top.info() 

#Exloratory data analysis
# to calculate mean median and mode variance standard deviation 

top.SP.mean() 
top.SP.median() 
top.SP.mode() 
top.SP.var() 
top.SP.std() 
top.SP.kurt()
top.SP.skew()

top.WT.mean() 
top.WT.median() 
top.WT.mode() 
top.WT.var()
top.WT.std()
top.WT.kurt()
top.WT.skew() 

#histogram

import matplotlib.pyplot as plt
plt.hist(top.SP, color = 'blue') 
plt.hist(top.WT, color = 'red') 

#boxplot 

import seaborn as sns
sns.boxplot(top.SP) 
sns.boxplot(top.WT)



IQR = top['SP'].quantile(.75) - top['SP'].quantile(.25)
upper_limit = top['SP'].quantile(.75) + 1.5 * IQR 
upper_limit
top['SP'] = np.where(top['SP'] >= upper_limit, upper_limit,top['SP']) 


sns.boxplot(top.SP)  

IQR = top['WT'].quantile(.75) - top['WT'].quantile(.25)
upper_limit = top['WT'].quantile(.75) + 1.5 * IQR 
lower_limit = top['WT'].quantile(.25) - 1.5 * IQR

top['WT'] = np.where(top['WT'] >= upper_limit, upper_limit,top['WT'])
top['WT'] = np.where(top['WT']<= lower_limit,lower_limit,top['WT'])

sns.boxplot(top.WT)



##### Q3 34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56
#1) Find mean, median, variance, standard deviation.
#2) What can we say about the student marks? [Hint: Looking at the various measures calculated above whether the data is normal/skewed or if outliers are present].

import pandas as pd

a = [34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]
b = pd.DataFrame(a)

b.info()

b.describe()
b.mean()
b.mode() 
b.median() 
b.var() 
b.std() 
b.skew() 
b.kurt() 

import matplotlib.pyplot as plt

plt.hist(b) 

import seaborn as sns 

sns.boxplot(b[0])














