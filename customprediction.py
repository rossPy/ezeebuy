from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "cartier", "models", "model_ex-031_acc-0.614583.h5"))
prediction.setJsonPath(os.path.join(execution_path, "cartier", "json", "model_class.json"))
prediction.loadModel(num_objects=3)

predictions, probabilities = prediction.predictImage("image.png", result_count=1)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)