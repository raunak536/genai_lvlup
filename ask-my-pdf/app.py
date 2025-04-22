from utils.chat import chat_with_gpt
from utils.embedder import generate_embeddings, get_top_k_chunks
from utils.chunker import chunk_text
from utils.pdf_loader import parse_pdf
from rich import print, prompt
import pickle
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'admin123'

# session_chunks = []
# session_embeddings = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_file = request.files['pdf']
        pdf_file.save(f'./uploads/{pdf_file.filename}')
        print('Parsing PDF...')
        text = parse_pdf(f'./uploads/{pdf_file.filename}')
        print('Chunking text...')
        chunks = chunk_text(text)
        print('Generating embeddings...')
        embeddings = [generate_embeddings(chunk) for chunk in chunks]
        
        session['filename'] = pdf_file.filename
        with open(f'./data/chunks_{session['filename'][:-4]}.pkl','wb') as f:
            pickle.dump(chunks, f)
        with open(f'./data/embeddings_{session['filename'][:-4]}.pkl','wb') as f:
            pickle.dump(embeddings, f)

        # session['chunks'] = chunks
        # session['embeddings'] = embeddings

        return redirect(url_for('chat'))
    return render_template('index.html')

@app.route("/chat",methods=['GET','POST'])
def chat():
    # chunks = session.get('chunks')
    # embeddings = session.get('embeddings')
    with open(f'./data/chunks_{session['filename'][:-4]}.pkl','rb') as f:
            chunks = pickle.load(f)
    with open(f'./data/embeddings_{session['filename'][:-4]}.pkl','rb') as f:
        embeddings = pickle.load(f)
    messages = session.get('messages', [])

    if request.method == 'POST':
        user_input = request.form['question']
        top_k_chunks = get_top_k_chunks(user_input, chunks, embeddings, top_k=3)
        chat_history = [{'role':'system',
                        'content':"You are a helpful assistant that answers based on provided documents."}]
        chat_history.append({"role": 'user', 
                             "content": f"Context : {top_k_chunks}"})
        chat_history.append({"role": 'user', 
                             "content": user_input})
        response = chat_with_gpt(chat_history)
        # chat_history.append({"role": 'assistant', 
        #                      "content": response.output_text})
        messages.append(('user',user_input))
        messages.append(('bot',response.output_text))
        session['messages'] = messages

    return render_template('chat.html', messages=messages)

        
        

