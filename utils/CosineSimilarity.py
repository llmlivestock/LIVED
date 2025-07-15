from sentence_transformers import SentenceTransformer, util

# Initialize the model
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')  # Support Chinese

# Define a function to calculate cosine similarity
def calculate_cosine_similarity(response, correct_answer):
    emb_ref = model.encode(response)
    emb_cand = model.encode(correct_answer)
    similarity = util.cos_sim(emb_ref, emb_cand).item()
    return similarity
