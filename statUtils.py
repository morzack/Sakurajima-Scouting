from sklearn import linear_model
import math

def nan_in_list(l):
    for i in l:
        if math.isnan(i):
            return True
    return False

def perform_regression(data, features, target):
    reg = linear_model.LinearRegression()
    x = []
    y = []

    for _, data_row in data.iterrows():
        x_adding = [data_row[i] for i in features]
        y_adding = data_row[target]
        if not nan_in_list(x_adding) and not nan_in_list([y_adding]):
            x.append(x_adding)
            y.append(y_adding)
    reg.fit(x, y)

    return reg, reg.score(x, y)