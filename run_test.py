import sys
from datetime import datetime

# Add the current directory to sys.path
sys.path.append('.')
import test

#cythonize -i day_5_part1.pyx
#python run_test.py

a = datetime.now()
test.test3()
b = datetime.now()
print((b-a).total_seconds())