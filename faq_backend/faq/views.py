from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import os
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Load the Sentence-BERT model
tokenizer = BertTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = BertModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Load FAQ data from faqs.json file
FAQ_PATH = os.path.join(os.path.dirname(__file__), 'faqs.json')
with open(FAQ_PATH, 'r') as f:
    faq_data = json.load(f)

faq_list = []
faq_embeddings = []

# Precompute embeddings for the FAQ questions
for category, entries in faq_data.items():
    for entry in entries:
        faq_list.append({
            "category": category,
            "question": entry["question"],
            "answer": entry["answer"]
        })
        
        # Compute embeddings for each question and reduce dimensions
        inputs = tokenizer(entry["question"], return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            embeddings = model(**inputs).last_hidden_state.mean(dim=1)  # Reducing 3D to 2D by averaging
        faq_embeddings.append(embeddings)

# Stack all FAQ embeddings into a single tensor and reduce dimensions
faq_embeddings = torch.cat(faq_embeddings, dim=0)  # Concatenate tensors along the first dimension

def compute_embedding(query):
    # Compute embedding for the query and reduce dimensions
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        embedding = model(**inputs).last_hidden_state.mean(dim=1)  # Average over sequence length
    return embedding

@api_view(['POST'])
def search_faq(request):
    query = request.data.get('query', '')
    
    if not query:
        return Response({"error": "Query parameter is required"}, status=400)
    
    query_embedding = compute_embedding(query)
    
    # Calculate cosine similarity between query and all FAQ embeddings
    similarities = cosine_similarity(query_embedding.numpy(), faq_embeddings.numpy())
    
    # Find the most similar question
    best_match_index = similarities.argmax()
    
    # Return the best matching FAQ
    best_faq = faq_list[best_match_index]
    
    return Response({
        "question": best_faq["question"],
        "answer": best_faq["answer"],
        "category": best_faq["category"]
    })
