from pylab import *
from matplotlib import rc
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])
def S(w):
	A=1
	t=1
	S=2*A*abs((1-cos(w*t))/w)
	return S
w=linspace(0,100,1000)
plot(w,S(w))
ylabel(r'$|S_{\omega}|$',fontsize=16)
xlabel(r'$\omega$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
savefig('task15_out.pdf')
show()
