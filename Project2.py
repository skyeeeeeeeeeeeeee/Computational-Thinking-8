halloween_points = 0
christmasorhunakkah_points = 0
thanksgiving_points = 0
fourthofjuly_points = 0

answer1 = input("Do you prefer A candy, B gifts, C family time, or D fireworks?    ")
if answer1 == "A":
    halloween_points += 1
elif answer1 == "B":
    christmasorhunakkah_points += 1
elif answer1 == "C":
    thanksgiving_points += 1
elif answer1 == "D":
    fourthofjuly_points += 1

answer2 = input("Do you enjoy A building gingerbread houses , B dressing up, C eating yummy food, or D watching loud and cool things?    ")
if answer2 == "A":
    christmasorhunakkah_points += 1
elif answer2 == "B":
    halloween_points += 1
elif answer2 == "C":
    thanksgiving_points += 1
elif answer2 == "D":
    fourthofjuly_points += 1

answer3= input("Would you rather A turkey, B hot dogs, C candy canes, D kitkat bar?       ")        
if answer3 == "A":
    thanksgiving_points += 2
elif answer3 == "B":
    fourthofjuly_points += 2
elif answer3 == "C":
    christmasorhunakkah_points +=2
elif answer3 == "D":
    halloween_points += 2

answer4= input("What feeling do you enjoy most? A Scared, B shocked, C peacful, or D, Jolly and Happy?      ")
if answer4 == "A" or answer4=="a":
    halloween_points += 1
elif answer4 == "B":
    fourthofjuly_points += 1
elif answer4 == "C":
    thanksgiving_points += 1
elif answer4 == "D": 
    christmasorhunakkah_points += 1

answer5= input("Would you rather be A, outside or B, inside?       ")
if answer5 == "A": 
    halloween_points += 1
elif answer5 == "A":
    fourthofjuly_points += 1
elif answer5 == "B": 
    christmasorhunakkah_points += 1
elif answer5 == "B":
    thanksgiving_points += 1

answer6= input("Which color combos do you prefer more out of these 4? A, Orange&Black, B, Brown&Tan, C, Blue&Black, or D, Red&Green?       ")
if answer6 == "A":
    halloween_points += 1
elif answer6 == "B":
    thanksgiving_points += 1
elif answer6 == "C":
    fourthofjuly_points += 1
elif answer6 == "D":
    christmasorhunakkah_points += 1


if christmasorhunakkah_points > thanksgiving_points and christmasorhunakkah_points > halloween_points and christmasorhunakkah_points > fourthofjuly_points:
    print("You are a Christmas/Hunakkah person! Me too!")
elif thanksgiving_points > christmasorhunakkah_points and thanksgiving_points > halloween_points and thanksgiving_points > fourthofjuly_points:
    print("You are a Thanksgiving person! You must be very thankful")
elif halloween_points > christmasorhunakkah_points and halloween_points > thanksgiving_points and halloween_points > fourthofjuly_points:
    print("You are a Halloween person! Ouuu spooky!")
elif fourthofjuly_points > halloween_points and fourthofjuly_points > christmasorhunakkah_points and fourthofjuly_points > thanksgiving_points:
    print("You are a Fourth of July person! Nice!")
else: 
    print("Could not quite figure out what Holiday you were")