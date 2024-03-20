import math
from scipy.stats import chi2
from scipy.stats import poisson

def poisson_chi2():
    observed_freq = []
    expected_freq=[]
    upd_obs=[]
    upd_exp=[]
    test_statistic_chi2=0.0
    flag = True
    while flag:
        input1 = int(input("Please enter observed frequency: "))
        if input1 == -1:
            flag = False
        else:
            observed_freq.append(input1)
    #observed_freq=np.array(observed_freq)
    total_obs=sum(observed_freq)
    n=len(observed_freq)-1
    average=float(input("Please enter average rate: "))
    sig_level=float(input("Please enter the significance level: "))
    for count in range(len(observed_freq)):
        exp_val= poisson.pmf(count,average)
        exp_val=exp_val*total_obs
        expected_freq.append(exp_val)
    #expected_freq=np.array(expected_freq)
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
    #upd_obs=np.array(upd_obs)
    #upd_exp=np.array(upd_exp)
    n=len(upd_obs)-1
    for i in range(len(upd_obs)):
        test_statistic_chi2 += ((upd_obs[i]-upd_exp[i])**2)/(upd_exp[i])
    critical_value_chi2=chi2.ppf(1-sig_level,n)
    print(f"The test statistic is: {test_statistic_chi2}")
    print(f"The critical value is: {critical_value_chi2}")    

poisson_chi2()    