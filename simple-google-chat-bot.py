from json import dumps
from httplib2 import Http # needs pip install
from time import sleep
import schedule # needs pip install

general_webhook_url = '####chat_key_here####'

person1 = ' <users/000000000000000000001> '
person2 = ' <users/000000000000000000002> '
person3 = ' <users/000000000000000000003> '

def sendgeneralmessage(bot_message):
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=general_webhook_url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print('Sent in General : ' + dumps(bot_message))

def reminder1():
    sendgeneralmessage({'text' : 'Happy Monday!'})
def reminder2():
    sendgeneralmessage({'text' : 'Good Morning  ('+ person1 + person2 + person3 +'). Have a good day.'})

schedule.every().monday.at("09:00").do(reminder1)
schedule.every().day.at("09:00").do(reminder2)

while True:
    schedule.run_pending()
    sleep(1)
