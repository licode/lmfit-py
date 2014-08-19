#!/usr/bin/env python
#<examples/doc_nistgauss2.py>
import numpy as np
from lmfit.models import GaussianModel, ExponentialModel

import matplotlib.pyplot as plt

dat = np.loadtxt('NIST_Gauss2.dat')
x = dat[:, 1]
y = dat[:, 0]

exp_mod = ExponentialModel(prefix='exp_')
gauss1  = GaussianModel(prefix='g1_')
gauss2  = GaussianModel(prefix='g2_')


def index_of(arrval, value):
    "return index of array *at or below* value "
    if value < min(arrval):  return 0
    return max(np.where(arrval<=value)[0])

ix1 = index_of(x,  75)
ix2 = index_of(x, 135)
ix3 = index_of(x, 175)

exp_mod.guess_starting_values(y[:ix1], x=x[:ix1])
gauss1.guess_starting_values(y[ix1:ix2], x=x[ix1:ix2])
gauss2.guess_starting_values(y[ix2:ix3], x=x[ix2:ix3])

mod = gauss1 + gauss2 + exp_mod

out = mod.fit(y, x=x)

print(mod.fit_report(min_correl=0.5))

plt.plot(x, y)
plt.plot(x, out.init_fit, 'k--')
plt.plot(x, out.best_fit, 'r-')
plt.show()
#<end examples/doc_nistgauss2.py>
