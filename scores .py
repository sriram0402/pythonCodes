totalScores=int(input("enter how many scores would you like to enter:"))
scores=[]*totalScores;
for i in range(totalScores):
    a=int(input("enter the score:"))
    scores.append(a)

print("Low score:",min(scores))
print("High score:",max(scores))
print("Average score:",round(sum(scores)/len(scores),2))
    
