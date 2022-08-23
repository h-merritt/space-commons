# set up simulation for model of space debris

# import dependencies
import numpy as np
import spaceDebris as sd
import matplotlib.pyplot as plt

# set parameter values
alpha = 1
beta = 1
gamma = 1
cleanup = 1
baseline = 1
duration = 1000
stepsize = 0.1

# set up simulation
def sim(alpha,beta,gamma,cleanup,baseline,duration,stepsize):

    model = sd.spaceDebris(alpha,beta,gamma,cleanup,baseline)

    # record stats
    debris = np.zeros((duration))
    danger = np.zeros((duration))
    time_hist = np.array(range(duration))

    # start time
    time = 0
    # run simulation
    print("begin sim")
    while time < duration:

        print(model.debris)
        # record
        debris[time] = model.debris
        #danger[time] = model.danger

        # euler step debris
        model.euler_debris(stepsize,time)

        # euler step danger
        #model.euler_danger(stepsize)

        time += 1

    # plot model behavior
    # plot change in debris density over time
    #plt.subplot(3,1,1)
    plt.plot(time_hist,debris)

    #plt.subplot(3,1,2)
    #plt.plot(time_hist, danger)

    #plt.subplot(3,1,3)
    #plt.plot(debris, danger)

    plt.show()

sim(alpha,beta,gamma,cleanup,baseline,duration,stepsize)
