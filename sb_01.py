import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mpl

titanic=sb.load_dataset("titanic")
titanic.to_csv("db_titanic.csv",index=False)
print(titanic)
sb.barplot(x="age",y="embark_town",orient='h',data=titanic)
mpl.show()

sb.barplot(x="embark_town",y="age",data=titanic)
mpl.show()

mpl.scatter("survived","age",data=titanic)
mpl.show()

sb.pointplot(x="sex",y="age",data=titanic)
mpl.show()

sb.swarmplot(x="pclass",y="age",data=titanic)
mpl.show()

iris=sb.load_dataset("iris")
sb.set_style("darkgrid")
sb.kdeplot(iris.loc[(iris['species']=='setosa'),'sepal_length'],color='b',shade=True,Label='setosa')
sb.kdeplot(iris.loc[(iris['species']=='virginica'),'sepal_length'],color='r',shade=True,Label='virginica')
mpl.show()

sb.countplot(x='class',hue='who',data=titanic)
mpl.show()


sb.countplot(x='sex',hue='who',data=titanic,palette="PuRd")
mpl.show()

sb.barplot(x = 'sex', y = 'survived', hue = 'class', data = titanic,palette = 'PuRd',
           order=['male','female'],capsize = 0.05,saturation = 8,errcolor='gray',errwidth=2,
           ci = 'sd')
mpl.legend()
mpl.show()

sb.jointplot(x='sex',y='age',data=titanic)
mpl.show()
##tips=sb.load_dataset('tips')
##print(tips)
