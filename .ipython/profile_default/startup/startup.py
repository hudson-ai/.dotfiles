from IPython import get_ipython
ipython = get_ipython() 
ipython.magic("load_ext autoreload") 
ipython.magic("autoreload 2")

#import multiprocessing as mp
#mp.set_start_method('fork')

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.ion()
