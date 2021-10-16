import os
import io
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont

API_KEY = os.environ["AZURE_FACIAL_RECOGNITION_KEY1"]
ENDPOINT = "https://jade-fjestad-squid-game.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))