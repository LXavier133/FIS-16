import numpy as np, matplotlib.pyplot as plt, math

def gaussian(x,x0,variance):
	return (1 / (np.sqrt(2 * np.pi * variance))) * np.exp(-((x - x0) ** 2) / (2 * variance))


f=open("data_photogate.txt","r") 
lines=f.readlines()
f.close()

data=np.array([float(line.strip().split("\t")[0]) for line in lines[2:]])
xm= np.mean(data)
x2m=np.mean(data**2)
variance = x2m - xm**2
mini,maxi=np.min(data), np.max(data)

d=max(xm-mini,maxi-xm)
x= np.linspace(xm-d,xm+d,1000)
y= gaussian(x,xm,variance)

plt.xlabel("T(s)")
plt.ylabel("frequência")
plt.title("Histograma - Fotodiodo")


plt.hist(data,bins=math.ceil(1+math.log2(len(data))),edgecolor="black",color="white",density=True,label="frequência exp.")

plt.plot(x,y,color="black",label="gaussiana")

plt.legend(loc="upper right")
plt.show()

