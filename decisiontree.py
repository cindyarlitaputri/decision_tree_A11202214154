import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt



# Membaca dataset
data = pd.read_csv('diabetes.csv', delimiter=',', header=0)

# Memastikan kolom 'Sentimen' ada dan diubah menjadi integer
data["Insulin"] = pd.factorize(data["Insulin"])[0]


# Verifikasi dataset
# print(data.head())
# print(data.info())

# Mengubah dataset menjadi array numpy
data = data.to_numpy()

# Membagi dataset menjadi atribut dan label
inputData = data[:, :-1]  # Semua kolom kecuali terakhir
labelData = data[:, -1]   # Kolom terakhir sebagai label

# Menggunakan data yang sama untuk training dan testing
inputTraining = inputData
labelTraining = labelData
inputTesting = inputData
labelTesting = labelData

# Mendefinisikan decision tree classifier
model = tree.DecisionTreeClassifier()

# Melatih model
model = model.fit(inputTraining, labelTraining)

# Memprediksi label
hasilPrediksi = model.predict(inputTesting)
print("Hasil prediksi: ", hasilPrediksi)
print("Label sebenarnya: ", labelTesting)

# Menghitung akurasi
prediksiBenar = (hasilPrediksi == labelTesting).sum()
prediksiSalah = (hasilPrediksi != labelTesting).sum()
print("Prediksi benar: ", prediksiBenar, "data")
print("Prediksi salah: ", prediksiSalah, "data")
print("Akurasi: ", prediksiBenar / (prediksiBenar + prediksiSalah) * 100, "%.")


# Visualisasi pohon keputusan
plt.figure(figsize=(20, 10))
tree.plot_tree(model, filled=True, feature_names=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                                                  "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"], 
               class_names=["No Diabetes", "Diabetes"])
plt.title("Decision Tree Visualization")
plt.show()