#!/usr/bin/python3 -B

# Put this file in:
# $HOME/.ipython/profile_default/startup/
# and it will act like a pythonic .bashrc.

import os, sys, threading, itertools

failed = {}

#sys.exit(0)

def exec_code(code):
    try:
        exec(code, globals())
    except Exception as e:
        failed['pyrc'] = e

with open(__file__) as fp:
    lines = fp.read().splitlines()

import_lines = itertools.dropwhile(lambda line: '#'*8 not in line, lines)
source = '\n'.join(import_lines)
thread = threading.Thread(target=exec_code, args=(source,))
thread.start()

sys.exit(0)


#########

# start executing here.
# keep track of the status of certain
# packages that are often not present.

# alpha
try:
    import alpha
    from alpha import *
    #alpha.set_log_level('debug')
except:
    failed['alpha'] = sys.exc_info()

# general
import os
import re
import io
import ast
import dis
import sys
import mmap
import glob
import json
import math
import time
import types
import ctypes
import base64
import signal
import struct
import socket
import pickle
import random
import typing
import atexit
import logging
import hashlib
import zipfile
import inspect
import pathlib
import warnings
import argparse
import datetime
import operator
import requests
import textwrap
import importlib
import functools
import itertools
import traceback
import contextlib
import collections
import dataclasses

# concurrency libraries
import asyncio
import threading
import subprocess
import concurrent.futures
import multiprocessing as mp
import multiprocessing.managers
import multiprocessing.sharedctypes
import multiprocessing.synchronize
import multiprocessing.shared_memory

# data science
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.ion()


