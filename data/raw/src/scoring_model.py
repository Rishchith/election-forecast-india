def calculate_score(row, weights):
    score = 0
    
    score += weights["historical"] * row["past_vote_share"]
    score += weights["swing"] * row["swing_estimate"]
    score += weights["alliance"] * row["alliance_strength"]
    score += weights["demographics"] * row["demographic_alignment"]
    score += weights["turnout"] * row["turnout_factor"]
    
    return score


def classify(score):
    if score > 0.65:
        return "Safe"
    elif score > 0.5:
        return "Lean"
    else:
        return "Toss-up"
