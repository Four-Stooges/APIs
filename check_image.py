import glob
from subprocess import call
import sys

test_file = sys.argv[1]
pics = glob.glob('./images/*.*')
for pic in pics:
	print(pic)
	call(['python3','face_detect.py',test_file,pic])