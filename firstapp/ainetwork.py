import numpy as np
from tensorflow import keras


def predict(imageFile):
    #Process images uploaded by users

    classNames=['Пакет', 'Мяч теннисный','Банан','Подшипник','Банка','Конверт','Бутылка','Деньги','Пластиковая бутылка','Игрушка']
    
    modelAi=keras.models.load_model('mmga3.h5')
    img = np.array(keras.preprocessing.image.load_img(imageFile, target_size=(71,71))).astype('float32')/255
    classIndex = np.argmax(modelAi(img.reshape(1,71,71,3)))
                       
    return 'Класс: '+ classNames[classIndex]

