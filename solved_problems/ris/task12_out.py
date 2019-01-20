from pylab import *
from matplotlib import rc
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])
def U(t):
	A=1
	U0=0.5
	tau=1
	a=4
	U=(
	+(1-exp(-t*a))*heaviside(t,1)
	-(1-exp(-(t-tau)*a))*heaviside(t-tau,1)
	+(1-exp(-(t-2*tau)*a))*heaviside(t-2*tau,1)
	-(1-exp(-(t-3*tau)*a))*heaviside(t-3*tau,1)
	+U0*exp(-a*t)
	  )
	return U
t=linspace(0,10,1000)
plot(t,U(t))
ylabel(r'$U_{\text{вых}}$',fontsize=16)
xlabel(r'$t$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
savefig('task12_out.pdf')
show()
