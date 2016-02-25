#coding: utf-8

import time
from spinner import make_it_spin, frames


@make_it_spin(frames[1], 'waiting..')
def foo():
    time.sleep(5)
foo()

