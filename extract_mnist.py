from keras.datasets import mnist
from PIL import Image

(x_train, y_train), (x_test, y_test) = mnist.load_data()

for i in range(0,10000):
    temp = x_test[i]

    path = "/content/drive/My Drive/MNIST_extract/stdp_extract_mycode/test/" + str(y_test[i]) + '/'
    
    img_temp = Image.fromarray(temp)
    img_temp.save(path + str(i) + '.jpg')

for i in range(0,59999):
    temp = x_train[i]

    path = "/content/drive/My Drive/MNIST_extract/stdp_extract_mycode/train/" + str(y_train[i]) + '/'
    
    img_temp = Image.fromarray(temp)
    img_temp.save(path + str(i) + '.jpg')


