from utils.chat import chat_with_gpt

if __name__ == '__main__':
	print("WELCOME TO POTATO-GPT")
	user_input = input("USER : ")
	while user_input != '/exit':
		response = chat_with_gpt(user_input)
		print(f"POTATO-GPT : {response.output_text}")
		user_input = input("USER : ")
	print("THANK YOU FOR USING POTATO-GPT!")
