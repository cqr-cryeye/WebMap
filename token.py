#!/usr/bin/env python3

import string, hashlib
from random import *
allchar = string.ascii_letters + string.digits
password = "cryeye"
print('Token: cryeye')
tokenhash = hashlib.sha256(password.encode('utf-8')).hexdigest()

with open('/root/token.sha256', 'w') as f:
	f.write(tokenhash)
