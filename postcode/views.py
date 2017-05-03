import csv

from django.http import JsonResponse

# Create your views here.


def api_postcode(request, postcode):
    retdata = []
    csv_file = csv.reader(open('static/postcode-my.csv'), delimiter=",")

    for row in csv_file:
        if postcode == row[0]:
            tempdata = dict()
            tempdata['postcode'] = row[0]
            tempdata['locality'] = row[1]
            tempdata['town'] = row[2]
            tempdata['state'] = row[3]
            retdata.append(tempdata)
    return JsonResponse(retdata, safe=False)