addcode1 = '[HEADER]'
addcode2 = '[HEADER.FIELDS]'		# INVALID
addcode3 = '[HEADER.FIELDS.NOT]'	# INVALID
addcode4 = '[TEXT]'


code1 = '(RFC822)'					# EVERYTHING
code2 = 'ALL'						# Internaldate, rfc.size, envelope, subject
code3 = 'FAST'						# Internaldate, rfc.size
code4 = 'FULL'						# Internaldate, rfc.size, envelope, subject, body summary
code5 = 'BODY'						# Body summary

code5_1 = code5 + addcode1			# All header data + flags
# code5_2 = code5 + addcode2
# code5_3 = code5 + addcode3
code5_4 = code5 + addcode4			# Only email text

code6 = 'BODY.PEEK'
code6_1 = code6 + addcode1			# All header data, limited to range
# code6_2 = code6 + addcode2
# code6_3 = code6 + addcode3
code6_4 = code6 + addcode4			# Only email text, limited to range
code7 = 'BODYSTRUCTURE'				# Structure of body
code8 = 'ENVELOPE'					# Sender, datetime sent at, subject, messageID
code9 = 'FLAGS'						# Flags, eg: Seen
code10 = 'INTERNALDATE'				# datetime received at
code11 = 'RFC822'					# Same as '(RFC822)'

code11_1 = 'RFC822.HEADER'			# Same as 'BODY[HEADER]', no flags
code11_2 = 'RFC822.SIZE'			# rfc.size
code11_3 = 'RFC822.TEXT'			# Same as 'BODY[TEXT]'

code12 = 'UID'						# UID = (2220 + msgnum) * 4??

codes = {
	'code1': code1,
	'code2': code2,
	'code3': code3,
	'code4': code4,
	'code5': code5,
	'code5_1': code5_1,
	# 'code5_2': code5_2,
	# 'code5_3': code5_3,
	'code5_4': code5_4,
	# 'code6': code6,
	'code6_1': code6_1,
	# 'code6_2': code6_2,
	# 'code6_3': code6_3,
	'code6_4': code6_4,
	'code7': code7,
	'code8': code8,
	'code9': code9,
	'code10': code10,
	'code11': code11,
	'code11_1': code11_1,
	'code11_2': code11_2,
	'code11_3': code11_3,
	'code12': code12,	
}