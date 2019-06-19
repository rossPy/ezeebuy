import os
import base64

from imageai.Prediction import ImagePrediction

execution_path = os.getcwd()
FILENAME = "image.jpg"


def decode_image(img_string, filename=FILENAME):
    imgdata = base64.b64decode(img_string)
    with open(filename, 'wb') as f:
        f.write(imgdata)


def predict_image(img_string):

    prediction = ImagePrediction()
    prediction.setModelTypeAsDenseNet()
    prediction.setModelPath(os.path.join(execution_path, "DenseNet-BC-121-32.h5"))
    prediction.loadModel()

    decode_image(img_string)

    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, FILENAME), result_count=5)
    return zip(predictions, probabilities)