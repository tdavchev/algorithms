global count
def countEmployeesUnder(people, name):
    # count = 0
    global count
    for person, manager in people:
        if manager == name:
            count = count + 1
            countEmployeesUnder(people, person)

    # return count

def print_et():
    count += 0
    print(count)

def callFunc():
    global count
    count = 0
    people = [("Veronica", ""), ("Nathan", "Veronica"), ("Dilbert", "Nathan"),
    ("Sally", "Veronica"), ("Bob", "Sally"), ("Joseph", "Sally"),
    ("Susan", "Bob"), ("Sam", "Joseph"), ("Betty", "Sam")]
    countEmployeesUnder(people, "Joseph")
    # print_et()
    print(count)

callFunc()
