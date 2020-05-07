def computegrade(score):
    if score > 1.0:
        return 'Bad Score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'
    


try:
    scr = float(input('Enter score: '))
except:
    print('Bad score')
    quit()

print(computegrade(scr))