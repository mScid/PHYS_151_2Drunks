import numpy
from array import *
from math import factorial
import matplotlib.pyplot as plt

N = 30

p = 0.5
q = 0.5
n1 = 0
n2 = 0

m = []
prob = []

while n1 < 31:
    n2 = N - n1
    m.insert(n1,n1 - n2)
    prob.insert(n1,(factorial(N))/(factorial(n1)*factorial(n2))*(p**n1)*(q**n2))
    n1 += 1

print(prob)

plt.title("Distribution of the probability of one drunk")
plt.xlabel("distance")
plt.ylabel("probability")
plt.plot(m, prob, color = "blue")
plt.show()

prob2 = prob.copy()

i = 0
while i < 31:
    prob2[i] = prob[i]**2
    i += 1

plt.title("Distribution of the probability 2 drunks land on a spot")
plt.xlabel("Distance")
plt.ylabel("Probability")
plt.plot(m, prob2, color = "red")
plt.show()

total_probability_together = sum(prob2)
print(total_probability_together)
