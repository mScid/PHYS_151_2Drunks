import numpy as np
from array import *
from math import factorial
import matplotlib.pyplot as plt

N = int(input("Enter value of N: "))


p = 0.5
q = 0.5
n1 = 0
n2 = 0

m = []
prob = []

while n1 < N+1:
    n2 = N - n1
    m.insert(n1,n1 - n2)
    prob.insert(n1,(factorial(N))/(factorial(n1)*factorial(n2))*(p**n1)*(q**n2))
    n1 += 1


prob2 = prob.copy()

# Total Probability that they will end up together
i = 0
while i < N+1:
    prob2[i] = prob[i]**2
    i += 1


total_probability_together = sum(prob2)

prob3 = prob.copy()

separation = 1

#separation in indices

seps = [0]
sums = [sum(prob2)]
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

#print(prob3)
#print(sum(prob3))

#sums = [sum(prob2),sum(prob3)]
#seps = [0,2]

# Initialize the subplot
figure, axis = plt.subplots(2,2)

# A single drunk
axis [0,0].plot(m, prob, color = "blue")
axis [0,0].set_title("Distribution of the probability of one drunk")

# 2 drunks landing on the same spot
axis [0,1].plot(m, prob2, color = "red")
axis [0,1].set_title("Distribution of the probability that 2 drunks land on the same spot")

axis [1,1].text(0, 0.5," The total probability that they end up together is " + str(total_probability_together))
axis [1,1].text(0, 0.8,"Total probability (for checking): " + str(sum(sums)))

axis [1,0].plot(seps, sums)
axis [1,0].set_title("Plot of probabilities per separation")

plt.show()


#sums = [total_probability_together]
#while separation < 30:
#    j = 0
#    i = 0
#    prob3.pop()
#    while i < 30-separation:
#        prob3[i] = 2*prob[i]*prob[i+separation]
#        i += 1
#    separation += 1
#    print(prob3)
#    sums.append(sum(prob3))
#    prob3 = prob.copy()

#print(total_probability_together)
