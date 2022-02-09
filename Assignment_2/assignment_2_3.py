def crowd_test(some_list):
    if len(some_list) > 3:
        print("The room is crowded")


people_list = ["Bob", "Bill", "Sam", "Joe"]

print("~~~~ First Call To crowd_test Function ~~~~")
crowd_test(people_list)

print("Removing 2 people from list...")
people_list.remove("Bob")
people_list.remove("Bill")

print("~~~~ Second Call To crowd_test Function ~~~~")
crowd_test(people_list)
