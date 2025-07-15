import re
def extract_and_evaluate_answer(model_response, correct_answer):
    """
    Extract the answer from the model's response, compare it with the standard answer, and return whether it is correct.

    :param model_response: model's response（str）
    :param correct_answer: standard answer（str）
    :return: true/false（Boolean），The answer extracted from the model (string)
    """
    #match = re.search(r'[A-D]', model_response) #multiple-choice questions
    # Use regular expressions to match "正确" or "错误".
    match = re.search(r'(正确|错误)', model_response)
    if match:
        predicted_answer = match.group(1)  # Return the first matched result
        is_correct = predicted_answer == correct_answer
        return is_correct, predicted_answer
    return False, None  # If no matching characters are found, return False and None.
