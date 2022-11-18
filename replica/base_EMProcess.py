from gaussian import Gaussian
from base import StochasticProcess
from utils import check_positive_number, check_positive_integer
import numpy as np


class BaseEulerMaruyamaProcess(StochasticProcess):

    def __int__(self,  f=None, g=None, initial=0.0, T=1.0, rng=None):
        super().__init__(T=T, rng=rng)
        self.f = f
        self.g = g
        self.initial = initial
        self.n = None
        self.dt = None
        self.times = None


    def _sample_em_process(self, n):
        check_positive_integer(n)

        self.n = n
        self.dt = 1.0 * self.T / self.n
        self.times = np.arange(0.0, self.T + self.dt, self.dt)
        dws = self.rng.normal(scale=np.sqrt(self.dt), size=self.n)
        simulation = [self.initial]
        previous = self.initial

        for (t, dw) in zip(self.times, dws):
            previous += self.f(previous, t) * self.dt + self.g(previous, t) * dw
            simulation.append(previous)

        return simulation

    def sample(self, n):
        return self._sample_em_process(n)