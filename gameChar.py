class Character:
    def __init__(self, char_name, char_description):
        self.char_name = char_name
        self.char_description = char_description
        self.conversation = None 
        self.life = 100
        
    def change_name(self, new_name):
        self.char_name = new_name
        print(f"Name changed to {new_name}")

    def show(self: any)-> None:
        return self.char_name + self.char_description
    
    def describe (self):
        print(f"{self.char_name} is here!")
        print(self.char_description)

    def talk(self, message)-> None:
        print(f"{self.char_name} says: {message}") 
        #add method talk to the main game when
        #when the user enters each room

    def fighting(self, message)-> None:
        return "Fight!"
        #add fight the charatcer method to the user after chatting to the chef 

    def send2Sleep(self)-> None: 
        return self.send2Sleep
        eliksir_count -= 1 #shoudl it be here or not? 

        print(f"{self.char_name} says: You look so thirty, would you like to have a sip of water?")
        #add eliskir count 
        #add if statement when interacxting with the Chef or other characters
        #add to send to sleep as a option if you have some eliksir 

class User(Character):
    has_key = False
    def __init__(self, char_name, char_description) -> None:
        self.has_key = False
        super().__init__(char_name,char_description )

    def take_key(self):
        self.has_key = True


class Chef(Character):
    def __init__(self, char_name, char_description, life) -> None:
        super().__init__(char_name,char_description )


    def set_life(self, item_life):
        self.weakness = item_life #how to set up weakness to the sleeping eliksir
    
    def take_potion(self):
        self.life = 0

    def talk(self, chat):
        print(chat)
        #user needs to put his name 
        #will need help finding an incredient 
        #show the way to play room 

class Child(Character):
    def __init__(self, char_name, char_description, life) -> None:
        super().__init__(char_name,char_description) 
        self.life = 100 #define power to each char 

    def get_char_life(self): 
        return self.life
        
    #child will wonna play a game and tell a secret
    #secret about the ghost Mikolaj Kopernik, Polish atronome (earth goes around the sun) 
    #"He says that he stopped the sun and moved the Earth. 
    # Keeps mentioning about the power of the Golden Age of Polish culture 
    #as if he is not aware that after the first patrition taken on the  Polish lithuanian Commonwealth, there isn't much left of the golden age.
    # What a weirdo!"

class Librarian(Character):
    def __init__(slef, char_name, char_description) -> None:
        super().__init__(char_name,char_description ) 
        
    #the lib will give googel access to help the scholar find IBAN number 
    # IBAN number was inveneted in 1966 but the schoalr is from around 1800

class Scholar(Character):
    def __init__(self, char_name, char_description) -> None: 
        super().__init__(char_name,char_description)
        
        #will need help with IBAN number 
        #will be annoyed by the musician to play the piano instead of the harpsichord 

class Musician(Character):
    def __init__(self, char_name, char_description) -> None: 
        super().__init__(char_name,char_description) #will need help with twinkle twinkle tune
        #Ludwig will be hearing teh ring noise cos of hie los ear condition 
        #will complain on Mozart beign the one from the famous twinkle tune 
        #he will know it's not original, he only wrote the variations 
        #will need help figuring out the tune, user needs to tipe it in solfa 
