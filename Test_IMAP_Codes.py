import json
import IMAPCodes as IC
from imaplib import IMAP4_SSL
from datetime import datetime

# ==========================================================================

# IMAP settings
# --------------
IMAPServerName = 'outlook.office365.com'
IMAPSeverPort = '993'

# Email login settings
# --------------
path = 'C:\\Users\\vgand\\Desktop\\MyStuff\\Personal Stuff\\Credentials\\'
accountName = 'Main_Outlook'

with open('Email_Accounts.json') as config_file:
	loginData = json.load(config_file)

emailID = loginData[accountName]['email_ID']
emailPassword = loginData[accountName]['password']

# ==========================================================================

# box = IMAP4_SSL(IMAPServerName, IMAPSeverPort)
# box.login(emailID, emailPassword)

# msgnum1 = '2627'	# notify.uw.edu
# msgnum2 = '2641'	# erdlyww@uw.edu, has a pdf and ATT00001.txt
# msgnum3 = '2621'	

# codes = Codes.codes

# for i in box.list()[1]:
# 	l = i.decode().split(' "/" ')
# 	folder = l[1]
# 	# print(folder)
# 	typ, status = box.status(folder,'(MESSAGES RECENT)')

# 	status_bytes = status[0]
# 	find_MESSAGES = status_bytes.find(b'MESSAGES')
# 	find_RECENT = status_bytes.find(b'RECENT')
# 	find_par = status_bytes.find(b')')

# 	# Count total emails and 'new' emails
# 	total = int(status_bytes[find_MESSAGES + 9: find_RECENT - 1])
# 	new = int(status_bytes[find_RECENT + 7: find_par])

# 	print(folder + '	---	' + str(total) + '	---	' + str(new))




print(dt())