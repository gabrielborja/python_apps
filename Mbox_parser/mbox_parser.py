import mailbox
import json

def parse_mbox():
    """Parse emails from mbox format to a list of dictionaries"""

    #Read mbox file
    inbox = mailbox.mbox('Inbox.mbox')

    #Define keys and empty list
    keys = ['Date', 'From', 'Subject']
    email_list = []

    #Extract data from keys and save to a list
    for message in inbox.itervalues():
        my_dict = dict(message.items())
        email_list.append({key:my_dict[key] if key in my_dict.keys() else '' for key in keys})
    
    #Print example output to console
    print(len(email_list), 'messages')
    print('**'*25)
    print(email_list[-3:]) #Print last 3 emails

    return email_list

def save_to_json(my_list):
    """Save list to json file"""
    try:
        with open('email_list.json', 'w') as f:
            json.dump(my_list, f)
    except TypeError:
        e = 0
        e += 1
    print(f'Unserializable obj: {e}')

#Run main program
if __name__ == "__main__":
    #email_list = [{'Date': 'Tue, 06 Apr 2021 19:17:22 +0000', 'From': '"Marketing Analytics" <no-reply@t.mail.coursera.org>', 'Subject': 'New Online Course to Help You Develop Effective Digital Marketing Strategies'},
    #{'Date': 'Tue, 06 Oct 2020 18:26:43 +0000', 'From': '"Humble Bundle" <contact@mailer.humblebundle.com>', 'Subject': '=?utf-8?b?QnJhd2wgZm9yIGl0IGFsbCBpbiB0aGUgTGV04oCZcyBGaWdodCBCdW5kbGUhIPCfpYo=?='},
    #{'Date': 'Thu, 15 Oct 2020 08:42:51 +0000 (UTC)', 'From': 'Digg Pizza <hei@digg.no>', 'Subject': '=?UTF-8?Q?P=C3=A5minnelse!?= Du har fortsatt tre gratis pizzaer til gode =?UTF-8?B?8J+NlQ==?='}]
    email_list = parse_mbox()
    save_to_json(email_list)