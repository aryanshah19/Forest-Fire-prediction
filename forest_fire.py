#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe

import numpy as np
import pandas as pd
#from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("Forest_fire.csv")
data = np.array(data)

X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
classifier = SVC(kernel='linear', random_state=0)  


classifier.fit(X_train, y_train) 

inputt=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]


b = classifier.predict_proba(final)



pickle.dump(classifier,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


