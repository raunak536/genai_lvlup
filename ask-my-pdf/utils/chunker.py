def chunk_text(text, chunksize=500):
    chunks = []
    for i in range(0,len(text), chunksize):
        chunks.append(text[i:i+chunksize])
    return chunks