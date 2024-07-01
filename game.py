
#add inheritance and pol
from gameChar import Chef, User 
from item import Item
from gameRoom import Room


user_input = ""
enter_count = 0

key_num = 0 # user needs to colelct keys to get from room to room 

eliksir_count = 0 #user can put other character to sleep and survive or steel the keys to the playroom(work on Chef)
gift_count = 0 #user can gift a child with a toy or play a game (works on Chef and on Child) child give a clu for Kopernik
show_descriptio_count = 0 #getter-user can see what works on the character to chose the right thing
google_help = 0

eliksir= Item("Eliksir", "sleeping potion")
chef = Chef



print("\nRing", "ding", "ding", "!!!", sep= "***")
print("\nLook!\nYou got a message, snooze the loud ringtone and check it out!")


while user_input != "off" and enter_count < 3:
    user_input = input("\nTo turn it off type: off ")
    user_input = user_input.lower()
    enter_count += 1 

    if enter_count == 3:#maybe user should say it {self.name}?
        print("\nWow, that was a horrible dream. Luckly I did not snooze my alarm again.") 

    
    if user_input != "off":
        print("\nRing", "ding", "ding", "!!!", sep= "***")
        enter_count += 1 
    else: 
        print("\nThanks for turnign it off! Here is the message: ") 
        #maybe some buttom to reveal the message or open the phone? 

        phoneText = """
            Dear Player, you are about to start your adventures journey. 
            We are so excited to host you here in the Maze Hill Mantion, 
            most importanlty we hope you are ready.
            Although the adventure is absolutly wonderful 
            beaware of the danger that it brings within. 
            Every move, each step must be well considered. 

            To help you browsing through the Mantion we have gifted you with items such as: 
            2 x eliksirs, 1 x gift, 1 x reveal character card
            
            You can use those items to pass through each character.
            Use it wisely, it does not always work on everyone. 
            Each character has its own personality and a weak point.

            Good luck!
            """
        print(phoneText)

        key_num += 1
        eliksir_count += 2 #one for Chef and one for Child but it won't work  
        gift_count += 1 #one for child 
        show_descriptio_count += 1 #if they don't know how to fight them 

        print("\nYou have received your first key, use it to open the doors.")
        print("\nGo alonside the corridor, it will take you to the kitchen.")
        break

#define properties, attribute and matters. 
#creste move matter, first define 

chef = Chef()
chef.change_name("Kirko Buchek")

user = User()
user.change_name(input("Enter your username: "))

# chef talks to user
chef.talk(f"Hello, my name is {chef.name}. Who are you?")
user.talk (f"Hi {chef.char_name} my name is {user.char_name}")

#teh cherf will ask fro riddle, the riddle is to help him to find an ingredient 
#if the user cannot find it it can give him a eliksir 

# we will choose from several options and check if chef's life is zero
# only if chef's life is zero you can get the key
# if chef's life is zero, you take the key: user.take_key()


# rooms = {
#     "kitchen":{
#         "You are in the kitchen, where you can meet the Chef."
#     }
#     "play room": {
#         "You are in the playroom "
#     }
# }

#here he meets chef, while they are interracting he user writes his name 

#user moves to a kitchen  HOW TO SHOW THAT? 

#the rest of the game code 

#End Game:
#print("Ring", "ding", "ding", "!!!", sep= "***") TAKE OFF THE COMMENT #

#the ringing tone that annoys Beethoven cos of his hearing problems 
#was atually user's alarm, beethoven played a klaster and wake up the user
#the user wakes up 