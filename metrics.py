
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
import numpy as np

y_true = np.array([50, 60, 70, 80])
y_pred = np.array([48, 62, 68, 85])

mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse) 
r2 = r2_score(y_true, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)
