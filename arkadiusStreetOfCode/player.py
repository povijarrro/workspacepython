class Player:
    def __init__(self, name):
        self.name=name
        self.abilities = {
"Strength": {
"points": 1,
"description": "Sila je potrebna k útoku, do ktorého okrem sily vstupuje aj obratnosť a skill."
},
"Defence": {
"points": 1,
"description": "Celkova obrana sa ráta z bodov obrany + obratnosti."
},
"Dexterity": {
"points": 1,
"description": "Obratnosť je dôležitá aj pre obranu aj pre útok."
},
"Skill": {
"points": 1,
"description": "Skill je dôležitý pri normálnom útoku ako aj kritickom útoku"
},
"Life": {
"points": 50,
"description": "Život je dôležitý pri bitke. Život sa dá doplniť po každom súboji."
},
"Luck": {
"points": 1,
"description": "Šťastie je dôležité pre kritický útok"
}
}

    def print_abilities(self):
        strength=self.abilities["Strength"]["points"]
        defence=self.abilities["Defence"]["points"]
        dexterity=self.abilities["Dexterity"]["points"]
        skill=self.abilities["Skill"]["points"]
        life=self.abilities["Life"]["points"]
        luck=self.abilities["Luck"]["points"]
        print(f"{self.name}, Tvoje schopnosti sú na tom takto:")
        print(f"Utocna sila - {strength} Obrana - {defence} Obratnost - {dexterity} Skill - {skill} Zivot - {life} Stastie - {luck}")