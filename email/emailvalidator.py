import re

def validate(email):
    return re.match(r'[\w\.+-]+@([\w-]+\.)+[a-z]{2,}', email)
