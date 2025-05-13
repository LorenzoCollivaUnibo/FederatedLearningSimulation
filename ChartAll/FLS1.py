import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0" #per disattivare ONEDNN

import tensorflow as tf
print(tf.__version__)

(x_train, y_train), (x_test, y_test)= tf.keras.datasets.mnist.load_data(path='mnist.npz')
assert x_train.shape == (60000, 28, 28)  #60000 immagini 28x28
assert y_train.shape == (60000,)         #60000 label
assert x_test.shape == (10000, 28, 28)   #10000 immagini 28x28
assert y_test.shape == (10000,)          #10000 label


ds_train = tf.data.Dataset.from_tensor_slices((x_train, y_train))  #crea un dataset dove ogni elemento è una tupla (x[i], y[i]) per il ds TRAIN
ds_test = tf.data.Dataset.from_tensor_slices((x_test, y_test))     #crea un dataset dove ogni elemento è una tupla (x[i], y[i]) per il ds TEST

ds_train = ds_train.batch(128)
ds_test = ds_test.batch(128)

#SUDDIVIDO IN TERMINI DI BATCH
num_batch_train_elements = len(ds_train)
div_train = num_batch_train_elements // 2

ds_train1 = ds_train.take(div_train)
ds_train2 = ds_train.skip(div_train)

print("n batch client 1: ", len(ds_train1))
print("n batch client 2: ", len(ds_train2))


#CREO E ADDESTRO IL MODELLO
#costruzione modello (rete neurale contenuta in model)
def create_model():
    model = tf.keras.models.Sequential([ #modello sequenziale (ogni layer riceve l'output del layer precedente) in keras
        tf.keras.layers.Input(shape=(28, 28)), #appiattisce l'input (immagine di dimensioni MNIST matrice 28x28) in un vettore unidimensionale di 784 elementi
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'), #crea uno strato denso (connesso con il layer precedente) di 128 nodi e come funzione di attivazione la ReLU
        tf.keras.layers.Dense(10) #crea un altro strato denso con 10 nodi (classi finali del ds), no funzione di attivazione è l'output
    ])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(0.001),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),   #Softmax trasforma i logits in probabilità
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
    )
    return model


rounds_number = 10
clients_number = 2

global_model = create_model()
client_models = []

client_model1 = create_model()
client_model2 = create_model()
rounds = []
accuracy = []

loss, s_cat_acc = global_model.evaluate(ds_test, verbose=1)
print(f"Loss modello globale: {loss}")
print(f"Sparse categorical accuracy modello globale: {s_cat_acc}")


print(global_model.metrics_names)

for r in range(rounds_number):
    print(f"Round {r+1}")
    client_model1.set_weights(global_model.get_weights())
    client_model2.set_weights(global_model.get_weights())

    client_model1.fit(ds_train1, epochs=1, validation_data=ds_test)
    client_model2.fit(ds_train2, epochs=1, validation_data=ds_test)

    weight1=client_model1.get_weights()
    weight2=client_model2.get_weights()

    # Usa una list comprehension
    new_global_weight = [
        (len(ds_train1) / len(ds_train)) * w1 + (len(ds_train2) / len(ds_train)) * w2
        for w1, w2 in zip(weight1, weight2)
    ]

    global_model.set_weights(new_global_weight)
    loss, s_cat_acc = global_model.evaluate(ds_test, verbose=0)
    print(f"Sparse categorical accuracy modello globale: {s_cat_acc}")
    rounds.append(r + 1)
    accuracy.append(s_cat_acc)


loss, s_cat_acc = global_model.evaluate(ds_test, verbose=1)
print(f"Loss modello globale: {loss}") #indica quanto sbaglia e con quanta sicurezza
print(f"Sparse categorical accuracy modello globale: {s_cat_acc}") #percentuale di accuratezza della risposta


def get_data1():
    return clients_number, rounds, accuracy