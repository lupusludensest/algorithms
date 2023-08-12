def squares_needed(grains):
    if grains == 0:
        return 0
    return 1 + squares_needed(grains // 2)



print(squares_needed(54))