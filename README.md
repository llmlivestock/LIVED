# LIVED: A Comprehensive Benchmark for Evaluating Large Language Models in the Livestock Domain

This repository contains the LIVED benchmark dataset and evaluation metrics for assessing the performance of large language models in the livestock domain.

## Dataset

We have released 1000 Q&As from the LIVED dataset, which can be found in the `minidata` folder. The distribution of question types is as follows:
- Multiple Choice Questions: 600 questions
- Judgment Questions: 165 questions
- Completion Questions: 155 questions
- Open-ended Questions: 80 questions

If you are interested in obtaining the full version of the LIVED dataset, please contact us via email at yb_20020727@webmail.hzau.edu.cn.

## Evaluation Metrics

The `utils` folder contains the evaluation metrics used to assess the performance of language models on the LIVED dataset:
- `Accuracy.py`: This script calculates the accuracy for multiple-choice and judgment questions.
- `Cosine_Similarity.py`: This script computes the cosine similarity for completion and open-ended questions.
