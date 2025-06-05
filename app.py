
from flask import Flask, request, jsonify
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import io

app = Flask(__name__)

def get_dominant_color(image_bytes, k=3):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize((150, 150))  # 縮小加速
    img_array = np.array(image)
    img_array = img_array.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(img_array)
    colors = kmeans.cluster_centers_.astype(int)

    # 取出最常出現的那個群心
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant = colors[np.argmax(counts)]
    return dominant.tolist()

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    file.save("test.jpg")
    image_bytes = file.read()
    dominant_color = get_dominant_color(image_bytes)
    return jsonify({'dominant_color': dominant_color})

if __name__ == '__main__':
    #ifconfig IP位址
    app.run(host='0.0.0.0', port=5000)
