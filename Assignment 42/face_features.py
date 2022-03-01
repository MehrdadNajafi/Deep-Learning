import os
import csv
from tqdm import tqdm
from deepface import DeepFace

def create_FaceFeatures(folders_path):
    embeddings = []
    for folder_path in folders_path:
        for img_path in tqdm(os.listdir(folder_path)):
            embedding = DeepFace.represent(img_path = f"{folder_path}/{img_path}", model_name = 'ArcFace', enforce_detection=False)
            embedding.insert(0, folder_path)
            embeddings.append(embedding)
    
    with open('FaceFeatures.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write multiple rows
        writer.writerows(embeddings)