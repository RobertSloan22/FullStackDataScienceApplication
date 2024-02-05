from flask import Flask, request, jsonify, render_template, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image, ImageEnhance
import numpy as np
import io

app = Flask(__name__)
app.secret_key = '123456789' 

# Load your trained model
model = load_model('digit_recognition_model.h5')

@app.route('/')
def index():
    session['predictions'] = []  # Initialize/reset the predictions list at the start of the session
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided.'}), 400
    image = request.files['image']
    image = Image.open(io.BytesIO(image.read()))
    image = image.convert('L')  # Convert to grayscale
    
    # Enhance the image (optional, can be adjusted or omitted)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Increase contrast

    image = image.resize((32, 32))  # Resize to match the model's expected input
    image = img_to_array(image)
    image = image.reshape(1, 32, 32, 1)  # Reshape for the model
    image = image.astype('float32')
    image /= 255.0  # Normalize

    prediction = model.predict(image)
    digit = np.argmax(prediction, axis=1)[0]  # model outputs one-hot encoded predictions

    # Add the prediction to the session
    if 'predictions' not in session:
        session['predictions'] = []
    session['predictions'].append(int(digit))

    # Return both the prediction and the history of predictions
    return jsonify({'prediction': int(digit), 'history': session['predictions']})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image, ImageEnhance
import numpy as np
import io

app = Flask(__name__)
app.secret_key = '123456789' 

# Load your trained model
model = load_model('digit_recognition_model.h5')

@app.route('/')
def index():
    session['predictions'] = []  # Initialize/reset the predictions list at the start of the session
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided.'}), 400
    image = request.files['image']
    image = Image.open(io.BytesIO(image.read()))
    image = image.convert('L')  # Convert to grayscale
    
    # Enhance the image (optional, can be adjusted or omitted)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Increase contrast

    image = image.resize((32, 32))  # Resize to match the model's expected input
    image = img_to_array(image)
    image = image.reshape(1, 32, 32, 1)  # Reshape for the model
    image = image.astype('float32')
    image /= 255.0  # Normalize

    prediction = model.predict(image)
    digit = np.argmax(prediction, axis=1)[0]  # model outputs one-hot encoded predictions

    # Add the prediction to the session
    if 'predictions' not in session:
        session['predictions'] = []
    session['predictions'].append(int(digit))

    # Return both the prediction and the history of predictions
    return jsonify({'prediction': int(digit), 'history': session['predictions']})

if __name__ == '__main__':
    app.run(debug=True)
