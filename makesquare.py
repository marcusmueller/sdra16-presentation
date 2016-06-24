#!/usr/bin/env python2

import numpy
from matplotlib import pyplot
import seaborn

def makefig(figsize=(1024./90,768./90)):
    return pyplot.figure(figsize=figsize, dpi=90)

def savefig(f,name):
    pyplot.ylim((-1.1,1.1))
#    pyplot.xlim((x[0],x[-1]))
    pyplot.tight_layout()
    return f.savefig(name + ".pdf")

N = 1000
x = numpy.linspace(-3, 3, N)
sin_analog = numpy.sin(x* numpy.pi)
noise_analog = numpy.random.normal(size=N)*0.2
y_digital = (numpy.floor(x) % 2 - 0.5)*-2
y_digital = numpy.round(y_digital, 2)
x_digital = x

c= numpy.pi/4
def comp(n,x):
    return c * numpy.sin(n*numpy.pi*x)/n
def plotlast():
    pyplot.plot(x,y_digital)
    pyplot.plot(x, y)

f = makefig()
pyplot.plot(x,y_digital)
savefig(f, "square")

f = makefig(figsize=(1024*0.45/90,768*0.45/90))
pyplot.plot(x,y_digital)
savefig(f, "squarehalf")


f = makefig()
y = comp(1,x)
pyplot.plot(x,y_digital)
pyplot.plot(x, y)
legend = ["square wave", "$\sin(\pi x)$"]
pyplot.legend(legend)
savefig(f,"square1harmonic")

output = open("squarewaves.tex", "w")
counter = 1

for maxn in range(1, 20, 2) + [65,1001]:
    f = makefig()
    legend = ["square wave", "all odd harmonics below {:d}".format(maxn), "$\sin(" + str(maxn) + "x) / "+str(maxn)+"$"]
    pyplot.plot(x,y_digital)
    y = comp(1,x)
    for i in range(3, maxn, 2):
        y += comp(i,x)
    pyplot.plot(x,y)
    y= comp(maxn, x)
    pyplot.plot(x,y)

    pyplot.legend(legend)
    filename = "square"+str(maxn)
    savefig(f, filename)
    output.write("\n\n\\only<" +str(counter) + ">{\\includegraphics[width=\\textwidth]{"+filename+"}}\n\n")
    counter += 1

output.close()

f = makefig()
x = numpy.arange(-101,101,2)
pyplot.xticks(x)
y = c*1/x
pyplot.stem(x,y)
pyplot.legend(["Spectrum of square wave"])
pyplot.xlim((0,41))
savefig(f, "squarespectrum")
f = makefig(figsize=(1024*0.45/90,768*0.45/90))
x = numpy.arange(-101,101,2)
pyplot.xticks(x[::2])
y = c*1/x
pyplot.stem(x,y)
pyplot.legend(["Spectrum of square wave"])
pyplot.xlim((0,41))
savefig(f, "squarespectrumhalf")
f = makefig()
x = numpy.arange(-101,101,2)
pyplot.xticks(x)
y = [ c*1/_x if abs(_x) <= 7 else 0 for _x in x]
pyplot.stem(x,y)
pyplot.legend(["Spectrum of band-limited square wave"])
pyplot.xlim((0,41))
savefig(f, "squarespectrum7")
f = makefig()
x = numpy.linspace(-3, 3, N)
y = comp(1,x)
for n in range(3,6,2):
    y+=comp(n,x)
pyplot.plot(x,y)
pyplot.legend(["Reconstructed from only 1., 3., 5. and 7. sine"])
savefig(f,"squarerec7")
