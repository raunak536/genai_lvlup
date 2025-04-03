from openai import OpenAI, api_key
client = OpenAI()

def chat_with_gpt(user_input):
	response = client.responses.create(
    		model="gpt-4o-mini",
    		input=str(user_input)
	)
	return response

