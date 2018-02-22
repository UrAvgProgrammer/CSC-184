import requests


def send_request(x):
    try:
        response = requests.get('http://data.nba.net/prod/v1/allstar/'+x+'/AS_roster.json')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

#espn take down its api so so far the available information is from 2016 to present only.
x = raw_input('Enter the date for to see the AllStar roster of NBA teams that year:\n')
send_request(x)