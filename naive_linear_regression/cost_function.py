import numpy as np
import math

training_sets = [(1, 1), (2, 2), (3, 3)]
theta0 = 0
theta1 = 0


def predict(x):
    return theta0 * x + theta1


prediction_values = []
differences = []
for a_set in training_sets:
    y = a_set[1]
    prediction_y = predict(a_set[0])
    diff = prediction_y - y
    print("diff", diff)
    diff_squared = diff * diff
    print("diff square", diff_squared)
    differences.append(diff_squared)

total_difference = sum(differences) / (len(training_sets) * 2)
print("sum diff", sum(differences))
print("total_difference", total_difference)
results = (theta0, theta1)
