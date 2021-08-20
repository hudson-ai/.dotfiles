from IPython import get_ipython
ipython = get_ipython() 

autoreload = True
if autoreload:
    ipython.magic("load_ext autoreload") 
    ipython.magic("autoreload 2")

ipython.magic("load_ext line_profiler")

#from alpha import *

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.ion()
