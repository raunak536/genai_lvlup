from utils.chat import chat_with_gpt

if __name__ == '__main__':
	print("WELCOME TO POTATO-GPT")
	persona = 'default'
	system_prompt = open(f'prompts/{persona}_prompt.txt').read()
	chat_history = [{'role':'assistant','content':system_prompt}]
	user_input = input("USER : ")
	chat_history.append({'role':'user', 'content':user_input})
	while user_input != '/exit':
		response = chat_with_gpt(chat_history)
		chat_history.append({"role": 'assistant', "content": response.output_text})
		print(f"POTATO-GPT : {response.output_text}")
		user_input = input("USER : ")
		if user_input == '/funny':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history.append({'role':'assistant', 'content':system_prompt})
			user_input = input("USER : ")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/wise':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history.append({'role':'assistant', 'content':system_prompt})
			user_input = input("USER : ")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/depressed':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history.append({'role':'assistant', 'content':system_prompt})
			user_input = input("USER : ")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/bully':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history.append({'role':'assistant', 'content':system_prompt})
			user_input = input("USER : ")
			chat_history.append({'role':'user', 'content':user_input})
		else:
			pass
		chat_history.append({ "role": "user", "content": user_input})

	print("THANK YOU FOR USING POTATO-GPT!")