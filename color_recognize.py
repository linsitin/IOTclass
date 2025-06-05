import requests
import cv2
import numpy as np
from sklearn.cluster import KMeans

def download_image_from_om2m(resource_url, headers=None):
    response = requests.get(resource_url, headers=headers)
    if response.status_code == 200:
        with open("photo.jpg", "wb") as f:
            f.write(response.content)
        print("圖片下載成功！")
        return "photo.jpg"
    else:
        print(f"下載失敗，狀態碼: {response.status_code}")
        return None


#使用OpenCV 和 scikit-learn 做主色偵測（K-means clustering）
def get_dominant_color(image_path, k=3):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (100, 100))  # 縮小加速處理
    image = image.reshape((-1, 3))  # 展平為N×3
    image = np.float32(image)

    # KMeans找主要k種顏色
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)
    colors = kmeans.cluster_centers_.astype(int)
    counts = np.bincount(kmeans.labels_)
    
    # 找最多的那個色
    dominant_color = colors[np.argmax(counts)]
    return dominant_color

def color(rgb): #顏色判斷
    r, g, b = rgb
    if r > 200 and g < 100 and b < 100:
        return "紅色"
    elif g > 200 and r < 100 and b < 100:
        return "綠色"
    elif b > 200 and r < 100 and g < 100:
        return "藍色"
    elif r > 200 and g > 200 and b < 100:
        return "黃色"
    elif r > 200 and g > 200 and b > 200:
        return "白色"
    elif r < 50 and g < 50 and b < 50:
        return "黑色"
    else:
        return "混合色"
    

'''
程式流程:    
image_path = download_image_from_om2m("檔案路徑")
if image_path:
    rgb = get_dominant_color(image_path)
    color_name = color_to_name(rgb)
    print(f"主要顏色為：{color_name}，RGB: {rgb}")
需要套件:
pip install opencv-python numpy scikit-learn pyttsx3 requests
'''

