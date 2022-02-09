# ~~~~~~~~~ three is a crowd part 2 ~~~~~~~~~

print("~~~~ three is a crowd part 2 ~~~~")


def crowd_test_2(some_list):
    if len(some_list) > 3:
        print("The room is crowded.")
    else:
        print("The room is not crowded.")


people_list_2 = ["Bob", "Bill", "Sam", "Joe"]

print("~~~~ First Call To crowd_test_2 Function ~~~~")
crowd_test_2(people_list_2)

print("Removing 2 people...")
people_list_2.remove("Bob")
people_list_2.remove("Bill")

print("~~~~ Second Call To crowd_test_2 Function ~~~~")
crowd_test_2(people_list_2)
