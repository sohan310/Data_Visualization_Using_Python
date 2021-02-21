import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

d1=pd.read_csv("Automobile_dataset.csv")

pt.bar(d1["company"],d1["price"])
pt.show()


##----Plotting with marker----
pt.plot(d1["company"],marker="x")
pt.show()


##---horizontal bar chart----
pt.barh(d1["company"],d1["price"])
pt.show()


##---- bar chart with color ----
pt.bar(d1["company"],d1["price"],color="hotpink")
pt.show()


##----histogram---

pt.hist(d1["price"],color="red")
pt.show()

##--- multiline plotting ---
x1=d1["company"]
y1=d1["price"]
y2=d1["wheel-base"]
x1=np.array([1,4,5,10])
y1=np.array([3,5,6,8])
y2=np.array([2,4,5,3])
pt.plot(x1,y1,color="red",marker="o")
pt.plot(x1,y2,color="yellow",marker="x")
pt.show()


##---- pie chart ---

d=d1.groupby("num-of-cylinders").mean()
pt.pie(d["index"])
pt.show() 
