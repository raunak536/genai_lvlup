from utils.chat import chat_with_gpt

if __name__ == '__main__':
	print("WELCOME TO POTATO-GPT")
	chat_history = [{'role':'assistant','content':'You are a helpful assistant.'}]
	user_input = input("USER : ")
	chat_history.append({'role':'user', 'content':user_input})
	while user_input != '/exit':
		response = chat_with_gpt(chat_history)
		chat_history.append({"role": 'assistant', "content": response.output_text})
		print(f"POTATO-GPT : {response.output_text}")
		user_input = input("USER : ")
		chat_history.append({ "role": "user", "content": user_input })

	print("THANK YOU FOR USING POTATO-GPT!")