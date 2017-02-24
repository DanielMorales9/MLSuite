import matplotlib.pyplot as plt
from numpy import arange, array, append
from classification.fast_neural_network import FastNeuralNetwork as FNN
from demo.classification.fast_neural_network.kaggle.store import getStoreInstance
from utility import FeatureAugmentation as FA
from normalization import MeanNormalization

backoff1 = [2 ** i for i in arange(0, 11)]
hidden_units = 128

x, y = getStoreInstance().loadDataset('data/train.csv', isShuffle=True)
m = len(x)
idx_train = int(m * 0.60)
idx_test = int(m * 0.80)
x = FA.map2(x, degree=3)
x = MeanNormalization().scale(x)
x_train = x[:idx_train, :]
y_train = y[:idx_train]
x_val = x[idx_train:idx_test, :]
y_val = y[idx_train:idx_test]
x_test = x[idx_test:, :]
y_test = y[idx_test:]

fnn = FNN()
error_train = array([])
error_val = array([])

for i in backoff1:
    fnn.fit(x_train, y_train, i, l=1.28)
    j_train = fnn.compute_cost(x_train, y_train)
    error_train = append(error_train, j_train)
    j_val = fnn.compute_cost(x_val, y_val)
    error_val = append(error_val, j_val)

plt.plot(backoff1, error_train, linewidth=2)
plt.plot(backoff1, error_val, linewidth=2)
legend = ["Error Train", "Error CV"]
plt.ylabel("Error")
plt.xlabel("Number of hidden units (hu)")
plt.legend(legend)
plt.title("Learning curve for neural network.")
plt.show()
