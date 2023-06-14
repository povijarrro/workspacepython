from player import Player 

class MainGame:
    def __init__(self):
        self.player=None
        print("Práve si zapol hru, v ktorej budeš bojovať proti príšerám a pri tom si zlepšovať svojho hrdinu. Si na to pripravený?\n0 - Nie, bojim sa.\n1 - Ano, podme na to.")
        
        while True:
            print("Aka je tvoja volba?")
            user_choice = input()
            if user_choice not in ["0", "1"]:
                continue
            elif user_choice == "0":
                break
            else:
                print("Vyborne, mas odvahu. To sa mi paci.")
                self.get_name(); 
                self.player.print_abilities()
                break

    def get_name(self):
        while True:
            print("Ako sa bude volat tvoj hrdina?")
            player_name= input()
            print(f"Si si isty, ze sa tvoj hrdina bude volat {player_name} ?\n0 - Nie, chcem zmenit meno.\n1 - Ano.")
            user_choice = input()
            if user_choice not in ["0", "1"]:
                continue
            elif user_choice == "0":
                continue
            else:
                print(f"Ahoj {player_name}")
                if not self.player:
                    self.player=Player(player_name)
                else: 
                    self.player.name=player_name
                break    
    
    