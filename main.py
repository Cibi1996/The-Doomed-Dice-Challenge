from collections import Counter
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

Total_combinations=[]
sum_combinations=[]

def dice_sum():

    for i in Die_A:
        row = []
        for j in Die_B:
            Total_combinations.append((i, j))
            sum = i + j
            row.append(sum)
        sum_combinations.append(row)


# 1. How many total combinations are possible? Show the math along with the code!
dice_sum()
for k in Total_combinations:
    print(k)
print(f"1.The total possible combinations are : {len(Total_combinations)}")

# 2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!
# Hint: A 6 x 6 Matrix.
print("2.Matrix Distribution(6*6)-->Die_A and Die_B")
for row in sum_combinations:
    print(row)

single_sum_combination=[item for sublist in sum_combinations for item in sublist]

count = Counter(single_sum_combination)

"""3.Calculate the Probability of all Possible Sums occurring among the number of
combinations from (2).

Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain
Sum = 2. Die A = Die B = 1."""


print("Probablities Of All Possible Sums:")
for a in set(single_sum_combination):
    print(f"Probablity of {a} is {count[a]/36:.4f}")

"""Part-B (25-30 Minutes):
Now comes the real challenge. You were happily spending a lazy afternoon playing
your board game with your dice when suddenly the mischievous Norse God Loki ( You
love Thor too much & Loki didn’t like that much ) appeared.
Loki dooms your dice for his fun removing all the “Spots” off the dice.

No problem! You have the tools to re-attach the “Spots” back on the Dice.
However, Loki has doomed your dice with the following conditions:
● Die A cannot have more than 4 Spots on a face.
● Die A may have multiple faces with the same number of spots.
● Die B can have as many spots on a face as necessary i.e. even more than 6.
But in order to play your game, the probability of obtaining the Sums must remain the
same!
So if you could only roll P(Sum = 2) = 1/X, the new dice must have the spots reattached
such that those probabilities are not changed.
Input:
● Die_A = [1, 2, 3, 4, 5, 6] & Die B = Die_A = [1, 2, 3, 4, 5, 6]
Output:
● A Transform Function undoom_dice that takes (Die_A, Die_B) as input &
outputs New_Die_A = [?, ?, ?, ?, ?, ?],New_Die_B = [?, ?,
?, ?, ?, ?] where,
● No New_Die A[x] > 4
"""

def undoom_dice(Die_A, Die_B):
    # Create a new list for Die A
    New_Die_A = []
    for i in Die_A:
        if i > 4:
            New_Die_A.append(i - 3)  # Subtract 3 if i > 4
        else:
            New_Die_A.append(i)  # Otherwise, keep i as it is

    # Create a new list for Die B
    New_Die_B = []
    for j in Die_B:
        if j % 2 == 0:
            New_Die_B.append(j + 2)  # Add 2 if j is even
        else:
            New_Die_B.append(j)  # Otherwise, keep j as it is
    return sorted(New_Die_A), sorted(New_Die_B)

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

print("Transformed Die A:", New_Die_A)
print("Transformed Die B:", New_Die_B)




