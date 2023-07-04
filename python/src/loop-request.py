#!/usr/bin/python

import requests

url="http://180.184.67.50/api/v1/users"
def loop(total):
    for i in range(50,50+total):
        username="aaa"+str(i)
        token="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4IiwiaWF0IjoxNjg4MzY5ODc4LCJleHAiOjE2ODg0MTMwNzgsInVzZXJUeXBlIjoiTE9DQUwiLCJ1c2VybmFtZSI6ImFkbWluIiwibmFtZSI6ImFkbWluIiwidXNlcklkIjo4LCJyb2xlcyI6WyJST0xFX0FETUlOIl0sImxpbnV4VWlkIjoyMDAxLCJsaW51eEdpZCI6MjAwMSwiZmFzdG9uZVNjZW5hcmlvIjoiRkNDRV9DTE9VRCIsInZlcnNpb24iOiIzLm1hc3Rlci4xNDY3MDMifQ.2CTQi_NZSnsvKYazR-veAJX6zCfwWIJcUu3NC1gj4bwx85GxZf_p6h-Rienw02_9Dw6Q4h4qVI9NbyxkXSeeFQ"
        payload="""
            {
                "name": "",
                "username": "%s",
                "phone": "",
                "loginShell": "",
                "homeDir": "",
                "email": "%s@163.com",
                "password": "111aaa",
                "confirmPassword": "111aaa",
                "roles": [
                    {
                        "name": "ROLE_USER"
                    }
                ],
                "state": "NORMAL",
                "expiresAt": null,
                "groups": [
                    {
                        "id": 1,
                        "name": "defaultGroup"
                    }
                ]
            }
            """ %(username,username)
        headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept" : "application/json, text/plain, */*",
    "Accept-Language" : "en-us",
    "Connection" : "keep-alive",
    "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7",
    "Content-Type":"application/json",
    "Authorization":token
    }

        r = requests.post(url, data=payload,headers=headers)
        requests.head
        print(r.status_code)
        print( r.content)
loop(50)