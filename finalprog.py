#!/usr/bin/env python3
answer = input(" Art thee ready for thy quest?! (Yea/Nay): ")

while True:
    if answer.lower().strip() == "yea":

        while True:
            answer = input("You're on a quest for the holy grail! You are King Arthur out to prove you are the greatest monarch.\n"
                       "You meet Tim the Enchanter, who directs you to a cave which is supposedly the location of the Grail.\n "
                       "You learn the entrance to the cave is guarded by the Rabbit of Caerbannog.\n"
                       "As you approach the entrance you see this bunny, but it looks docile, even cute\n"
                       "but you have heard of its terrible powers and ferocious nature. What do you do?\n"
                       " A. Attacketh the bunny with full force of thy might! \n"
                       " B. Go up and pet the rabbit\n"
                       " C. Taketh no chances and throweth thy holy hand grenade!\n").lower().strip()
            if answer == "a":
                exit("The bunny anticipates this and activates his trap card. You drop down an endless hole, "
                      "never to return, you have died!")
            elif answer == "b":
                while True:
                    answer = input("You walk slowly toward the rabbit in a non-threatening way with vigorous jazz hands.\n"
                          "The rabbit does not react. You remember you have a bag of carrots with you because they are your favorite \n"
                          "vegetable, you know he would love them! But you also know he is now within arms reach! You can end him \n"
                          "now! Or you know... just pet him. What do you do? \n"
                          "A. pet the rabbit \n"
                          "B. feedeth the rabbit thy carrots! \n"
                          "C. striketh the rabbit down! \n").lower().strip()
                    if answer == "a":
                        while True:
                            answer = input("You put hand on the rabbit and pat in gently it's head. The rabbit seems to enjoy it \n"
                            "and even starts to pur. You start to to scratch it's ear, when suddenly the rabbit says \n"
                            "'Oh right there thats the right spot.' You jump back in surprise. You think to yourself \n"
                            "By odin's beard! the rabbit can speaketh!\n"
                             "What do you do?\n"
                            'A. introduceth yourself, thee doth not wanteth to be malapert\n'
                            "B. Killeth the rabbit while tis guardeth is down!\n").lower().strip()

                            if answer == "a":
                                while True:
                                    answer = input('You introduce yourself "Mine own nameth is king arthur, I leadeth the knights of \n '
                                     'the round table and i am on a quest to seeketh the holy grail.  \n'
                                     'What is thy nameth? and i wast wondering if be true i may passeth into the cave \n'
                                     'behind thee?" The rabbit introduces itself as "My name is Beelzebub! THE DARK PRINCE\n'
                                     'THE BREAKER OF GOOD! THE CENTER OF ALL EVIL! AND THE STEALER OF CANDY FROM LITTLE CHILDREN,\n'
                                     'but you can call me Beelz. Nice to meet you! And as for passage in my cave it will cost \n'
                                     'you food." You remeber you have your carrots, but you do not have much and thats all\n'
                                     'you have until the next village which is about 2 days trip away. What do you do? \n'
                                     'A. Feed him your carrots\n'
                                     'B. Try to bargin with him\n').lower().strip()
                                    if answer == "a":
                                        exit("You decide to feed him your carrots. You grab them out of your bag and hand\n"
                                             "them to Beelz. He eats them very fast and asks 'Do you have them anymore?\n"
                                             "Cause that was not enough!' You say with surprise 'How much can one rabbit consume?!\n"
                                             " yond an entire days w'rth of food. Thats all i has!' The hair on beelz sticks staright\n"
                                             "up and he grows 3 times larger than you, he says in a demonic voice 'It was not enough, but\n"
                                             "you are!' then swallows you whole. You died in the rabbits stomach being melted by acid")
                                    elif answer == "b":
                                        exit("You say to the rabbit 'Sir Beelz, I'm afraid i has't not any food i can spareth'\n"
                                             "Beelz  looks down at the ground in disappointment, but then looks with hungry eyes\n "
                                             "'If you have no food you are food!' He huffs then puffs and blows a stream of hellfire\n"
                                             "straight toward your face, melting it staight to bone. Conrats you'll make a good human\n"
                                             "steak dinner tonight.")
                                    else:
                                        print("Art thee no more brain than stone? The only options art A or B!")


                            elif answer == "b":
                                exit("You try to grab your sword but the rabbit is to quick and swiftly jumps on your\n"
                                     "hand. Its start's ripping your hand apart. With your other hand you pull the pin off\n"
                                     "the holy hand grenade on your belt and it explodes killing you, and the demon rabbit\n"
                                     "At least you died honorably this time, You should probably try again maybe be a bit\n"
                                     "nicer next time?")
                            else:
                                print("Art thee no more brain than stone? The only options art A or B!")

                    elif answer == "b":
                        exit("You stick your hand out with he carrot in it. The rabbit starts to sniff it at first then \n"
                              'starts to nibble on it. You think to yourself "It likes the carrot! maybe this rabbit is not so bad\n'
                              'after all, maybe you could even keep it as a pet!.....\n'
                              "as you're dwelling in your own thoughts, the rabbit finishes it's carrot, but it's still hungry.\n"
                              "you start notice even though it is done, it keeps on eating straight into your hand! You try to \n"
                              "stop it, but it's to late. The rabbit jumps and starts devouring your face next. You are dead ")

                    elif answer == 'c':
                        exit("You unsheath mighty excalibur and swiftly slash it down at the demonic rabbit, but it is too fast\n"
                             "It's reflex are supernatural and too speedy for you to comprehend. The rabbit dashes right behind you\n"
                             "and the last thing you hear is a hiss before it devours you whole.")
                    else:
                        print("Art thee no more brain than stone? The only options art A, B, or C!")
            elif answer == 'c':
                while True:
                    answer = input("Thy grenade explodes with the furry of a 1000 gods oblit'rating the rabbit into nothingness. All you see \n"
                          "before you now is scorched earth and the cave entrance cleared. You trot into to the cave in search for \n"
                          "for the grail, but alas you see no signs of the golden cup. But jinkees! you found a clue! You find an \n"
                          "inscription from Joseph of Arimathea (last known holder of the grail) directing you to the Castle of Aarrgh \n"
                          "As you're exiting the cave, you hear a loud rumble! Behind you see a gargantuan monster charging at you. \n"
                          "the monster looks like a giant animated bull. What do you do?\n"
                          "A. Chargeth backeth at the monster, that gent is nay matcheth for the power of excalibur! A coward dies \n"
                          "a thousand times before his death, but the valiant taste of death but once! \n"
                          "B. Runneth liketh a sissy: ").lower().strip()
                    if answer == "a":
                        while True:
                            print("You draw the mighty excalibur and wait for the bull to come to you.\n"
                                  "you see the bull coming closer and ready your weapon. You yell 'FOR CAMELOT!!!' and slice the\n"
                                  "bull in two as if it was butter. The two halves of the beast lie on the floor on either side\n"
                                  "of you and walk out of the cave triumphantly! You start your journey to the Castle of Aarrgh\n"
                                  "I hope you enjoyed that because thats the only part of this story you'll be epic in.\n")
                            answer = input("The journey was long and arduous. It took many bags of carrots to help feed you along\n"
                                            "the way. By your calculations you are only 3,025 steps more toward the location \n"
                                           "of the grail! You're so close you can just imagine the wine you would be drinking from it\n"
                                           " Until you encounter a bridge guarded by a bridge troll. The troll says\n"
                                           "' Stop! Who would cross the Bridge of Death must answer me these questions five, or off the bridge thou shall dive.'\n"
                                           "what do you do?\n"
                                           "A. Paunch the troll, thee has't nay timeth f'r this\n"
                                           "B. Say 'Asketh me the questions, bridgekeep'r.  I am not afraid!'\n")
                            if answer == "a":
                                exit("Before you can even touch your sword, the troll could sense your intent and with a wisp \n"
                                     "of his hand you are sent flying into the air and down to the cliff into lava. You should have\n"
                                     "you should have just answered the questions. Politeness can get you a long way! ")
                            elif answer == "b":
                                while True:
                                    answer = input("The troll says 'alright first question!, what is your name?\n"
                                               "A. King Arthur \n"
                                               "B. Sir Lancealot\n"
                                               "C. Sir Gallahad \n"
                                               "D. Bob the builder\n").lower().strip()
                                    if answer == "a":
                                            answer = input("'Good, what is your quest?\n"
                                                           "A. Seek the holy grail\n"
                                                           "B. Seek ark of the covenant\n"
                                                           "C. El derado \n"
                                                           "D. Just Cause \n").lower().strip()
                                            if answer == "a":
                                                while True:
                                                    answer = input("What is your favorite color?: \n"
                                                               "A. Blue\n"
                                                               "B. Gamboge\n"
                                                               "C. chartreuse\n"
                                                               "D. Yellow\n"
                                                               "E. Red \n").lower().strip()
                                                    if answer == "d":
                                                        while True:
                                                            answer = input("Fourth question, what is th capital of Assyria? \n"
                                                                        "A. Beirut \n"
                                                                        "B. Balawat \n"
                                                                        "C. Assur \n"
                                                                        "D. Nimrud\n").lower().strip()
                                                            if answer == 'c':
                                                                answer = input("Correct! What is the airspeed velocity of an unladen swallow? \n"
                                                                           "A. Ask him to be more specific \n"
                                                                           "B. 57 mph \n"
                                                                           "C.  9.5 meters per second \n"
                                                                           "D. Speed of light\n").lower().strip()
                                                                if answer == 'a':
                                                                    print("You ask him 'What do you mean? An African or European swallow?' \n"
                                                                      "The troll says ' What? I don't know!' and he wisped away off over the cliff")
                                                                    exit("You make your way to the castle of Aarrgh and find it abandoned. The halls \n"
                                                                     "were empty and walls crumbling. You search thru the entire place trying to find any trace \n"
                                                                     "of thr grail until you found a large door locked inside the basement. You wer able to open \n"
                                                                     "easily by slicing it thru with excalibur. The room was empty except for one wooden cup \n"
                                                                     "with the words etched in 'holy grail' on the side. You were fooled and bamboozled, there \n"
                                                                     "has been no grail this entire time, but it wasn't the destination that mattered. but the journey itsef \n"
                                                                     "you proved that you're an olay monarch that was fooled to go on a fae quest. the end")
                                                                elif answer == 'a' or 'b' or 'd':
                                                                    exit(" You took a guess, and it was wrong, now that troll flys you away \n"
                                                                             "at the speed you said")
                                                                else:
                                                                    print("Art thee no more brain than stone? The only options art the ones I gave you!")
                                                            elif answer == 'a' or 'b' or 'd':
                                                                exit("'Wrong city!' the troll says 'but here let me show you where \n"
                                                                 "it really is!' and he sends you flying into the sky, somewhere toward the middle east")
                                                        else:
                                                            print("Art thee no more brain than stone? The only options art the ones I gave you!")
                                                    elif answer == "a" or "b" or 'c' or 'e':
                                                        exit("you say the color, but you realize it was wrong. you say \n"
                                                             "'No I meant, Yel-' and before you can finish your sentence \n"
                                                             "you are sent flying into oblivion while finishing the rest of your \n"
                                                             "sentence 'loooooooooooooow' ")
                                                    else:
                                                        print("Art thee no more brain than stone? The only options art the ones I gave you!")
                                            elif answer == "b" or "c" or 'd':
                                                exit("'You really don't know the very thing you seek? What are you even doing\n"
                                                     "here then? off you go' the troll says and wisps his hand you go flying \n"
                                                     "into the stratosphere")
                                            else:
                                                print(
                                                    "Art thee no more brain than stone? The only options art the ones I gave you!")
                                    elif answer == 'b' or 'c' or 'd':
                                        exit("How do you not know your own name? What kind of monarch are you?\n"
                                             "you deserve death. You should have paid attention to the story more\n"
                                             "at the beginning ")
                                    else:
                                        print("Art thee no more brain than stone? The only options art A, B, or C!")


                            else:
                                print("Art thee no more brain than stone? The only options art A or B!")
                    elif answer == "b":
                        exit("Your sprint with all the energy in your body towards the cave entrance! As you flee, the entrance \n"
                             "is only a few more feet away, but alas you feel a horn penetrate through your back and straight \n"
                             "thru your chest. You should have fought the bull like a true king would. You have died! ")
                    else:
                        print("Art thee no more brain than stone? The only options art A or B!")

            else:
                print("Art thee no more brain than stone? The only options art A, B, or C!")


    else:
        print("Well yond is too lacking valor and honor! Thy only choice is yea.")
        answer = input(" Art thee ready for thy quest?! (Yea/Nay): ")
