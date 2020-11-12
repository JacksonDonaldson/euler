weekday=1;
monthday=1;
month=1;
year=1901;
suncount=0;
while year<=2000:
    if monthday==1 and weekday==6:
        suncount+=1;
    weekday= (weekday+1)%7;
    monthday+=1;
    if month==4 or month ==6 or month==9 or month==11:
        if monthday==31:
            monthday=1;
            month+=1;
    if month ==2:
        if (year%4)==0:
            if monthday==30:
                monthday=1;
                month+=1;
        else:
            if monthday==29:
                monthday=1;
                month+=1;
    if month ==12:
        if monthday==32:
            monthday=1;
            month=1;
            year+=1;
    else:
        if monthday==32:
            monthday =1;
            month+=1;
    #print(year);
    #print(month);
    #print(monthday);
    #print(weekday);
print(suncount);
        
    
