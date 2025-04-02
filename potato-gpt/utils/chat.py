from openai import OpenAI
client = OpenAI()

def chat_with_gpt(user_input):
	response = client.responses.create(
    		model="gpt-4o",
    		input=str(user_input)
	)
	return response

