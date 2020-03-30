name = ['CClist' , 'ACCList', 'Login']

#print (name[1])

for i in name:
    se =  ( 'service_desc' + ' ' + i)



send_nsca = {'hostname':'localhost' , 'Service' : i }



print (send_nsca)