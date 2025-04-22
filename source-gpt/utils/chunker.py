def chunk_text(text_with_metadata, chunksize=500):
    all_chunks = []
    chunk_id = 1
    for page_num, text in text_with_metadata:
        for i in range(0,len(text), chunksize):
            chunk = {'chunk_id':chunk_id,
                     'page_num': page_num,
                     'chunk_text':text[i:i+chunksize]}
            all_chunks.append(chunk)
            chunk_id+=1
    return all_chunks