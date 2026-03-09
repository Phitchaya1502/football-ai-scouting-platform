def analyze_player(goals, assists, passes, rating):

    score = (

        goals * 0.4 +
        assists * 0.3 +
        passes * 0.1 +
        rating * 0.2

    )

    if score > 8:

        recommendation = "Top Player"

    elif score > 6:

        recommendation = "Good Player"

    else:

        recommendation = "Average Player"

    return score, recommendation