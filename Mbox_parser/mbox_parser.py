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
    with open('email_list.json', 'w') as f:
        json.dump(my_list, f)

#Run main program
if __name__ == "__main__":
    email_list = parse_mbox()
    save_to_json(email_list)