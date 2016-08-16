print("What is your name, young grasshopper?")
name=input("Name?")
print("A castle looms in the distance. As the fog clears something draws you towards the castle.")
print("After walking for a brief distance, two choices stand before you. An ominous wooden door creaks in the wind, swinging open as though it was possessed by a mystical force. You look to the right and there is a cellar door concealed behind a large rock. Further to the right, you spot a garden. Which way do you go?")
choice1=input("Door or Cellar or Garden?")
while choice1!=("Door" or "Cellar" or "Garden"):
    print("Please enter Door, Cellar or Garden.")
    choice1=input("Door or Cellar or Garden?")
    if choice1=="Door":
        print("A shiny piece of candy lies on the ground.")
        print("Do you eat the candy?")
        choice2=input("Yes or No?")
        if choice2=="Yes":
                print("The candy was infused with powerful magic and you turn into an evil witch! But you rule the world so it's okay.")
        if choice2=="No":
                print("A skeleton shoots you while you're distracted and you pass out.")

    if choice1=="Cellar":
        print("You turn a corner and two doors slowly emerge. One is blood red, while the other is poisonous blue.")
        print("Which door do you go through?")
        choice3=input("Red or Blue?")
        if choice3=="Red":
            print("You find an iron chest. As you open the chest, your vision is flooded by a sea of gold. You leap in joy as you drag the chest of gold back home. You become a millionare!!!!")
        if choice3=="Blue":
            print("A vampire appears before you. As you stare into its entrancing gaze, it surges forward and buries its fangs into your flesh. You slowly feel yourself losing consciousness as blood seeps out of your body.")
            print("As you slowly regain consciousness, you feel as though you are possessed by an ancient force. A voice rings in your ears: 'You're a vampire, "+name+".'")
        
    if choice1=="Garden":
        print("A luscious garden materializes in front of your very eyes. Behold the wild plants and cherry trees! You explore the garden and suddenly hear a loud meowing sound. Two cats stare up at you, their eyes round as moons. A sleek calico cat purrs as it rubs against your calf.")
        print("On your other side, a large grey tabby prowls, its eyes glowing demonically.")
        choice4=input("Pet the Calico, or Tabby?")
        if choice4=="Calico":
            print("The cat hisses in a threatening manner and digs its claws into your eyes. You scream in fury and pain, but you are powerless against this satanic creature, and eventually succumb to its wrath.")
        if choice4=="Tabby":
            print("As you approach the tabby, it morphs into a handsome prince, standing before you. His emerald gaze envelops your soul. You find yourself falling into his arms as you exclaim, 'my prince!'")    
#print("THE END")