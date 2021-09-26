
def tournmentWinner(compitions,results):
    print(compitions,results)
    winners = {}
    for i in range(len(compitions)):
        result  = results[i]
        if result == 0:
            winnerName = compitions[i][1]
        else :
            winnerName = compitions[i][0]
        if winnerName in winners:
            winners[winnerName] += 1
        else:
            winners[winnerName] = 1
    print(winners)
    max = float('-inf')
    name = "test"
    for key in winners:
        if winners[key] > max:
            name = key
    print(name)

compitions = [["HTML","C#"],["C#","Python"],["Python","HTML"]]
results = [0,0,1]
tournmentWinner(compitions,results)
