import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, render_template, request, url_for
from PIL import Image

# Load the converted Keras model
model = keras.models.load_model("mnist_cnn_model.h5")

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def preprocess_image(image):
    """Preprocess the uploaded image to match MNIST format."""
    image = image.convert("L")  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to 28x28
    image_array = np.array(image)
    image_array = 255 - image_array  # Invert colors (MNIST format expects white digits on black)
    image_array = image_array / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=(0, -1))  # Add batch & channel dimensions
    return image_array

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None  # Track uploaded image file name

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            filename = file.filename  # Get uploaded file name
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)  # Save uploaded image

            # Process and predict
            image = Image.open(file)
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_digit = int(np.argmax(prediction))  # Get the most likely digit

            return render_template("index.html", prediction=predicted_digit, filename=filename)

    return render_template("index.html", prediction=prediction, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
