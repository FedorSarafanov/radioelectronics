from pylab import *
from matplotlib import rc
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])
def U(t):
	E=1
	U0=0.5
	tau=5
	U=(E-U0)*heaviside(t,1)*exp(-t)-E*exp(-t+tau)*heaviside(t-tau,1)
	return U
t=linspace(0,10,100)
plot(t,U(t))
ylabel(r'$U_{\text{вых}}$',fontsize=16)
xlabel(r'$t$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
savefig('task4_out.pdf')
show()
