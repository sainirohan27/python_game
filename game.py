import time
print("_______________")
print("Enter your name")
print("---------------")
name=str(input(""))
print("logging into the server")
print("creating profile...\n")
print("PRESS ANY KEY TO BEGIN..!")
input()


def start():
	print("You went on a cruise in the North China Sea...\n A robust storm wrecked your yacht")
	print("make your choice",name)
	print("1) shoot the red rescue flares in sky and jump in the sea")
	print("2) put all your strenth and manage to sail in a lifeboat")
	print("3) try to repair the drowning yacht")
	x=int(input(""))
	if(x==1):
		print("poor",name,"flares are shot when a rescue ship is sighted\n")
	if(x==2):
		print("very well,",name,", You survived the crash.""\n")
		time.sleep(2)
		two()
	if(x==3):
		print("reparing the drowning yacht...",name,", u r dead.!\n")		


def two():
	print("U have sailed for 2 days on that lifeboat, now you are thirsty. Time is 13:30")
	print("make your choice",name)
	print("1) Order hot coffee from Nescafe")
	print("2) drink sea water")
	print("3) reach the nearest island (1 km away) and look for water\n")
	x=int(input(""))
	if(x==1):
		print("Nescafe- sorry for the inconvenience",name," we dont serve that area\n")
	if(x==2):
		print(name,"Say a Hiiii to YAMRAJ from my side\n")
	if(x==3):
		print("good choice",name)
		print("\n")
		time.sleep(2)
		three()
		

def three():
	print("U have reached the island, time is 15:00")
	print("make your choice",name)
	print("1) look for water")
	print("2) look for food")
	print("3) Hungry?...grab a Snickers in your dreams\n")
	x=int(input(""))
	if(x==1):
		print("good choice buddy..looks like you have got some survival skills\n")
		time.sleep(2)
		four()
	if(x==2):
		print(name,"not a good option ... I think water is more essential\n")
	if(x==3):
		print("Eat Snickers ..u r dead",name)
		print("\n")

def four():
	print("u have reached the island and luckily found freshwater stream and some fruits near the shore")
	print("while you were eating the food a mysterious little fire breathing dragon entered your pocket...she considers u as her friend ")
	print("your stomach is full, time is 16:00")
	print("make your choice",name)
	print("1) Have some time for yourself and enjoy till night")
	print("2) move on as u have consumed all the fruits available, water coming from stream is no longer clean")
	print("3) love to die here\n")
	x=int(input(""))
	if(x==1):
		print("Nescafe- sorry for the inconvenience",name," we dont serve that area\n")
	if(x==2):
		print("Hats off to u man, go on \n")
		time.sleep(2)
		five()
	if(x==3):
		print(name,"Say a Hiiii to YAMRAJ from my side\n")

def five():
	print("U found a long mysterious cave and u decided to enter it, ")
	print("u got trapped inside the cave just the moment u entered by the large falling stones.")
	print("make your choice",name)
	print("1) try making yout way out by lifting the stones ")
	print("2) shout for help")
	print("3) move ahead in the cave\n")
	x=int(input(""))
	if(x==1):
		print("You are not Hercules, and hence u die\n")
	if(x==2):
		print(name,"shout louder ...nearest human being is just few thousand KM away\n")
	if(x==3):
		print("Brave",name)
		print("\n")
		time.sleep(2)
		six()

def six():
	print("cave leads to three scary doors..exit through 1...death through the rest 2")
	print("make your choice",name)
	print("1) behind this door are 20 lions who are hungry from a week")
	print("2) behind this door are 10 posionous snakes...kills instantly")
	print("3) behind this door are 100 crocodiles...very hungry\n")
	x=int(input(""))
	if(x==1):
		print(name,"very intelligent..A lion hungry since past 2 weeks is obviously dead\n")
		time.sleep(2)
		seven()
	if(x==2):
		print(name,"dead")
		print("\n")
	if(x==3):
		print("dead",name)
		print("\n")		

def seven():
	print("You escaped from the mysterious cave and have reached the opposite part of the island")
	print("You have managed to find some fruits and fresh water")
	print("time is 23:00")
	print("make your choice",name)
	print("1) sleep in dark")
	print("2) keep moving in absolute dark")
	print("3) use dragon friend to burn fire and sleep near fire\n")
	x=int(input(""))
	if(x==1):
		print(name,"its very risky\n")
	if(x==2):
		print(name,"you are not an Owl\n")
	if(x==3):
		print("good,fire will keep the animals away",name)
		print("\n")
		time.sleep(2)
		eight()
	
def  eight():
	print("you woke up fresh...it was a comfortable night...time is 5:00")
	print("make your choice",name)
	print("1) move ahead")
	print("2) keep sleeping there")
	print("3) have RedBull...might give you wings to fly and escape the island\n")
	x=int(input(""))
	if(x==1):
		print(name,"you are not lazy\n")
		time.sleep(2)
		choose()
	if(x==2):
		print(name,"this ain't your home \n")
	if(x==3):
		print(name,"planning to go straight up with those wings?\n")
