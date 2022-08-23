# mathematical model of changes in space debris
# density due to space policy and cleanup technology
# and the danger of space travel due to space debris density

import numpy as np

# define class for model
class spaceDebris():

    def __init__(self,alpha,beta,gamma,cleanup,baseline):

        self.alpha = alpha        # tunes increase due to collisions
        self.beta = beta          # tunes decrease due to cleanup technology
        self.gamma = gamma        # tunes increase due to colonization
        self.cleanup = cleanup    # cleanup technology
        self.baseline = baseline  # baseline danger
        self.debris = 1           # space debris density
        self.danger = 0           # danger level

    #def euler_colonization(time):
        # captures rate of colonization as a factor of time

        # math here

    def euler_debris(self,stepsize,time):
        # captures change in space debris density

        self.debris += stepsize * (self.alpha * self.debris**2 - self.beta * self.cleanup * time * self.debris**(1/2) + self.gamma) #* self.euler_colonization(time))

    #def euler_danger(self,stepsize):
        # captures danger level of space travel given distance from earth

        #self.danger = self.debris / distance + self.baseline
