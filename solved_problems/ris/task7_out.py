from pylab import *
from matplotlib import rc
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])
def K(w):
	K=( (w**4+w**2)/
		            (
		              (1-w**2)**2+w**2 
		            )
	  )**0.5
	return K
w=linspace(-10,10,2000)
plot(w,K(w))
ylabel(r'$|K_{\omega}|$',fontsize=16)
xlabel(r'$\omega$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
savefig('task7_out.pdf')
show()
