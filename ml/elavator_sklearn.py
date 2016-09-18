import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
from scipy.signal import find_peaks_cwt

from sklearn import svm, metrics, neighbors, linear_model

def regularise_time(ts, xs, ys, zs):
    t1 = np.arange(ts[0], ts[len(ts) - 1], 0.1)
    x1 = np.interp(t1, ts, xs)
    y1 = np.interp(t1, ts, ys)
    z1 = np.interp(t1, ts, zs)

    return(t1, x1, y1, z1)

t0 = df_accel.index - df_accel.index[0]
t0 = [_t.seconds+float(_t.microseconds)/1000000 for _t in t0]
x0 = df_accel['x']
y0 = df_accel['y']
z0 = df_accel['z']

(t, x, y, z) = regularise_time(t0, x0, y0, z0)

abs_val = []
for i in range(0, len(t)):
    abs_val.append(x[i]*x[i] + y[i]*y[i] + z[i]*z[i])

# Smoothing data
window_size, poly_order = 25, 3

itp = interp1d(t,abs_val, kind='linear')
abs_val_sg = savgol_filter(itp(t), window_size, poly_order)

my_min_snr = 10

indexesAbsUp = find_peaks_cwt(abs_val_sg, np.arange(10, 30))
indexesAbsDown = find_peaks_cwt(-abs_val_sg, np.arange(10, 30))

indexesAll = indexesAbsUp
indexesAll.extend(indexesAbsDown)
indexesAll.sort()

up_times = [107.0, 129.5, 144.0, 166.0, 182.0, 204.0]
down_times = [110.0, 126.0, 147.0, 163.0, 185.0, 201.0]

plt.figure(4)
plt.plot(t, abs_val, 'b-', t, abs_val_sg, 'g-')
plt.ylabel('abs')
plt.xlabel('time')
for this_time in up_times:
    plt.axvline(x = this_time, color = 'k')
for this_time in down_times:
    plt.axvline(x = this_time, color = 'r')

width = 20 # Number of points, ~1s

ups_data = np.zeros((len(up_times), width*2+1))
ups_data_t = np.zeros((len(up_times), width*2+1))
i = 0
for this_time in up_times:
    peakIndex = (np.abs(np.subtract(t, this_time))).argmin()
    ups_data[i, :] = abs_val[(peakIndex - width):(peakIndex + width + 1)]
    ups_data_t[i, :] = np.subtract(t[(peakIndex - width):(peakIndex + width + 1)], t[(peakIndex - width)])
    i += 1

downs_data = np.zeros((len(down_times), width*2+1))
downs_data_t = np.zeros((len(down_times), width*2+1))
i = 0
for this_time in down_times:
    peakIndex = (np.abs(np.subtract(t, this_time))).argmin()
    print this_time, peakIndex
    downs_data[i, :] = abs_val[(peakIndex - width):(peakIndex + width + 1)]
    downs_data_t[i, :] = np.subtract(t[(peakIndex - width):(peakIndex + width + 1)], t[(peakIndex - width)])
    i += 1

rand_times = [95.0, 100.0, 110.0, 150.0, 210.0, 240.0, 90.0, 97.0, 105.0, 250.0]
rand_data = np.zeros((len(rand_times), width*2+1))
rand_data_t = np.zeros((len(rand_times), width*2+1))

i = 0
for this_time in rand_times:
    peakIndex = (np.abs(np.subtract(t, this_time))).argmin()
    rand_data[i, :] = abs_val[(peakIndex - width):(peakIndex + width + 1)]
    rand_data_t[i, :] = np.subtract(t[(peakIndex - width):(peakIndex + width + 1)], t[(peakIndex - width)])
    i += 1

ups_labels = np.ones((len(up_times),1))
downs_labels = np.multiply(np.ones((len(down_times),1)), 2)
rand_labels = np.zeros((len(rand_times), 1))

plt.figure(5)
plt.plot(np.transpose(ups_data_t), np.transpose(ups_data))
plt.ylabel('abs')
plt.xlabel('time')
plt.title('elavator start')

plt.figure(6)
plt.plot(np.transpose(downs_data_t), np.transpose(downs_data))
plt.ylabel('abs')
plt.xlabel('time')
plt.title('elavator stop')

plt.figure(7)
plt.plot(np.transpose(rand_data_t), np.transpose(rand_data))
plt.ylabel('abs')
plt.xlabel('time')
plt.title('no elavator')

# Prepare data for training
data = np.concatenate((ups_data, downs_data, rand_data), axis=0)
labels = np.concatenate((ups_labels, downs_labels, rand_labels), axis=0)
n_samples = len(labels)

shuffled_indices = np.arange(n_samples)
np.random.shuffle(shuffled_indices)

data = data[shuffled_indices,:]
labels = labels[shuffled_indices].astype(int)

training_data = data[:n_samples / 2]
training_labels = labels[:n_samples / 2]

test_labels = labels[n_samples / 2:]
test_data =  data[n_samples / 2:]

knn = neighbors.KNeighborsClassifier()
logistic = linear_model.LogisticRegression()

print('KNN score: %f' % knn.fit(training_data, training_labels).score(test_data, test_labels))
print('LogisticRegression score: %f'
      % logistic.fit(training_data, training_labels).score(test_data, test_labels))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)
classifier.fit(training_data, training_labels)

# Now predict on test
predicted_labels = classifier.predict(test_data)

print("Classification report for SVN %s:\n%s\n"
      % (classifier, metrics.classification_report(test_labels, predicted_labels)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(test_labels, predicted_labels))
