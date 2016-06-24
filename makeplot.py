#!/usr/bin/env python2

import numpy
from matplotlib import pyplot
import seaborn
from taps import taps
from scipy import signal

def makefig(figsize=(1024./90,600./90)):
    return pyplot.figure(figsize=figsize, dpi=90)

def savefig(f,name):
    pyplot.tight_layout()
    return f.savefig(name + ".pdf")

f=makefig()
taps = [t*10000 for t in taps]
w,h = signal.freqz(taps,10000)
pyplot.plot(w*12.5/numpy.pi,10*numpy.log10(numpy.abs(h)))
pyplot.ylabel("power [dB]")
pyplot.xlabel("frequency [MHz]")
pyplot.ylim(-100,1)
savefig(f,"filterplot")