def choose():
	print("the story continues...how do you want it to be?")
	time.sleep(2)
	print("1) realistic")
	time.sleep(2)
	print("2) magical and fictional")
	x=int(input(""))
	if(x==1):
		print("your journey begins..""\n")
		time.sleep(1)
		real_1()
	if(x==2):
		print("your magical journey begins"" \n")
		time.sleep(1)
		mag_1()

def real_1():
	print("At this part of the beach lives some tribal men...who surprisingly speak english")
	print("They also have large boats..capable enough to reach a neighbouring nation")
	print("make your choice",name)
	print("1) Go talk to them about borrowing their boats ")
	print("2) observe their behaviour first ...make sure they dont eat humans")
	print("3) live your life...make it large go and fight the whole tribe")
	x=int(input(""))
	if(x==1):
		print(name,"this is too risky they might eat you\n")
	if(x==2):
		print(name,"good job\n")
		time.sleep(2)
		real_2()
	if(x==3):
		print(name,"u lived your life and now you are dead\n")

def real_2():
	print("You observed the tribal people and found out they are harmless")
	print("You also discovered that they are looking for something missing")
	print("make your choice",name)
	print("1) Go talk to them about borrowing their boats ")
	print("2) take your dragon and kill them all ")
	print("3) live your life...make it large go and fight the whole tribe")
	x=int(input(""))
	if(x==1):
		print(name,"conversation was interesting\n")
		time.sleep(2)
		real_3()
	if(x==2):
		print(name,"little dragon proved to be their friend and killed you\n")
	if(x==3):
		print(name,"u lived your life and now you are dead\n")

def real_3():
	print(name,"- Hey man....I want to borrow your boat")
	print("Tribal man- We will do anything for you, help us find the last successor of deity we worship")
	print(name,"-last what....?")
	print("Trival man- Its a dragon..")
	print("make your choice",name)
	print("1) Give him the Dragon and borrow their boat\n")
	print("2) Beg them for their boat\n")
	print("3) kill the dragon along with all the 200 tribal men and take their boat\n")
	x=int(input(""))
	if(x==1):
		print("_____________________________________________")
		print("congractulations",name," you have survived ..\n")
		print("---------------------------------------------")
	if(x==2):
		print(name,"they made you their slave..\n")
	if(x==3):
		print(name,"u died \n game over")		

	
def mag_1():
	print("while moving ahead, you have found a treasure map\n The map says OLD LAMP is the GOLD LAMP\nonce the golden lamp is found it fulfills all the needs of its user")
	print("make your choice",name)
	print("1) just keep the map...might be a good paper to burn fire")
	print("2) Leave the map and move")
	print("3) your need is a boat...find the lamp to get a boat")
	x=int(input(""))
	if(x==1):
		print("3rd option was more opt\n")
	if(x==2):
		print(name,"it was your last hope...poor\n")
		
	if(x==3):
		print(name,",you have a sharp mind..\n")
		time.sleep(2)
		mag_2()

def mag_2():
	print("There are 3 ways to get the gold lamp..\n ")
	print("make your choice",name)
	print("1) posionous spiders...instant death")
	print("2) deadly wasp....instant death")
	print("3) mosquitoes...may infect you with Dengue")
	x=int(input(""))
	if(x==1):
		print(name,"You are dead\n")
	if(x==2):
		print(name,"You are dead\n")
		
	if(x==3):
		print(name,"You may get dengue virus but dont worry once u get a boat and reach a nation its curable \n")
		time.sleep(2)
		mag_3()

def mag_3():
	print("You have reached the place where the ancient golden lamp is supposed to be placed..\ninstead you found a old rusted iron lamp..\nDon't forget its the magical world ")
	print("make your choice",name)
	print("1) Throw the lamp and move back through one of those 3 ways")
	print("2) lit the mysterious lamp by your fire breathing friend")
	print("3) wait to die there")
	x=int(input(""))
	if(x==1):
		print(name,"most probably u will soon b dead\n")
	if(x==2):
		print(name,"acted smartly\n")
		time.sleep(2)
		mag_4()			
	if(x==3):
		print(name,"You are dead\n")

def mag_4():
	print("nothing happened when you lit your lamp...\n")
	time.sleep(2)
	print("you closed your eyes and magical things happened the moment you opened your eyes\n")
	time.sleep(2)
	print("You are sitting in your home along with the lamp\n")
	time.sleep(2)
	print("You blink your eyes again and find that your room has become of gold....MAGIC\n")
	time.sleep(2)
	print("Game- Never met a genius like you,",name,"\nyou won")
start()


