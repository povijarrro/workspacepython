#!python

from itertools import combinations


def best_price(enemy:dict[str,int],shop:dict[str,dict[str,dict[str,int]]])->int:
    player = {"hp":100,"damage":0,"armor":0}
    weaps = list(shop["weapons"].keys())
    arms = list(shop["armor"].keys())
    arms.append("")
    rings = list(shop["rings"].keys())
    

    for w in weaps:
        for a in arms:
            for k in (0,1,2):
                for r in combinations(rings,k):
                    pass
                




if __name__ =="__main__":
    weapons={"Dagger":{"Cost":8,"Damage":4},
             "Shortsword":{"Cost":10,"Damage":5},
             "Warhammer":{"Cost":25,"Damage":6},
             "Longsword":{"Cost":40,"Damage":7},
             "Greataxe":{"Cost":74,"Damage":8}}
         
    armor={"Leather":{"Cost":13,"Armor":1},
           "Chainmail":{"Cost":31,"Armor":2},
           "Splintmail":{"Cost":53,"Armor":3},
           "Bandedmail":{"Cost":75,"Armor":4},
           "Platemail":{"Cost":102,"Armor":5}}
     
    rings={"Damage+1":{"Cost":25,"Damage":1,"Armor":0},
           "Damage+2":{"Cost":50,"Damage":2,"Armor":0},
           "Damage+3":{"Cost":100,"Damage":3,"Armor":0},
           "Defense+1":{"Cost":20,"Damage":0,"Armor":1},
           "Defense+2":{"Cost":40,"Damage":0,"Armor":2},
           "Defense+3":{"Cost":74,"Damage":0,"Armor":3}}
    
    shop = {"weapons":weapons,
            "armor":armor,
            "rings":rings}

    enemy = {"hp":103,
             "damage":9,
             "armor":2}

    player = {"hp":100,
              "damage":0,
              "armor":0}
print(combinations_with_replacement(range(6),0)+combinations_with_replacement(range(6),2))