#!/usr/bin/env python2

import numpy
from matplotlib import pyplot
import seaborn

def makefig(figsize=(1024./90,768./90)):
    return pyplot.figure(figsize=figsize, dpi=90)

def savefig(f,name, xlim=None):
    pyplot.ylim((-1.6,1.6))
    if not xlim:
        xlim = (x[0],x[-1])
    pyplot.xlim(xlim)
    pyplot.tight_layout()
    return f.savefig(name + ".pdf")

N = 6**4
x = numpy.linspace(0, 6, N)
sin_analog = numpy.sin(x* numpy.pi)
cos_analog = numpy.cos(x* numpy.pi)
noise_analog = numpy.random.normal(size=N)*0.075
y_analog = sin_analog + noise_analog
y_digital = y_analog[0::N/6**2]
y_digital = numpy.round(y_digital, 2)
x_digital = x[0::N/6**2]

f = makefig()
pyplot.plot(x,cos_analog)
pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)$"])
savefig(f, "sigcos")

f = makefig((1024./90,180/90))
pyplot.plot(numpy.linspace(-100,100,10000),numpy.cos(numpy.pi*(numpy.linspace(-100,100,10000))))
pyplot.scatter(numpy.arange(-6,6,1./3), numpy.cos(numpy.pi*numpy.arange(-6,6,1./3)))
pyplot.xticks(numpy.arange(-6,6,1))
#pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)$"])
savefig(f, "sigcossmall", xlim=(-6,6))

f = makefig((1024./90,180/90))
#pyplot.plot(x,cos_analog)
pyplot.stem([-0.5,0.5], [0.5,0.5])
pyplot.xticks(numpy.arange(-6,6,1))
#pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)$"])
savefig(f, "speccossmall", xlim=(-6,6))

f = makefig((1024./90,180/90))
#pyplot.plot(x,cos_analog)
pyplot.scatter([-0.5,0.5], [0.5,0.5])
x_=[]
for f_ in [-0.5,0.5]:
    for shift in numpy.arange(-9,9,3):
        x_.append(f_+shift)
#pyplot.vlines(x_,-100,100)
pyplot.stem(x_,[0.5]*len(x_))
pyplot.xticks(numpy.arange(-6,6,1))
#pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)$"])
savefig(f, "speccosperiodsmall", xlim=(-6,6))

f = makefig()
pyplot.plot(x,cos_analog)
pyplot.vlines(numpy.arange(min(x),max(x), 2), -100,100)
pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)$", "period boundaries"])
savefig(f, "sigcosperiod")

f = makefig()
pyplot.plot(x,cos_analog)
#pyplot.vlines(numpy.arange(min(x),max(x), 2), -100,100)
pyplot.vlines(numpy.arange(min(x),max(x), 1./3), -100,100)
x2 = numpy.arange(min(x),max(x),1./3)
y2 = numpy.cos(x2*numpy.pi)
pyplot.scatter(x2,y2)
pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)\\rightarrow f_\cos = \\frac{1}{2}$", "sampling instants, $f_{sample}=3$"])
savefig(f, "sigcossampling")

f = makefig()
#pyplot.plot(x,cos_analog)
#pyplot.vlines(numpy.arange(min(x),max(x), 2), -100,100)
#pyplot.vlines(numpy.arange(min(x),max(x), 1./3), -100,100)
x2 = numpy.arange(min(x),max(x),1./3)
y2 = numpy.cos(x2*numpy.pi)
pyplot.scatter(x2,y2)
#pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)\\rightarrow f_\cos = \\frac{1}{2}$","signal period" "sampling instants, f_\\text{sample}=3"])
pyplot.legend(["samples"])
savefig(f, "sigcossampled")

f = makefig()
#pyplot.vlines(numpy.arange(min(x),max(x), 2), -100,100)
#pyplot.vlines(numpy.arange(min(x),max(x), 1./3), -100,100)
x2 = numpy.arange(min(x),max(x),1./3)
y2 = numpy.cos(x2*numpy.pi)
y3 = numpy.cos(x*7*numpy.pi)
#pyplot.plot(x,cos_analog,)
pyplot.plot(x,y3 )
pyplot.scatter(x2,y2)
pyplot.legend([ "$\\cos(7\pi x)\\rightarrow f_\cos = \\frac{7}{2}$", "samples"])
#pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)\\rightarrow f_\cos = \\frac{1}{2}$","signal period" "sampling instants, f_\\text{sample}=3"])
savefig(f, "sigcosundersampled")

f = makefig()
#pyplot.vlines(numpy.arange(min(x),max(x), 2), -100,100)
#pyplot.vlines(numpy.arange(min(x),max(x), 1./3), -100,100)
x2 = numpy.arange(min(x),max(x),1./3)
y2 = numpy.cos(x2*numpy.pi)
y3 = numpy.cos(x*13*numpy.pi)
#pyplot.plot(x,cos_analog,)
pyplot.plot(x,y3 )
pyplot.scatter(x2,y2)
pyplot.legend(["$\\cos(13\pi x)\\rightarrow f_\cos = \\frac{13}{2}$", "samples"])
#pyplot.legend(["Analog signal, well known: $\\cos(\\pi x)\\rightarrow f_\cos = \\frac{1}{2}$","signal period" "sampling instants, f_\\text{sample}=3"])
savefig(f, "sigcosundersampled2")

f = makefig()
pyplot.plot(x,y_analog)
pyplot.xticks([])
pyplot.yticks([0])
pyplot.legend(["analog signal"])
savefig(f, "siganalog")

f = makefig()
pyplot.plot(x,y_analog)
pyplot.yticks(numpy.arange(-1.5,1.5,0.1))
pyplot.xticks(x_digital[::2])
pyplot.legend(["analog signal"])
savefig(f, "siganaloggrid")

f = makefig()
pyplot.plot(x,y_analog)
pyplot.yticks(numpy.arange(-1.5,1.5,0.1))
pyplot.xticks(x_digital[::2])
pyplot.stem(x_digital, y_digital)
pyplot.legend(["analog signal", "digital signal"])
savefig(f, "siganalogdigital")

f = makefig()
pyplot.yticks(numpy.arange(-1.5,1.5,0.1))
pyplot.xticks(x_digital[::2])
pyplot.scatter(x_digital, y_digital)
pyplot.legend(["digital signal"])
savefig(f, "sigdigital")

f = makefig((1024./90,250./90))
pyplot.xticks(x_digital[::2])
pyplot.scatter(x_digital, y_digital)
savefig(f, "sigdigitalsmall")

out = open("digital.tex", "w")
out.write("\\texttt{" + ", ".join("{:0.2f}".format(y) for y in y_digital) + "}")
out.close()
