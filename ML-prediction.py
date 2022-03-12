import numpy as np
import argparse
import matplotlib.pyplot as plt
from sklearn.svm import SVR

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Ready to use"

parser = argparse.ArgumentParser(description='SVR')
parser.add_argument(
    '--file', type=str, default='Jlee-PRB-2016-270materials.csv')
parser.add_argument(
    '--validation', type=float, default=0.2)


def data_load(filename):
    data = None
    with open(filename) as f:
        data = np.loadtxt(f, delimiter=',', skiprows=1)
    return data


def train(trains, labels):
    regression = SVR(C=1.0, verbose=True, tol=1e-4)
    regression.fit(trains, labels)
    return regression


def plot(slot1, slot2):
    plt.bar(np.arange(slot1.shape[0]), slot1)
    plt.bar(np.arange(slot2.shape[0]), slot2, alpha=0.5)
    plt.savefig("bar_graph.png")


if __name__ == "__main__":
    args = parser.parse_args()
    data = data_load(args.file)
    print(data[:, 0].min(), data[:, 0].max())
    validateLabels = data[:int(args.validation * data.shape[0]), 0]
    validateData = data[:int(args.validation * data.shape[0]), 1:]
    trainLabels = data[int(args.validation * data.shape[0]):, 0]
    trainData = data[int(args.validation * data.shape[0]):, 1:]
    model = train(trainData, trainLabels)
    predicted = model.predict(validateData)
    plot(predicted, validateLabels)
    print(model.score(validateData, validateLabels))
