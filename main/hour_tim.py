import machine
from machine import RTC

def time_corr():
    if machine.reset_cause()==1:
        import PST_time
        PST_time.time_pull()

    curr_min=RTC().datetime()[5] #current minutes
    curr_sec=RTC().datetime()[6] #current seconds
    i=0
    min_diff=60-curr_min
    sec_diff=60-curr_sec
    if min_diff==0:
        slep_time=3600000-(1000*sec_diff)
    else:
        slep_time=(min_diff*60000)-(1000*sec_diff)


    
    print(slep_time)
    return(slep_time)
