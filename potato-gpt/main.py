from utils.chat import chat_with_gpt
from rich import print, prompt
from datetime import datetime

if __name__ == '__main__':
	print("WELCOME TO POTATO-GPT")
	choice = prompt.Prompt.ask(f"[bold yellow]Choose a persona : \n1.Default\n2.Funny\n3.Wise\n4.Depressed\n5.Bully[/bold yellow]\n")
	choice = int(choice)
	if choice==1:
		system_prompt = open(f'prompts/default_prompt.txt').read()
	elif choice==2:
		system_prompt = open(f'prompts/funny_prompt.txt').read()
	elif choice==3:
		system_prompt = open(f'prompts/wise_prompt.txt').read()
	elif choice==4:
		system_prompt = open(f'prompts/depressed_prompt.txt').read()
	elif choice==5:
		system_prompt = open(f'prompts/bully_prompt.txt').read()
	else:
		raise Exception(f"Incorrect option!")
	chat_history = [{'role':'system','content':system_prompt}]
	user_input = prompt.Prompt.ask("[green]USER : [/green]")
	while user_input != '/exit':
		response = chat_with_gpt(chat_history)
		chat_history.append({"role": 'assistant', "content": response.output_text})
		print(f"[cyan]POTATO-GPT : {response.output_text}[/cyan]")
		user_input = prompt.Prompt.ask("[green]USER : [/green]")
		if user_input == '/funny':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history[0] = {'role':'system', 'content':system_prompt}
			user_input = prompt.Prompt.ask("[green]USER : [/green]")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/wise':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history[0] = {'role':'system', 'content':system_prompt}
			user_input = prompt.Prompt.ask("[green]USER : [/green]")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/depressed':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history[0] = {'role':'system', 'content':system_prompt}
			user_input = prompt.Prompt.ask("[green]USER : [/green]")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/bully':
			system_prompt = open(f'prompts/{user_input[1:]}_prompt.txt').read()
			chat_history[0] = {'role':'system', 'content':system_prompt}
			user_input = prompt.Prompt.ask("[green]USER : [/green]")
			chat_history.append({'role':'user', 'content':user_input})
		elif user_input == '/save':
			save_text = ""
			for chat in chat_history:
				save_text += chat['role'] + ': ' + chat['content'] + '\n'
			with open(f"chat_history/log_{datetime.now()}.txt",'w') as f:
				f.write(save_text)
			break
		else:
			chat_history.append({ "role": "user", "content": user_input})

	print("[cyan]POTATO-GPT: THANK YOU FOR USING POTATO-GPT![/cyan]")