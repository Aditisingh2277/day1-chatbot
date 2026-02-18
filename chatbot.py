from google import genai 
from google.genai import types
import os #to read environment variable
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env') #load .env file,  reads the api key from .env file

API_KEY=os.environ["GEMINI_API_KEY"] 


#create a client to talk too google genai
client = genai.Client(api_key=API_KEY)


#ask the model to generate content
response=client.models.generate_content(
    model='gemini-2.5-flash',
    
    contents='Hi , I am Aditi, currently i am exploring ai and tech field. write a short bio about me.'
    
    )

print(response.text)