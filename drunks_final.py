# Importing libraries
import numpy as np
from array import *
from math import factorial
import matplotlib.pyplot as plt

# Asking for input of N. Integer.
N = int(input("Enter value of N: "))

# p and q are the values for the probability of going left an right respectively
p = 0.5
q = 0.5
# this is just for the initialization
n1 = 0
n2 = 0
m = []
prob = []

# This is the loop for the creation of the array for the positions of one drunk
# m is the array containing the possible positions of the drunk
# prob is the probability for the drunk to be at position with the same index in array m
# I had problems using 2 dimensional array but the is certainly better than using 2 separate array
# In hindsight, that makes it easier for me to copy the whole array in the loop after this (prob2 = prob.copy())
while n1 < N+1:
    n2 = N - n1
    m.insert(n1,n1 - n2)
    prob.insert(n1,(factorial(N))/(factorial(n1)*factorial(n2))*(p**n1)*(q**n2))
    n1 += 1

# copying the array
# prob2 = prob will only link the two meaning if changes are made in prob2, it will also affect prob
prob2 = prob.copy()

# This is the loop that solves the possibility that 2 drunks land on the same place
# Notice that it is just the same array multiplied by itself since the second drunk have the same probabilty as the first
i = 0
while i < N+1:
    prob2[i] = prob[i]**2
    i += 1

#sum of the probabilites in array prob2. This is, well, total probability together
total_probability_together = sum(prob2)

# copying array prob again
prob3 = prob.copy()

# separation in indices. This is not the separation of their distance. Their seperation in distance is different but we can get away with one
# since the array is automatically separated in two.
separation = 1

# initialization
seps = [0]
sums = [sum(prob2)]

# loop for creating the probability for separation from separation = 2 to separation = N*2 
while separation < N:
    prob3.pop()
    i = 0
    while i < N+1 - separation:
        prob3[i] = 2*prob[i]*prob[i+separation]
        i += 1
    seps.append(separation*2)
    sums.append(sum(prob3))
    separation += 1

print(sum(sums))

# Initialize the subplot
figure, axis = plt.subplots(2,2)

# A single drunk
axis [0,0].plot(m, prob, color = "blue")
axis [0,0].set_title("Distribution of the probability of one drunk")

# 2 drunks landing on the same spot
axis [0,1].plot(m, prob2, color = "red")
axis [0,1].set_title("Distribution of the probability that 2 drunks land on the same spot")

# Text
axis [1,1].text(0, 0.5," The total probability that they end up together is " + str(total_probability_together))
axis [1,1].text(0, 0.8,"Total probability (for checking): " + str(sum(sums)))

# plot of separation distance vs the probability they end up there
axis [1,0].plot(seps, sums)
axis [1,0].set_title("Plot of probabilities per separation")

# display the plot
plt.show()
