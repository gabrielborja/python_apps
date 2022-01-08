import mailbox

class MboxParser():
    def __init__(self, mbox: str):
        self.__mbox__ = mbox
        self.__email_list__ = []

    def parse_mbox(self: list) -> list:
        """ Parse mbox file and extract date and from values """
        inbox = mailbox.mbox(self.__mbox__)
        for i in range(10):
            date = inbox[i].get('Date')
            sender_name = inbox[i].get('From')
            my_dict = dict({"date": date, "from": sender_name})
            self.__email_list__.append(my_dict)
    
    def get_emails(self: list) -> list:
        """ Returns a list of emails parsed by mbox_parser """
        return self.__email_list__

if __name__ == '__main__':
    emails = MboxParser(mbox='Inbox.mbox')
    emails.parse_mbox()
    print(emails.get_emails())