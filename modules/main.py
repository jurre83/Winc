# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import this
import time
import math
from datetime import datetime
import sys
from greet import supergreeting

now = datetime.now()


def wait(seconds):
    time.sleep(seconds)
    return


def my_sin(float):
    sin = math.sin(float)
    return sin


def iso_now():
    return now.strftime("%Y-%m-%dT%H:%M")


def platform():
    return sys.platform


def supergreeting_wrapper(name):
    return supergreeting(name)
