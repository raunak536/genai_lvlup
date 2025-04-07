from utils.chat import chat_with_gpt
from utils.embedder import generate_embeddings, get_top_k_chunks
from utils.chunker import chunk_text
from utils.pdf_loader import parse_pdf
from rich import print, prompt
from datetime import datetime

if __name__ == '__main__':
    print("WELCOME TO ASK-MY-PDF")
    chat_history = [{'role':'system',
                     'content':"You are a helpful assistant that answers based on provided documents."}]
    print('Parsing PDF...')
    text = parse_pdf("./data/offer_letter_rk.pdf")
    print('Chunking text...')
    chunks = chunk_text(text)
    print('Generating embeddings...')
    embeddings = [generate_embeddings(chunk) for chunk in chunks]
    user_input = prompt.Prompt.ask("[green]USER : [/green]")
    while user_input != '/exit':
        top_k_chunks = get_top_k_chunks(user_input, chunks, embeddings,top_k=3)
        chat_history.append({"role": 'user', 
                             "content": f"Context : {top_k_chunks}"})
        chat_history.append({"role": 'user', 
                             "content": user_input})
        response = chat_with_gpt(chat_history)
        chat_history.append({"role": 'assistant', 
                             "content": response.output_text})
        print(f"[cyan]ASK-MY-PDF : {response.output_text}[/cyan]")
        user_input = prompt.Prompt.ask("[green]USER : [/green]")
    
    print("[cyan]ASK-MY-PDF: THANK YOU FOR USING ASK-MY-PDF![/cyan]")


        
        

