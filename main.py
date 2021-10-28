import os
dirname = os.getcwd()
import sys
sys.path.append(f'{dirname}/src/')
try:
	import tool38
	tool38.main()
except:
	import tool310
	tool310.main()

