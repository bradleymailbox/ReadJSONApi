################################################33
# ABOUT: Call an API and return json data for processing
# written using python 2.+
# DEV: 2019/01/25
################################################33

#Import the modules
import requests
import json
import csv
import config as cf
import api_module as apimod

# Convert it to a Python dictionary
api = 'http://196.10.10.26:8080/alfresco/service/api/people'
data = json.loads(apimod.getRequestData(api))
# open a file to write the output to
f = open(cf.filenames['output'], "w")
#write the file header
f.writelines('username,email,location\n')
# Loop through the result.
for item in data['people']:
        # write the data read
        wstr = "USER:%s\t\tE-MAIL:%s" % (item['userName'], item['email'])
        # create the string to write to the file
        csv_str = str(item['userName']) +','+ str(item['email']) +  ',' + str(item['location']) + "\n"
        #write outputs to screen and file
        print wstr
        f.writelines(csv_str)
# close the file and terminate the program
f.close()
print "program ended!"
