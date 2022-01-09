from datetime import date
import mailbox
from email.utils import parsedate

class MboxParser():
    def __init__(self, mbox_str: str):
        self._inbox = mailbox.mbox(mbox_str)
        self._email_list = []

    def get_keys(self) -> list:
        """ Return a list of keys available in mbox file """
        key_list =  sorted(self._inbox[0].keys())
        return key_list

    def parse_mbox(self) -> None:
        """ Parse mbox file and extract date and from values """
        for i in range(10):
            date = self._inbox[i].get('Date')
            sender_name = self._inbox[i].get('From')
            my_dict = dict({"date": date, "from": sender_name})
            self._email_list.append(my_dict)
    
    def get_emails(self) -> list:
        """ Returns a list of sorted emails parsed by mbox_parser method """
        sorted_emails = sorted(self._email_list, key=lambda d: parsedate(d['date']))
        return sorted_emails


if __name__ == '__main__':
    emails = MboxParser(mbox_str='Inbox.mbox')
    emails.parse_mbox()
    print(emails.get_emails())
    #print(emails.get_keys())