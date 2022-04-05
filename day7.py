st = open ("st.txt", "w")
st.write ("Как тебя зовут?")
st.close()



import csv

with open("st.csv", "w") as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["звездные войны",
                "терминатор",
                "интелект"])
    w.writerow(["klkl",
                "jkjkj",
                "jkjkjn"])
    w.writerow(["jkjggg",
                "uuuu",
                "pppp"])
