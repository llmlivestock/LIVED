from sentence_transformers import SentenceTransformer, util

# 初始化模型
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')  # 支持中文

# 定义计算余弦相似性的函数
def calculate_cosine_similarity(response, correct_answer):
    emb_ref = model.encode(response)
    emb_cand = model.encode(correct_answer)
    similarity = util.cos_sim(emb_ref, emb_cand).item()
    return similarity

# # 示例文本
# response = "我喜欢吃苹果"
# correct_answer = "我也喜欢吃苹果"
# # 调用函数计算余弦相似度
# similarity = calculate_cosine_similarity(response, correct_answer)
# # 打印结果
# print(f"Response: {response}")
# print(f"Correct Answer: {correct_answer}")
# print(f"Cosine Similarity: {similarity:.4f}")
