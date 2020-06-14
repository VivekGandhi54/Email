
# IMAP settings
# --------------
IMAPServer = None
IMAPPort = None

# Email login settings
# --------------
emailID = None
emailPassword = None

# ==========================================================================

# nkepfyooljbzfecc

from imaplib import IMAP4_SSL
from datetime import datetime
import time
import json

# Return the current time as a string "DD/MM/YY hh:mm:ss"
timeStamp = lambda: datetime.now().strftime("%x %X")

# ==========================================================================

def getLoginDetails(accountName = 'Main_Outlook'):
	global emailID, emailPassword
	global IMAPServer, IMAPPort

	# ----------------------------------------------------------------------

	path = 'C:\\Users\\vgand\\Desktop\\MyStuff\\Personal Stuff\\Credentials\\'

	with open(path + 'Email_Accounts.json') as config_file:
		loginData = json.load(config_file)

	emailID = loginData[accountName]['email_ID']
	emailPassword = loginData[accountName]['password']
	service = loginData[accountName]['service']

	# ----------------------------------------------------------------------

	with open('IMAPProfiles.JSON') as config_file:
		serverData = json.load(config_file)

	IMAPServer = serverData[service]['Server']
	IMAPPort = serverData[service]['Port']

# ==========================================================================

def initializeInbox():
	global emailID, emailPassword, IMAPServer, IMAPPort

	box = IMAP4_SSL(IMAPServer, IMAPPort)
	box.login(emailID, emailPassword)

	return box

# ==========================================================================

def main():
	global emailRefreshes, isOnTimeout

	try:
		# Initialize Inbox
		box = initializeInbox()

		# Check inbox every 15 seconds
		while True:
			checkForNew(box)

			# Managed to check inbox after a timeout
			if isOnTimeout:
				isOnTimeout = False

			print(timeStamp() + ' --- Email Refreshes: ' + str(emailRefreshes) + '		', end='\r', flush=True)
			time.sleep(15)

	except KeyboardInterrupt:
		print('\nKeyboardInterrupt')
		exit()

	except:
		timeout()

# ==========================================================================


def checkForNew(box):
	global emailRefreshes, confirmedTotal

	# Ask for inbox status
	typ, status = box.status('Inbox','(MESSAGES RECENT)')

	status_bytes = status[0]
	find_MESSAGES = status_bytes.find(b'MESSAGES')
	find_RECENT = status_bytes.find(b'RECENT')
	find_par = status_bytes.find(b')')

	# Count total emails and 'new' emails
	total = int(status_bytes[find_MESSAGES + 9: find_RECENT - 1])
	new = int(status_bytes[find_RECENT + 7: find_par])

	# For first iteration
	if emailRefreshes == 0:
		confirmedTotal = total

	new = 100

	# If any new emails or discrepancy in how many emails have been checked
	if new > 0 or total > confirmedTotal + new:
		msgnums = [item for item in range(total - new + 1, total + 1)]
		nums = str(msgnums).strip('[]').replace(' ','')

		# Get the first few relevant messages
		typ, messages = box.fetch(nums, 'BODY[TEXT]')

		# Every other item in 'messages' contains the flags of the email
		for i in range(0, new*2, 2):
			msg = messages[i][1]

			# If email contains notification about a class opening
			if b'notify.uw.edu' in msg:
				SLN = getSLN(msg)

				if SLN != -1:
					RegisterBot.register([SLN])

	confirmedTotal = total
	emailRefreshes += 1

# ==========================================================================

def testEmailConnection(details = None):
	global emailID, emailPassword
	global IMAPServer, IMAPPort

	if details != None:
		TEST_EmailID = details['EmailID']
		TEST_EmailPassword = details['EmailPassword']
		TEST_IMAPServer = details['IMAPServer']
		TEST_IMAPPort = details['IMAPPort']
	else:
		TEST_EmailID = emailID
		TEST_EmailPassword = emailPassword
		TEST_IMAPServer = IMAPServer
		TEST_IMAPPort = IMAPPort

	print('Test email ID:		' + TEST_EmailID)
	print('Test email ID:		' + '*'*len(TEST_EmailPassword))
	print('Test IMAP Server:	' + TEST_IMAPServer)
	print('Test IMAP Port:		' + TEST_IMAPPort)

	try:
		box = IMAP4_SSL(TEST_IMAPServer, TEST_IMAPPort)
		box.login(TEST_EmailID, TEST_EmailPassword)
		reply = box.noop()

		if reply[0] == 'OK':
			print('Passed')
			return True

		else:
			print('Failed Login')
	except:
		print('Failed to connect to Server')

	return False

# ==========================================================================

getLoginDetails('Main_Outlook')
testEmailConnection()