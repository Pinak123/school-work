print ('   Enter the required values to find simple intrest  ')
principal=float(input('enter principal amoungth'))
rate=float(input('enter rate of intreast'))
time=float(input('enter time period'))
intrest=(principal*rate*time)*0.01
total=principal+rate
print ('total amounth after'+str(time)+'years is '+ str(total) +' And value of intrest is '+str(intrest))