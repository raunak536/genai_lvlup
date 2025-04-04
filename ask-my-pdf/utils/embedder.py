from openai import OpenAI

def generate_embeddings(text):
    client = OpenAI()
    response = client.embeddings.create(input=text,
                                        model="text-embedding-3-small")

    embedding = response.data[0].embedding
    return embedding