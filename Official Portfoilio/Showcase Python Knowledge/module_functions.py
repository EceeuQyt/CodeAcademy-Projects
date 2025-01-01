import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats 
import seaborn as sns

from statistics import mode, multimode, quantiles
#from math 


samp = pd.DataFrame({'sample':[range(0,50)],'sample 2':[range(0,50,2)]})
print(samp)

samp2 = pd.DataFrame({'sample':[range(0,30)],'sample 2':[range(0,30,2)]})
print(samp2)

def create_dataframe(table, x):
    if table == 'csv_txt':
        return pd.read_cvs(x)
    else: 
        return pd.Dataframe(x)

def create_rand_df(n1, n2, x, y , col1, col2, col3):
    return pd.DataFrame(np.random.randint(n1, n2, size=(x, y)), columns=[col1, col2, col3])

def create_series(li):
    return pd.Series(li)


def create_lambda(name, variable, expression):
    name = lambda variable: expression   

def fibonacci_of (n): #input range(n)
    if n in (0,1):
        return n
    return fibonacci_of(n-1) + fibonacci_of(n-2)
#fibb_sequence = [fibonacci_of(n) for n in range(35)]

def type_statistic(d, stats):
    if stats == "Mean":
        return np.mean(d)
    elif stats == "Median":
        return np.median(d)
    elif stats == 'Mode':
        return mode(d)
    elif stats == 'MultiMode':
        return multimode(d)
    elif stats == "Minimum":
        return np.min(d) 
    elif stats == "Maximum":
        return np.max(d)
    elif stats == "Sum":
        return sum(d)
    elif stats == 'Category col Count':
        return d.count()
    elif stats == 'Category Count':
        return d.nunique()
    elif stats == 'Category Unique':
        return d.unique()
    elif stats == 'STD':
        return np.std(d)
    elif stats == 'Standard Error':
        return np.std(d, ddof=1) / np.sqrt(np.size(d)) #from scipy.stats import sem /sem(d)
    elif stats == "Variance":
        return np.var(d)
    elif stats == "MAD":
        return mad(d)
    elif stats == "Sample Variance":
        return np.var(d, ddof=1)
    elif stats == "Percent":
        return np.percentile(d)
    elif stats == 'Quarter Quantiles':
        return quantiles(d, n = 4, method= 'exclusive')
# Raises error if stats is not any of the above:
    else:
        raise Exception('Are you certain you selected a Data Statistic, otherwise is it grammatically correct.')

def create_vector(array):
    return np.array([array])


def create_matrix(a,a2,a3):
    return np.array([[a], [a2], [a3]])

def merging_df(merge, df1, df2): #make dataframe that has nan or 0 to apply this
    if merge == "left":
        return pd.merge(df1, df2, how = "left")
    elif merge == "right":
        return pd.merge(df1, df2, how = "right")
    elif merge == "merge":
        return pd.merge(df1, df2)
    else:
        return pd.concat([df1,df2])

def diffential_calculus(fx, limit):
    return np.gradient(fx, limit) 

def vector_ops(type, v1, v2, constant):
    if type == 'Scalar':
        return constant*v1, constant*v2
    elif type == 'Add':
        return v1 + v2
    elif type == 'Subtract':
        return v1 - v2
    elif type == "dot product":
        return np.dot(v1,v2)
    else:
        return 'Are you sure your math and syntax are correct'
        
def matrix_ops(type, constant, m1, m2):
    if type == 'Scalar':
        return constant*m1, constant*m2
    elif type == 'Add':
        return m1 + m2
    elif type == 'Subtract':
        return m1 - m2
    elif type == 'Matrix Mul':
        return m1@m2 # np.matmul(m1,m2)
    else: 
        return 'Check your math or syntax'

def population_distribution(population_data):
    # plot the population distribution
    sns.histplot(population_data, stat='density')
    # informative title for the distribution 
    plt.title(f"General Distribution")
    # remove None label
    plt.xlabel('')
    plt.show()
    plt.clf()
    

def sampling_distribution(Data, samp_size, stat):
# list that will hold all the sample statistics
    sample_stats = []
    for i in range(500):
    # get a random sample from the population of size samp_size
        sample = np.random.choice(Data, samp_size, replace = False)
    # calculate the chosen statistic (mean, minimum, or variance) of the sample
        sample_stat = type_statistic(sample, stat)
    # add sample_stat to the sample_stats list
        sample_stats.append(sample_stat)

    pop_statistic = round(type_statistic(Data, stat),2)
    # plot the sampling distribution
    sns.histplot(sample_stats, stat='density')
    # informative title for the sampling distribution
    plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}")
    plt.axvline(pop_statistic,color='g',linestyle='dashed', label=f'Population {stat}')
    # plot the mean of the chosen sample statistic for the sampling distribution
    plt.axvline(np.mean(sample_stats),color='orange',linestyle='dashed', label=f'Mean of the Sample {stat}s')
    plt.legend()
    plt.show()
    plt.clf()
    
""""
Catagorical_summaries
nuniQue()
count()
unique()
boxplot()


Quantitive_summaries
Mean() mode(), median() and similar
histogram()
scatterplot()
"""

