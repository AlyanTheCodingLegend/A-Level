import scipy.stats as stats

def value_inputting():
    data_inp_type=(input("Are the data values going to be inputted individually or is the sum going to be inputted?: ")).lower()
    #type = individual or sum
    sig_level=float(input("Please input the significance level: "))
    test_tail=int(input("Please input 1 if test is one-tailed or 2 if test is two-tailed: "))
    if data_inp_type=="single individual":
        print("Press -1 when you want to stop inputting values")
        val_freq=0.0
        sum_x=0.0
        sum_x_square=0.0
        total_obs_x=-1
        while val_freq!=-1:
            sum_x+=val_freq
            sum_x_square+=(val_freq**2)
            total_obs_x+=1
            val_freq=float(input("Please enter a value: "))
        diff_mean=float(input("Please write the difference in means to be tested: "))
        mean_x=sum_x/total_obs_x
        comb_var=((1/(total_obs_x-1))*(sum_x_square-((sum_x**2)/total_obs_x)))/total_obs_x
        if total_obs_x>=30:
            if test_tail==1:
                critical_value=stats.norm.ppf(1-sig_level)
            elif test_tail==2:
                critical_value=stats.norm.ppf(1-(sig_level/2))
        else:
            if test_tail==1:
                critical_value=stats.t.ppf(1-sig_level,total_obs_x-1)
            elif test_tail==2:
                critical_value=stats.t.ppf(1-(sig_level/2),total_obs_x-1)
        test_statistic=(mean_x-diff_mean)/(comb_var**(0.5))        
     
    elif data_inp_type=="double sum":
        sum_x=float(input("Please enter the sum of observations of x: "))
        sum_y=float(input("Please enter the sum of observations of y: "))
        sum_x_square=float(input("Please enter the sum of observations of x^2: "))
        sum_y_square=float(input("Please enter the sum of observations of y^2: "))
        total_obs_x=int(input("Please enter the total number of observations of x: "))
        total_obs_y=int(input("Please enter the total number of observations of y: "))
        pool_var_check=input("Will the variance be pooled?: ")
        diff_mean=float(input("Please write the difference in means to be tested: "))
        mean_x=sum_x/total_obs_x
        mean_y=sum_y/total_obs_y
        unb_var_x=(1/(total_obs_x-1))*(sum_x_square-((sum_x**2)/total_obs_x))
        unb_var_y=(1/(total_obs_y-1))*(sum_y_square-((sum_y**2)/total_obs_y))
        if pool_var_check=="no":
            comb_var=(unb_var_x/total_obs_x)+(unb_var_y/total_obs_y)
            test_statistic=((mean_x-mean_y)-(diff_mean))/(comb_var**(0.5))
        elif pool_var_check=="yes":
            pool_var=((total_obs_x-1)*(unb_var_x)+(total_obs_y-1)*(unb_var_y))/(total_obs_y+total_obs_x-2) 
            test_statistic=((mean_x-mean_y)-(diff_mean))/(pool_var**(0.5))*(((1/total_obs_x)+(1/total_obs_y))**0.5)   
        if total_obs_x>=30:
            if test_tail==1:
                critical_value=stats.norm.ppf(1-sig_level)
            elif test_tail==2:
                critical_value=stats.norm.ppf(1-(sig_level/2))
        else:
            if test_tail==1:
                critical_value=stats.t.ppf(1-sig_level,total_obs_x+total_obs_y-2)
            elif test_tail==2:
                critical_value=stats.t.ppf(1-(sig_level/2),total_obs_x+total_obs_y-2)

    elif data_inp_type=="single sum":
        sum_x=float(input("Please enter the sum of observations of x: "))
        sum_x_square=float(input("Please enter the sum of observations of x^2: "))
        total_obs_x=int(input("Please enter the total number of observations of x: "))
        comb_var=((1/(total_obs_x-1))*(sum_x_square-((sum_x**2)/total_obs_x)))/total_obs_x
        if total_obs_x>=30:
            if test_tail==1:
                critical_value=stats.norm.ppf(1-sig_level)
            elif test_tail==2:
                critical_value=stats.norm.ppf(1-(sig_level/2))
        else:
            if test_tail==1:
                critical_value=stats.t.ppf(1-sig_level,total_obs_x-1)
            elif test_tail==2:
                critical_value=stats.t.ppf(1-(sig_level/2),total_obs_x-1)
        diff_mean=float(input("Please write the difference in means to be tested: "))
        mean_x=sum_x/total_obs_x
        test_statistic=(mean_x-diff_mean)/(comb_var**(0.5))        


         
    print(f"The test statistic is: {test_statistic}")
    print(f"The critical value is: {critical_value}")

value_inputting()


