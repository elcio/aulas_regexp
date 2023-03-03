import re

def validate(ip):
    ip_part = r'(1?\d{1,2}|2([0-4]\d|5[0-5]))'
    validator = r'^(%s\.){3}%s$' % (ip_part, ip_part)
    print(re.match(validator, ip))
    return re.match(validator, ip)

