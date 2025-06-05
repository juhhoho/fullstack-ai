from flask import Flask, request, jsonify
import cv2
import numpy as np
import requests

app = Flask(__name__)

def fetch_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image"):
            image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
            if image is None:
                return None, "Failed to decode image"
            return image, None
        else:
            return None, f"Invalid content type: {response.headers.get('Content-Type')}"

    except requests.exceptions.RequestException as e:
        return None, str(e)

def normalize_image_size(image1, image2):
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]
    
    target_height = min(height1, height2)
    target_width = min(width1, width2)
    
    image1_resized = cv2.resize(image1, (target_width, target_height), interpolation=cv2.INTER_AREA)
    image2_resized = cv2.resize(image2, (target_width, target_height), interpolation=cv2.INTER_AREA)
    
    return image1_resized, image2_resized

def compute_image_similarity(image1, image2):
    # Convert images to HSV color space
    image1_hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    image2_hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    # Calculate histograms
    hist1 = cv2.calcHist([image1_hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist2 = cv2.calcHist([image2_hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])

    # Normalize histograms
    hist1 = cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
    hist2 = cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)

    # Calculate similarity using Bhattacharyya distance
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    
    return similarity

@app.route('/compare_images', methods=['POST'])
def compare_images():
    data = request.get_json()

    if 'url1' not in data or 'url2' not in data:
        return jsonify({"error": "Both image URLs are required"}), 400

    # Fetch images from URLs
    image1, error1 = fetch_image(data['url1'])
    image2, error2 = fetch_image(data['url2'])

    if image1 is None or image2 is None:
        return jsonify({"error": "Invalid image data"}), 400
    
    # Normalize image sizes
    image1, image2 = normalize_image_size(image1, image2)
    
    # Calculate similarity score
    similarity = compute_image_similarity(image1, image2)
    score = round((1 - similarity) * 100, 2)

    return jsonify({
        "score": score
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
