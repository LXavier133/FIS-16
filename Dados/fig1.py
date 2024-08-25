import matplotlib.pyplot as plt, numpy as np, scipy.special

f=open("data_dice.txt","r")
lines=f.readlines()
f.close()

data=np.array([int(line.strip()) for line in lines[1:]])

axis=np.arange(0,25)
exp = 100*scipy.special.comb(24,axis)*((1/6)**axis)*((5/6)**(24-axis))


plt.xlabel('n', fontsize=15)
plt.ylabel('contagens', fontsize=15)

plt.hist(data,color="white", edgecolor="black",label="contagens experimentais")
plt.plot(axis,exp,"o",color="black",label="contagens esperadas")

plt.legend(loc="upper right")
plt.show()
