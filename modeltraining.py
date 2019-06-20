from imageai.Prediction.Custom import ModelTraining
import os

my_path = os.getcwd()

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()

model_trainer.setDataDirectory(os.path.join(my_path, "cartier"))
model_trainer.trainModel(num_objects=3, num_experiments=100, enhance_data=True, batch_size=32, show_network_summary=True)
