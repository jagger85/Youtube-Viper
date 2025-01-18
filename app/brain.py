import requests
import os
import textwrap

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f'Bearer {os.getenv("HUGGING_FACE_KEY")}'}

def chunk_text(text, max_chunk_size=1000, overlap=100):
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

def summarize_chunk(chunk):
    """
    Summarize an individual text chunk
    
    Args:
    - chunk (str): Text chunk to summarize
    
    Returns:
    Summarized text or None if error
    """
    try:
        payload = {
            "inputs": chunk,
            "max_length": 1000,
            "min_length": 30,
            "length_penalty": 2.0,
            "num_beams": 4,
            "do_sample": False
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        # Handle different response formats
        if isinstance(result, list) and result and 'summary_text' in result[0]:
            return result[0]['summary_text']
        elif isinstance(result, dict) and 'summary_text' in result:
            return result['summary_text']
        else:
            print("Unexpected response format")
            return None
    
    except Exception as e:
        print(f"Error summarizing chunk: {e}")
        return None

def summarize_long_text(text):
    """
    Summarize a long text by breaking it into chunks
    
    Args:
    - text (str): Long input text
    
    Returns:
    Comprehensive summary of the entire text
    """
    # Chunk the text
    chunks = chunk_text(text)
    
    # Summarize each chunk
    chunk_summaries = []
    for chunk in chunks:
        summary = summarize_chunk(chunk)
        if summary:
            chunk_summaries.append(summary)
    
    # If multiple chunk summaries, create a final summary
    if len(chunk_summaries) > 1:
        final_combined_text = " ".join(chunk_summaries)
        final_summary = summarize_chunk(final_combined_text)
        return final_summary or " ".join(chunk_summaries)
    elif chunk_summaries:
        return chunk_summaries[0]
    else:
        return "Could not generate summary"

# # Example usage
# long_text = """Your very long text goes here..."""
# comprehensive_summary = summarize_long_text(long_text)
# print(comprehensive_summary)