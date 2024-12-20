import os
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

LATEST_MODEL_URL = os.getenv("LATEST_MODEL_URL")
DESTINATION_MODEL_PATH = os.getenv("DESTINATION_MODEL_PATH")

response = requests.get(LATEST_MODEL_URL)

with open(DESTINATION_MODEL_PATH, 'wb') as f:
    f.write(response.content)

model = load_model(DESTINATION_MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify(
                {
                    'success': False,
                    'message': 'No image file found in the request',
                    'response_code': 400,
                    'data': None
                }
            ), 400

        image_file = request.files['image']
        image = Image.open(image_file).convert('L')
        
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)

        predictions = model.predict(image_array)
        
        predictions_list = predictions[0].tolist()
        response = {
            'success': True,
            'message': 'Image recognized successfully',
            'response_code': 200,
            'data': {
                'digit': int(np.argmax(predictions)),
                'probabilities': predictions_list,
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify(
            {
                'success': False,
                'message': str(e),
                'response_code': 500,
                'data': None
            }
        ), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
