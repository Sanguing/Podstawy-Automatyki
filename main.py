from math import sqrt
import matplotlib.pyplot as plt

a = 1.5
beta = 0.035
tp = 0.1
tk = 3600
h_min = 0
h_max = 5

n = int(tk/tp) + 1

h = [0.0, ]
t = [0.0, ]
qd = [0.05, ]
qo = [0.0, ]

for n_krok in range(1, n):
    t.append(n_krok*tp)
    h.append(max(min(tp*(qd[-1] + qo[-1]) / (a + h[-1]), h_max), h_min))
    qo.append(beta * sqrt(h[-1]))
    qd.append(qd[-1])

plt.plot(t,h)
plt.show()


#print(t)

print(h[-1])
