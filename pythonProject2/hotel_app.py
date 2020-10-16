# Let's imagine that you're running a hotel,
# and you want to keep track of guests by floor
# and room number:

# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.

# current state of hotel for each floor
hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
    '102': [],
    '103': [],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
    '238': ['Jack Russel'],
    '239': [],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus'],
    '334': [],
    '335': ['Stas Chorny'],
  }
}

# flag to know when guest has checked in or out
bad_input = True

# until guest successfully checks in or out
while bad_input:
    # ask guest if they are checking in
    check_in = input("Checking in? ").lower()
    if check_in == "yes": # if guest responds "yes"
        # set floor number to empty string
        # so it can be checked against existing hotel floors
        floor_number = ''
        # until guest provides existing hotel floor
        while floor_number not in hotel:
            # ask guest what floor they are staying on
            floor_number = input("Floor number? ")
        # set room to empty string to check against
        # existing rooms in hotel
        room_number = ''
        # until guest provides existing hotel room
        while room_number not in hotel[floor_number]:
            # ask guest what hotel room they are staying in
            room_number = input("Room number? ")
        # set number of occupants = 0 so that we can check
        # if guest has responded with valid number of occupants
        num_occupants = 0
        # until guest gives valid number of occupants (int > 0)
        while num_occupants <= 0:
            # prepare for non-integer input
            try:
                # prompt guest for number of occupants in room
                num_occupants = int(input("Number of occupants? "))
            except:
                # if guest does not provide integer input
                # do nothing, ask again
                pass
        # create empty list for storing occupants' names
        occupant_names = []
        # until number of occupant names given equals
        # number of occupants staying in room
        while len(occupant_names) < num_occupants:
            # ask guest for each occupant name
            occupant_name = input("Who is occupant #%d? " % (len(occupant_names) + 1))
            # if that occupant has not been added yet
            if occupant_name not in occupant_names:
                # add that occupant's name
                occupant_names.append(occupant_name)
            else:
                # let the guest know that occupant is
                # already added
                print("Guest already added.")
        # only if that room is empty
        if hotel[floor_number][room_number] == []:
            # add the occupants to the room
            hotel[floor_number][room_number] = occupant_names
            # let the guest know the check-in is complete
            print("Enjoy your stay.")
            # change flag to indicate successful check-in
            # and break loop
            bad_input = False
    else: # if guest did not respond yes to checking in
        # ask guest if they are checking out
        check_out = input("Checking out? ").lower()
        if check_out == "yes": # if guest responds "yes"
            # set floor number to empty string to check
            # if guest input for floor is valid
            floor_number = ''
            # until guest provides existing floor number
            while floor_number not in hotel:
                # ask guest what floor number they stayed on
                floor_number = input("Floor number? ")
            # set room number to empty string to check
            # if guest input for room is valid
            room_number = ''
            # until guest provides valid room number
            while room_number not in hotel[floor_number]:
                # ask guest what room they stayed in
                room_number = input("Room number? ")
            # if that room is not empty
            if hotel[floor_number][room_number] != []:
                # remove occupants from room
                hotel[floor_number][room_number] = []
                # inform guest check-out is complete
                print("Thanks for staying with us. Goodbye.")
                # change flag to indicate successful
                # check-out and break loop
                bad_input = False

print(hotel)