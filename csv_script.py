csv_filepathname ="C:\\Users\\edwluk1\\Desktop\\CSV_Upload.csv"

your_djangoproject_home="C:\\Users\\edwluk1\\spxdashboard\\"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='spxdashboard.settings'

from purchase_requests.models import Request

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
next(dataReader, None)


for row in dataReader :
    request=Request()
    request.part_number=row[0]
    request.qty=row[1]
    request.WH=row[2]
    request.OTP=row[3]

    request.save
