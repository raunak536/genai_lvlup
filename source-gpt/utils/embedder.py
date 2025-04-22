from openai import OpenAI
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def generate_embeddings(text):
    client = OpenAI()
    response = client.embeddings.create(input=text,
                                        model="text-embedding-3-small")

    embedding = response.data[0].embedding
    return embedding

def get_top_k_chunks(query, chunks, top_k=3):
    query_vec = np.array(generate_embeddings(query)).reshape(1, -1)
    
    #added this on top of ask-my-gpt
    chunk_embeddings = []
    for chunk in chunks:
        chunk_embeddings.append(chunk['embedding'])

        
    chunk_vecs = np.array(chunk_embeddings)

    # Compute cosine similarity
    similarities = cosine_similarity(query_vec, chunk_vecs)[0]

    # Get indices of top_k scores
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    # Return matching chunks
    top_chunks = [chunks[i] for i in top_indices]
    return top_chunks