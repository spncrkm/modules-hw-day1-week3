class Mood:
    
    def __init__(self):
        pass

    
    def mood_input(self):
        self.choice = input("How are you feeling? \n1. Happy \n2. Sad \n3. Excited \n4. Tired ")
        if self.choice == '1':
            print("We can all be happy together! ")
        elif self.choice == '2':
            print("Aww, I hope you feel better. ")
        elif self.choice == '3':
            print("Let's party!!!! ")
        elif self.choice == '4':
            print("Go get some sleep! ")
        else:
            print("Please enter either 1, 2, 3 or 4. ")
            
        