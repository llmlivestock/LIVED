import re
def extract_and_evaluate_answer(model_response, correct_answer):
    """
    从模型的回答中提取答案，并与标准答案比较，返回是否正确。

    :param model_response: 模型的回答内容（字符串）
    :param correct_answer: 标准答案（字符串）
    :return: 是否正确（布尔值），模型提取的答案（字符串）
    """
    #match = re.search(r'[A-D]', model_response) #选择题
    # 使用正则表达式匹配“正确”或“错误”
    match = re.search(r'(正确|错误)', model_response)
    if match:
        predicted_answer = match.group(1)  # 返回匹配到的第一个结果
        is_correct = predicted_answer == correct_answer
        return is_correct, predicted_answer
    return False, None  # 如果没有找到匹配的字符，返回 False 和 None
#
# # 示例使用
# if __name__ == "__main__":
#     # 模型的回答示例
#     model_response_1 = "经过分析，这个说法是正确的。"
#     model_response_2 = "这个说法是错误的，因为……"
#     model_response_3 = "无法确定这个说法是否正确。"
#
#     # 标准答案
#     correct_answer_1 = "正确"
#     correct_answer_2 = "错误"
#     correct_answer_3 = "正确"
#
#     # 调用函数并打印结果
#     print("示例 1:")
#     is_correct_1, predicted_answer_1 = extract_and_evaluate_answer(model_response_1, correct_answer_1)
#     print(f"模型回答: {model_response_1}")
#     print(f"标准答案: {correct_answer_1}")
#     print(f"提取答案: {predicted_answer_1}")
#     print(f"是否正确: {is_correct_1}\n")
#
#     print("示例 2:")
#     is_correct_2, predicted_answer_2 = extract_and_evaluate_answer(model_response_2, correct_answer_2)
#     print(f"模型回答: {model_response_2}")
#     print(f"标准答案: {correct_answer_2}")
#     print(f"提取答案: {predicted_answer_2}")
#     print(f"是否正确: {is_correct_2}\n")
#
#     print("示例 3:")
#     is_correct_3, predicted_answer_3 = extract_and_evaluate_answer(model_response_3, correct_answer_3)
#     print(f"模型回答: {model_response_3}")
#     print(f"标准答案: {correct_answer_3}")
#     print(f"提取答案: {predicted_answer_3}")
#     print(f"是否正确: {is_correct_3}\n")
