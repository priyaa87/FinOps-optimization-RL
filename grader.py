def grade_performance(initial_cost, final_cost):
    improvement = (initial_cost - final_cost) / initial_cost

    if improvement > 0.4:
        return 1.0  # excellent
    elif improvement > 0.2:
        return 0.7
    elif improvement > 0.1:
        return 0.4
    else:
        return 0.1