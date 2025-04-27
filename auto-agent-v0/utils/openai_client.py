import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv('/Users/72625/Documents/general/genai_lvlup/.env')
import sys
sys.path.append('..')

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def chat_with_gpt(user_input):
	response = client.responses.create(
    		model="gpt-4o-mini",
    		input=str(user_input)
	)
	return response

