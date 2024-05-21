# lib analysis statistic
import scipy.stats as sc
import statsmodels.api as sm

# lib model evaluations
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

def evaluations(y_test, predictions):
  mae = mean_absolute_error(y_test, predictions) * 100
  mse = mean_squared_error(y_test, predictions) * 100
  mape = mean_absolute_percentage_error(y_test, predictions) * 100
  return mae, mse, mape