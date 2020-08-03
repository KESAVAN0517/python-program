import random 
  
  
a = "s"
   
while a == "s": 
    dice = random.randint(1,6) 
      
    if dice == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  1  ]") 
        print("[     ]") 
        print("[-----]") 
    if dice == 2: 
        print("[-----]") 
        print("[2    ]") 
        print("[     ]") 
        print("[    2]") 
        print("[-----]") 
    if dice == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[3 3 3]") 
        print("[     ]") 
        print("[-----]") 
    if dice == 4: 
        print("[-----]") 
        print("[4   4]") 
        print("[     ]") 
        print("[4   4]") 
        print("[-----]") 
    if dice == 5: 
        print("[-----]") 
        print("[5   5]") 
        print("[  5  ]") 
        print("[5   5]") 
        print("[-----]") 
    if dice == 6: 
        print("[-----]") 
        print("[6   6]") 
        print("[6   6]") 
        print("[6   6]") 
        print("[-----]") 
          
    a=input("press s to roll again and n to exit:") 
    print("\n") 