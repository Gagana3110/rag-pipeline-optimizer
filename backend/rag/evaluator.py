
def evaluate_pipeline(question, answer, context):

    # Simple heuristic evaluation

    relevance_score = 0
    faithfulness_score = 0

    # Relevance check
    if any(word.lower() in answer.lower() for word in question.split()):
        relevance_score += 0.8
    else:
        relevance_score += 0.4

    # Faithfulness check
    if any(sentence[:20] in context for sentence in answer.split(".")):
        faithfulness_score += 0.9
    else:
        faithfulness_score += 0.5

    return {
        "faithfulness": round(faithfulness_score, 2),
        "answer_relevancy": round(relevance_score, 2)
    }