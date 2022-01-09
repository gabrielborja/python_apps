from datetime import date
import mailbox
from email.utils import parsedate
import json

class MboxParser():
    def __init__(self, mbox_str: str):
        self._inbox = mailbox.mbox(mbox_str)
        self._email_list = []

    def count_emails(self) -> int:
        return self._inbox.__len__()
    
    def get_keys(self) -> list:
        """ Return a list of keys available in mbox file """
        key_list =  sorted(self._inbox[0].keys())
        return key_list

    def parse_mbox(self) -> None:
        """ Parse mbox file and extract date and from values """
        for i in range(self.count_emails()):
            date = self._inbox[i].get('Date')
            sender_name = self._inbox[i].get('From')
            my_dict = dict({"date": date, "from": sender_name})
            self._email_list.append(my_dict)
    
    def get_emails(self) -> list:
        """ Returns a list of dictionaries of parsed emails """
        return self._email_list[-5:]
    
    def _is_jsonable(self, x) -> bool:
        """ Check if json object is serializable """
        try:
            json.dumps(x)
            return True
        except (TypeError, OverflowError):
            return False
        
    def save_to_json(self):
        filtered_emails = [i for i in self._email_list if self._is_jsonable(i)]
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_emails, f, indent=4)
        print("All data saved successfully!")
        print(f"Final json file contains: {len(filtered_emails)} records.")


if __name__ == '__main__':
    emails = MboxParser(mbox_str='Inbox.mbox')
    emails.parse_mbox()
    print(emails.get_emails()) # => List last five records
    emails.save_to_json()