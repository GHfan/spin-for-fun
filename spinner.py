#!/usr/bin/env python
#coding: utf-8

import time
import sys
import functools
import multiprocessing


frames = [
        [u"|", u"/", u"-", u"\\"],
        [u"+-------",
         u"-+------",
         u"--+-----",
         u"---+----",
         u"----+---",
         u"-----+--",
         u"------+-",
         u"-------+",
         u"------+-",
         u"-----+--",
         u"----+---",
         u"---+----",
         u"--+-----",
         u"-+------",
         u"+-------",
         ],
        ]

pipe = multiprocessing.Pipe()

def spin(pipe, frames, msg):
    i = 0
    length = len(frames)
    # spin when no data to recv
    while not pipe.poll():
        sys.stdout.write(u'\r{0}  {1}'.format(frames[i % length], msg))
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

def make_it_spin(frames, msg='bang bang bang..'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            spin_process = multiprocessing.Process(target=spin, args=(pipe[1], frames, msg))
            spin_process.start()
            func(*args, **kwargs)
            pipe[0].send("stop")
        return wrapper
    return decorator
