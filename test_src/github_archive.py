#! /usr/bin/env python

import requests
import datetime
import sys

inputDate = raw_input("Enter the date in format 'dd/mm/yyyy' : ")
day,month,year = inputDate.split('/')
isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
    if len(year) == 4 and len(day) == 2 and len(month) == 2 :
        pass
    else :
        print('Invalid year')
        sys.exit(1)
    if len(day) == 1:
        day = '0'+day
    if len(month) == 1:
        month = '0'+month
except ValueError :
    isValidDate = False
    if(isValidDate) :
        pass
    else :
        sys.exit("Input date is not valid")

try :
    inputTime = int(raw_input("Enter the time hour (1 - 24): "))
    if inputTime <= 0 or inputTime > 24 :
        sys.exit("Invalid time hour provided")
    else :
        pass
except ValueError :
        sys.exit("Input time hour is not valid")

url = 'http://data.githubarchive.org/{0}-{1}-{2}-{3}.json.gz'.format(year,
        month, day, inputTime)
print('Github Archive URL : {}'.format(url))
try :
    #github_archive_01_01_2018_13.gz
    archive_file = 'github_archive_{0}_{1}_{2}_{3}.gz'.format(day, month, year, inputTime)
    print('Downloading {} ...'.format(archive_file))
    r = requests.get(url)
    if(r.status_code == 200) :
        with open(archive_file, 'wb') as f:  
            f.write(r.content)
        print('Download Complete')
        print('HTTP status code : {}'.format(r.status_code))
    else :
        print('Request failed with HTTP error code {}'.format(r.status_code))

except (requests.exceptions.RequestException,
        requests.exceptions.HTTPError) as e :
    print('In exception')
    print e
    sys.exit(1)
