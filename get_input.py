from data_manager import DataManager

class GetInput:
    def __init__(self):
        self.data_manager = DataManager()
        print("Welcome to Mayank's Flight Deals Club.")
        print("We find the best flight deals and email you.")
        f_name = input("What is your first name?\n")
        l_name = input("What is your last name?\n")
        email = input("What is your email?\n")
        retyped_email = ""

        while email != retyped_email:
            retyped_email = input("Type your email again.\n")
            if email == retyped_email:
                self.data_manager.update_user_data(f_name=f_name.title(), l_name=l_name.title(), email=email)
                print("You are in the club!")
            else:
                print("Your emails mismatch, please try again.\n")

