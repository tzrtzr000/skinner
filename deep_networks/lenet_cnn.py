
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD

def lenet_cnn(selected_metrics, input_size):

    if len(selected_metrics)==1:
        selected_metrics = [selected_metrics]

    # First block of layers: Convolutional + ReLU + Max pooling
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, input_shape=(3, input_size[0], input_size[1])))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Second block of layers: Convolutional + ReLU + Max pooling
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Third block of layers: Convolutional + ReLU + Max pooling
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Fully connected layers
    model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    # Close the network indicating binary cross entropy, using rmsprop as the optimizer
    # and using accuracy as quality measure
    sgd = SGD(lr=0.001, clipnorm=1.)
    model.compile(loss='binary_crossentropy',
                  optimizer=sgd,
                  metrics=selected_metrics)

    return model
