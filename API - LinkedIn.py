import requests
import json

#example basic search
people_string='''
{
    "people":[
        {
            "name":"John Smith"
        }
    ]
}
'''

data=json.loads(people_string)

print(data['people'])

#playing with LinkedIn API
from linkedin import linkedin
from oauthlib import *

KEY = 'wFNJekVpDCJtRPFX812pQsJee-gt0zO4X5XmG6wcfSOSlLocxodAXNMbl0_hw3Vl'
SECRET = 'daJDa6_8UcnGMw1yuq9TjoO_PMKukXMo8vEMo7Qv5J-G3SPgrAV0FqFCd0TNjQyG'

API_KEY = "wFNJekVpDCJtRPFX812pQsJee-gt0zO4X5XmG6wcfSOSlLocxodAXNMbl0_hw3Vl"
API_SECRET = "daJDa6_8UcnGMw1yuq9TjoO_PMKukXMo8vEMo7Qv5J-G3SPgrAV0FqFCd0TNjQyG"
RETURN_URL = "http://localhost:8000"
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print(authentication.authorization_url)
application = linkedin.LinkedInApplication(authentication)
