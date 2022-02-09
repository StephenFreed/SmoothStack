# six is a mob

print("~~~~ six is a mob ~~~~")


def six_is_a_mob(some_list):
    if len(some_list) > 5:
        print(f"There is a mob in the room. {len(some_list)} people.")
    elif len(some_list) > 3 and len(some_list) < 6:
        print(f"The room is crowded. {len(some_list)} people.")
    elif len(some_list) > 0 and len(some_list) < 3:
        print(f"The room is not crowded. {len(some_list)} people.")
    else:
        print("The room is empty.")


six_is_a_mob_list = ["Bob", "Bill", "Sam", "Joe", "Jack", "John"]


print("~~~~ First Call To six_is_a_mob Function ~~~~")
six_is_a_mob(six_is_a_mob_list)

print("Removing 2 people...")
six_is_a_mob_list.remove("Bob")
six_is_a_mob_list.remove("Bill")

print("~~~~ Second Call To six_is_a_mob Function ~~~~")
six_is_a_mob(six_is_a_mob_list)

print("Removing 2 people...")
six_is_a_mob_list.remove("Sam")
six_is_a_mob_list.remove("Joe")

print("~~~~ Third Call To six_is_a_mob Function ~~~~")
six_is_a_mob(six_is_a_mob_list)

print("Removing 2 people...")
six_is_a_mob_list.remove("Jack")
six_is_a_mob_list.remove("John")

print("~~~~ Forth Call To six_is_a_mob Function ~~~~")
six_is_a_mob(six_is_a_mob_list)
