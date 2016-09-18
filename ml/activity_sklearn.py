import matplotlib.pyplot as plt
import numpy as np

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

rest_times = np.concatenate((np.arange(10.0, 65, 6), np.arange(235.1, 290, 6)))
active_times = np.concatenate((np.arange(70.1, 104, 6), [110, 120, 126, 132, 138, 148, 154, 230, 235],
                               np.arange(206, 224, 6), np.arange(166, 180, 6), np.arange(186, 198, 6)))

plt.figure(1)
plt.plot(t, abs_val, 'b-', t, abs_val, 'g-')
plt.xlabel('time')
plt.ylabel('abs')
for this_time in rest_times:
    plt.axvline(x = this_time, color = 'k')
for this_time in active_times:
    plt.axvline(x = this_time, color = 'r')
plt.ylabel('abs')
plt.xlabel('time')

width = 20 # Number of points, ~1s

rest_data = np.zeros((len(rest_times), width*2+1))
rest_data_t = np.zeros((len(rest_times), width*2+1))
i = 0
for this_time in rest_times:
    peakIndex = (np.abs(np.subtract(t, this_time))).argmin()
    rest_data[i, :] = abs_val[(peakIndex - width):(peakIndex + width + 1)]
    rest_data_t[i, :] = np.subtract(t[(peakIndex - width):(peakIndex + width + 1)], t[(peakIndex - width)])
    i += 1

rest_labels = np.zeros((len(rest_times),1))

active_data = np.zeros((len(active_times), width*2+1))
active_data_t = np.zeros((len(active_times), width*2+1))
i = 0
for this_time in active_times:
    peakIndex = (np.abs(np.subtract(t, this_time))).argmin()
    active_data[i, :] = abs_val[(peakIndex - width):(peakIndex + width + 1)]
    active_data_t[i, :] = np.subtract(t[(peakIndex - width):(peakIndex + width + 1)], t[(peakIndex - width)])
    i += 1

active_labels = np.ones((len(active_times),1))

plt.figure(2)
plt.plot(np.transpose(rest_data_t), np.transpose(rest_data))
plt.ylabel('abs')
plt.xlabel('time')
plt.title('no activity')

plt.figure(3)
plt.plot(np.transpose(active_data_t), np.transpose(active_data))
plt.ylabel('abs')
plt.xlabel('time')
plt.title('activity')

# Prepare data for training
data = np.concatenate((rest_data, active_data), axis=0)
labels = np.concatenate((rest_labels, active_labels), axis=0)
n_samples = len(labels)

shuffled_indices = np.arange(n_samples)
np.random.shuffle(shuffled_indices)

data = data[shuffled_indices,:]
labels = labels[shuffled_indices]

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
