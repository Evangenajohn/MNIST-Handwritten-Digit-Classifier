# MNIST-Handwritten-Digit-Classifier
This project is a Flask-based web application that classifies handwritten digits using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Users can upload an image of a digit, and the model predicts the number.

## 🚀 Demo

You can try the live demo here: [Add your deployment link if hosted]

## 📌 Features

- Upload a handwritten digit image
- Preprocessing of the image to match MNIST format
- Predict the digit using a trained CNN model
- Simple web interface built with Flask

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mnist-digit-classifier.git
   cd mnist-digit-classifier
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## 📁 Project Structure
```
mnist-digit-classifier/
│── templates/
│   ├── index.html  # Web UI
│── static/
│── app.py  # Flask app
│── mnist_cnn_model.h5  # Trained CNN model
│── requirements.txt  # Python dependencies
│── README.md  # Project documentation
```

## 📖 How It Works

1. User uploads an image of a handwritten digit.
2. The image is preprocessed (grayscale, resized, normalized).
3. The CNN model predicts the digit.
4. The predicted digit is displayed on the web page.

## 🏗 Model Details

- **Dataset**: MNIST (60,000 training, 10,000 testing images)
- **Architecture**:
  - Convolutional Layers
  - Max Pooling
  - Fully Connected Layers
  - Softmax Activation
- **Frameworks**: TensorFlow, Keras

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 📞 Contact

- **Your Name**: [Evangelin G]
- **Email**: [eg5157@srmist.edu.in]

---
⭐ If you like this project, feel free to give it a star!

