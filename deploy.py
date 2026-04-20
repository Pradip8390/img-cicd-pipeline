import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'face-detection-input'

def upload_images():
    folder = 'images'
    
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        
        if os.path.isfile(file_path):
            print(f"Uploading {file}...")
            s3.upload_file(file_path, BUCKET_NAME, file)
            print(f"{file} uploaded successfully!")

if __name__ == "__main__":
    upload_images()
