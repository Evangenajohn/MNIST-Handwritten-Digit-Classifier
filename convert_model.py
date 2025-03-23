import pickle
import tensorflow as tf

# Step 1: Load the Pickle Model
with open("mnist_cnn_model.pkl", "rb") as f:
    model = pickle.load(f)  # Load the model from pickle file

# Step 2: Save the Model in HDF5 Format
model.save("mnist_cnn_model.h5")

print("Model successfully converted to HDF5 format!")
