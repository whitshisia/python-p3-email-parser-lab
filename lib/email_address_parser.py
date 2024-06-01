# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
        emails = email_regex.findall(self.email_string)
        emails = list(set(emails))
        emails.sort()
        return emails