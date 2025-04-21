import os
from openai import OpenAI
import textwrap

client = OpenAI(
    api_key=os.getenv("MODEL_API_KEY"),
    base_url=os.getenv("MODEL_API_URL")
)

def chunk_text(text:str, max_chunk_size=1000, overlap=100):
    """
    Split text into manageable chunks with optional overlap
    
    Args:
    - text (str): Input text to chunk
    - max_chunk_size (int): Maximum characters per chunk
    - overlap (int): Number of characters to overlap between chunks
    
    Returns:
    List of text chunks
    """
    chunks = []
    for i in range(0, len(text), max_chunk_size - overlap):
        chunk = text[i:i + max_chunk_size]
        chunks.append(chunk)
    return chunks

def summarize_chunk(chunk:str, prompt:str) -> str:
    """
    Summarize an individual text chunk using the llm
    """
    try:
        completion = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": chunk}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return completion.choices[0].message.content
    
    except Exception as e:
        print(f"Error summarizing chunk: {e}")
        return None

def summarize_long_text(text:str, prompt="Summarize this text") -> str:
    """
    Process text with a given a prompt
    `summarize this text` is the default prompt in case is not provided
    
    Args:
    - text (str): Long input text
    - prompt (str): The user prompt
    
    Returns:
    Comprehensive summary of the entire text
    """
    # Chunk the text
    chunks = chunk_text(text)
    
    # Summarize each chunk
    chunk_summaries = []
    for chunk in chunks:
        summary = summarize_chunk(chunk, prompt)
        if summary:
            chunk_summaries.append(summary)
    
    # If multiple chunk summaries, create a final summary
    if len(chunk_summaries) > 1:
        final_combined_text = " ".join(chunk_summaries)
        final_summary = summarize_chunk(final_combined_text, prompt)
        return final_summary or " ".join(chunk_summaries)
    elif chunk_summaries:
        return chunk_summaries[0]
    else:
        return "Could not generate summary"
