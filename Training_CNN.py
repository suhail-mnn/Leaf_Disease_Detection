import os
from keras.api._v2.keras.applications import InceptionV3
from tensorflow import keras
from keras.layers.core import Flatten, Dense 
import sys
def build_model():
    try:
        class_names = sorted(os.listdir('train'))

        base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        for layers in base_model.layers:
                layers.trainable = False
        
        base_model_output = base_model.output
        x = Flatten()(base_model_output)
        x = Dense(512, activation='relu')(x)
        x = Dense(len(class_names), activation='softmax')(x)
        model = keras.Model(inputs=base_model.input, outputs=x)
        
        model.compile(optimizer = 'sgd', loss ='categorical_crossentropy', metrics = ['accuracy'])

        from keras.preprocessing.image import ImageDataGenerator

        train_datagen = ImageDataGenerator(
                rescale=1/255,
                rotation_range=40,
                horizontal_flip=True,
                vertical_flip=True)

        test_datagen = ImageDataGenerator(rescale=1./255)
        training_set = train_datagen.flow_from_directory(
                'train',
                target_size=(224, 224),
                batch_size=32,
                subset='training',
                class_mode='categorical' )
        label_map = (training_set.class_indices)

        print(label_map)

        test_set = test_datagen.flow_from_directory(
                'val',
                target_size=(224,224),
                batch_size=32,
                subset='validation',
                class_mode='categorical')

        model.fit(
                training_set,
                epochs=10,
                validation_data=test_set,
                )

        print("[INFO] Saving model...")
        try:
            model.save('cnn_model.h5')
            print("[INFO] model saved successfully")
        except Exception as e:
            print("Error=",e)

    except Exception as e:
        print("Error=", e)
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)
