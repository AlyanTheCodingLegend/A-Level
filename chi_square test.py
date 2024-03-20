import numpy as np
from scipy.stats import chi2
from scipy.stats import chi2_contingency
from scipy.stats import binom
from scipy.stats import chi2
import scipy.integrate as spi
import math
from scipy.stats import poisson


def goofy_func():
    print("Press -1 if you want to stop inputting values.")
    freq=0
    array=[]
    while freq != -1:
        freq=int(input("Please input observed frequency: "))
        if freq!=-1:
            array.append(freq)

    array=np.array(array)

    pvalue=float(input("Please specify the significance level of this test: "))
    degoffreedom=len(array)-1

    critical_chi2=chi2.ppf(1-pvalue,degoffreedom)

def f(x):
    return (3/(x**2))

def observed_table():
    try:
        col=int(input("Please enter the amount of columns: "))
        row=int(input("Please enter the amount of rows: "))
        print("Press -1 if you want to stop inputting values.")
        freq=0
        obs_array=[[int for i in range(col)] for j in range(row)]
        for rows in range(row):
            for columns in range(col):
                obs_array[rows][columns]=int(input(f"Please enter the observed frequency for row: {rows+1} and column: {columns+1}:  "))
        obs_array=np.array(obs_array)
        return obs_array,row,col
    except TypeError:
        print("Please enter an integer.\nPlease try again")

def contingency_table_func(observed):
    row_sums=np.sum(observed, axis=1)
    col_sums=np.sum(observed, axis=0)
    total_sum=np.sum(row_sums)
    expected_array=np.outer(row_sums,col_sums)/total_sum
    return expected_array

def chisquareval(observed,row,col):    
    pvalue=float(input("Please specify the significance level of this test: "))   
    dof=(row-1)*(col-1)
    #contingency_table = contingency_table_func(observed)
    test_chi2,temp,dof,expected=chi2_contingency(observed)
    critical_chi2=chi2.ppf(1-pvalue,dof)
    print(f"The test statistic is: {test_chi2}")
    print(f"The critical statistic is: {critical_chi2}")

#obs_array,row,col=observed_table()
#chisquareval(obs_array,row,col)

#expected=calculate_expected(array)
#observed_chi2=np.sum((array-expected)**2/expected)

#print("Chi-Square Test Value: ",observed_chi2)
#print("Chi-Square Critical Value: ",critical_chi2)

#observed_table()


def calculate_expected(observed):
    expected=[]
    total_obs=sum(observed)
    for i in range(len(observed)):
        upp_lim=int(input(f"Please enter upper limit for this observed value {observed[i]}: "))
        low_lim=int(input(f"Please enter lower limit for this observed value {observed[i]}: "))
        expectedval,error=spi.quad(f,low_lim,upp_lim)
        expectedval=expectedval*total_obs
        expected.append(expectedval)
    expected=np.array(expected)
    return expected

def goodness_binomial(observed,expected):
    observed = np.array(observed)
    expected = np.array(expected)
    correction = np.where(expected < 5, 0.5, 0)
    observed_freq_adj = observed - correction
    expected_freq_adj = expected - correction
    chi_square = np.sum((observed_freq_adj - expected_freq_adj)**2 / expected_freq_adj)
    p_value = float(input("Enter significance level: "))
    return chi_square, p_value

def frequencies():
    observed_freq = []
    flag = True
    while flag:
        input1 = int(input("Please enter observed frequency: "))
        if input1 == -1:
            flag = False
        else:
            observed_freq.append(input1)
    n = np.sum(observed_freq)
    p = float(input("Enter probability of success value: "))
    expected_freq = [binom.pmf(k, n, p) * n for k in range(len(observed_freq))]
    dof = len(observed_freq) - 1
    return expected_freq,observed_freq,dof

#expected_freq,observed_freq,dof = frequencies()
#chi_square,p_value = goodness_binomial(observed_freq,expected_freq)
#critical_value = chi2.ppf(1 - p_value, dof)
#print("Chi-square statistic:", chi_square) #should be 7.84
#print("Critical value:", critical_value)

def discrete_dist_chi2():
    observed_freq = []
    expected_freq=[]
    upd_obs=[]
    upd_exp=[]
    test_statistic_chi2=0.0
    flag = True
    distribution=(input("What distribution are we testing upon?: ")).lower()
    if distribution=="binomial":
        success_prob=float(input("Please enter probability of success: "))
    elif distribution=="poisson":
        average=float(input("Please enter average rate: "))
    elif distribution=="uniform":
        pass
    elif distribution=="non-uniform":
        pass
    else:
        print("Invalid distribution!")
        return
    print("Please enter -1 when you want to stop entering observed frequencies!")
    while flag:
        input1 = int(input("Please enter observed frequency: "))
        if input1 == -1:
            flag = False
        else:
            observed_freq.append(input1)
    total_obs=sum(observed_freq)
    n=len(observed_freq)-1
        
    sig_level=float(input("Please enter the significance level: "))
    for count in range(len(observed_freq)):
        if distribution=="binomial":
            exp_val= (math.comb(n,count))*(success_prob**count)*((1-success_prob)**(n-count))
        elif distribution=="poisson":
            exp_val= poisson.pmf(count,average)
        elif distribution=="uniform":
            exp_val=1/len(observed_freq) 
        elif distribution=="non-uniform":
            exp_val=float(input(f"Please enter the probability of {count+1}: "))       
        exp_val=exp_val*total_obs
        expected_freq.append(exp_val)

    i=0
    while i<(len(observed_freq)-1):
        count=i+1
        temp_exp=expected_freq[i]
        temp_obs=observed_freq[i]
        while temp_exp<5 or expected_freq[count]<5:
            temp_exp += expected_freq[count]
            temp_obs += observed_freq[count]
            count += 1
            if count==len(observed_freq):
                break
        i=count    
        upd_obs.append(temp_obs)
        upd_exp.append(temp_exp)
    if distribution=="binomial" or distribution=="poisson":
        estimated_parameters=int(input("How many parameters have been estimated?: "))
        dof=len(upd_exp)-1-estimated_parameters
    else:
        dof=len(upd_exp)-1    
    for i in range(len(upd_obs)):
        test_statistic_chi2 += ((upd_obs[i]-upd_exp[i])**2)/(upd_exp[i])
    critical_value_chi2=chi2.ppf(1-sig_level,dof)
    print(f"The test statistic is: {test_statistic_chi2}")
    print(f"The critical value is: {critical_value_chi2}")
    if test_statistic_chi2<critical_value_chi2:
        print("Ho is accepted.")
    else:
        print("Ho is rejected.")        

discrete_dist_chi2()