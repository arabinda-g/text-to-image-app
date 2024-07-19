from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import torch
from diffusers import StableDiffusionPipeline
import os

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/text_to_image"
mongo = PyMongo(app)

# Load the Stable Diffusion model
model_path = "models/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(model_path)
pipe = pipe.to(device)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    text_prompt = data.get('prompt')
    
    # Generate image
    with torch.no_grad():
        image = pipe(text_prompt).images[0]
    
    # Save it
    if not os.path.exists('static'):
        os.makedirs('static')
    image_path = f"static/{text_prompt.replace(' ', '_')}.png"
    image.save(image_path)
    
    # Insert to DB
    image_record = {
        "prompt": text_prompt,
        "image_path": image_path
    }
    image_id = mongo.db.images.insert_one(image_record).inserted_id
    
    return jsonify({"id": str(image_id), "image_url": f"http://localhost:5000/{image_path}"})

@app.route('/get-image/<id>', methods=['GET'])
def get_image(id):
    image_record = mongo.db.images.find_one({"_id": ObjectId(id)})
    if image_record:
        return jsonify({
            "id": str(image_record['_id']),
            "prompt": image_record['prompt'],
            "image_url": f"http://localhost:5000/{image_record['image_path']}"
        })
    else:
        return jsonify({"error": "Image not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
