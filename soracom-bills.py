import json
import requests
import datetime

import os
import subprocess as sub

url = os.environ["WEBHOOK_URL"]

p = sub.Popen(['/home/vagrant/work/bin/soracom', 'bills', 'get-latest'],stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

content_amount = json.loads(output)['amount']
content_time = json.loads(output)['lastEvaluatedTime']

content_time_formed = datetime.datetime.strptime(content_time, '%Y%m%d%H%M%S')

content = str(content_amount) + 'JPY (' + str(content_time_formed) + ')'

channel_name = '#billing'

payload_dic = {
    "text":content,
    "username":'SORACOM Monthly Billing',
    "icon_emoji":':soracom_suberu:',
    "channel":channel_name,
    }

if __name__=='__main__':
    r = requests.post(url, data=json.dumps(payload_dic))
