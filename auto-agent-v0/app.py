
from utils.openai_client import chat_with_gpt
from tools.calculator import calculate
from tools.search import web_search
from tools.weather import get_weather
import re

tool_map = {'calculate':calculate,
            'web_search':web_search,
            'get_weather':get_weather}

def parse_response(gpt_response):
    action_line = None
    for line in gpt_response.splitlines():
        if "Action" in line:
            action_line = line
    if action_line is None:
        return None,None
    else:
        match = re.search(r".*Action:\s*(\w+)\(\"(.*)\"\)", action_line)
        toolname, argument = match.group(1),match.group(2)
        print(f"Parse response : {toolname, argument}")
        return toolname, argument

if __name__ == '__main__':
    chat_history = [{'role':'system',
                     'content':"""You are an intelligent agent. Your objective is to give answer to  
                     user questions using the following tools if required: 
                     - get_weather(location)
                     - calculate(expression)
                     - web_search(query)
                     
                     Your output should have following 3 fields : 
                    1. Thought: (Think about the user question first)
                    2. Action:  (Use above mentioned tools to get to the answer)
                    2. Observation: (Observe the output of the tools)
                
                    When you have enough information to fully answer the question, just output 1 field:                                
                    1. Final Answer: [your final answer here]
                                
                    Only output Final Answer when you are completely done."""}]

    user_input = input("WELCOME TO AUTO AGENT V0. HOW CAN I HELP YOU?\n")
    chat_history.append({'role': 'user', 'content': user_input})
    c = 0
    if user_input == '/exit':
        print('THANKS FOR USING AUTO AGENT V0!')
    else:
        while True:
            response = chat_with_gpt(chat_history)
            print(f"Iter {c+1} : \n{response.output_text}")
            c+=1
            toolname, argument = parse_response(response.output_text)
            if 'Final Answer' in response.output_text:
                break
            else:
                tool_output = tool_map[toolname](argument)
                chat_history.append({'role':'assistant', 'content':response.output_text + f"\nTool Output : {tool_output}"})


