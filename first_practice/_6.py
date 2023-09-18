def split_list(scores):
    if not scores:
        return [], []

    average_score = sum(scores) / len(scores)
    lower_half = []
    upper_half = []

    for score in scores:
        print(score)
        if score <= average_score:
            lower_half.append(score)
        else:
            upper_half.append(score)

    print(scores)
    print(lower_half, upper_half)
    print(average_score)

    return lower_half, upper_half

split_list([1, 12, 3, 24, 5])
