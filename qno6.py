emails = [
    'ram.sharma@gmail.com',
    'spam@hooya.com',
    'virus@malware.net',
    'shyam.kumar@workcorp.com'
]

blacklist = ('@hooya.com', '@malware.net')

spam_emails = list(filter(lambda email: email.endswith(blacklist), emails))

print(spam_emails)
