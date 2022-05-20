import pandas as p 
import plotly.express as pe

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np

data = p.read_csv("velocity.csv")



def model(x):
    return 1/(1 + np.exp)
    
X_test = np.linespace(0 , 100 , 200)
chances = model(X_test * lr.coef_ + lr.intercept_).ravel()

plt.plot(X_test , chances , color="black" , linewidth=3)

plt.axhline(y = 0 , color = 'k' , linestyle='-')
plt.axhline(y = 1 , color = 'k' , linestyle='-')


plt.axhline(y = 0.5 , color = 'b' , linestyle='--')
plt.axvline(x=X_test[165] , color='b' , linestyle='--')

plt.ylabel('y')
plt.xlabel('x')
plt.xlim(75,85)
plt.show()
