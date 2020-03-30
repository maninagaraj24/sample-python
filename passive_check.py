#!/usr/bin/python

service_description = {'Login', 'Logout', 'CCList', 'ACCList'}

for n in service_description:
     name = n
send_nsca = ('localhost' + ';'  + name  + ';' + '1' + ';' + 'This service is Failed')


print ('---' * 64)
print (' ' * 64)
print (send_nsca)
print (' ' * 64)
print ('---' * 64)





