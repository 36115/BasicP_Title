import os, time
queues = []
mainMenu = True

while mainMenu :
    os.system('cls')
    print("=================================================")
    print("=                                               =")
    print("=               ระบบจองคิวร้านหมาล่า               =")
    print("=                                               =")
    print("====================== Menu =====================")
    print("=                                               =")
    print("= [1]: สั่งเมนู                                    =")
    print("= [2]: เช็คคิว                                    =")
    print("=                                               =")
    print("=================================================")
    choice = int(input("เลือกเมนู: "))
    if choice == 1 :
        mainMenu = False
        queueMenu = True
        os.system('cls')

        while queueMenu :
            chooseSoup = int(input("เลือกน้ำซุป: "))
            chooseMala = int(input("เลือกหมาล่า: "))

            myQueue = len(queues)
            myQueue += 1

            queues.append({"queue": myQueue, "soup": chooseSoup, "mala": chooseMala})
            
            print("คุณอยู่คิวที่: ", myQueue)
            print(queues)
            input("Press Enter to continue...")
            mainMenu = True
            queueMenu = False
    elif choice == 2 :
        mainMenu = False
        queueCheck = True
        os.system('cls')

        while queueCheck :
            for queue in queues :
                print("=================== คิวหมายเลข", queue["queue"], "=================")
                print("= น้ำซุป: ", queue["soup"])
                print("= หมาล่า: ", queue["mala"])
                print("=================================================")

            print("=                                               =")
            print("= [x]: Exit                                     =")
            print("=                                               =")
            print("=================================================")

            # รับค่าตัวเลือกเมนูจากผู้ใช้
            menu = input("เลือกเมนู: ")
            if menu == "x" or menu == "X" :
                mainMenu = True
                queueCheck = False
            else :
                os.system('cls')
                print("Invalid menu!")
                time.sleep(1)
                os.system('cls')
    else :
        os.system('cls')
        print("Invalid menu!")
        time.sleep(1)
        os.system('cls')

# myQueue = 1
# myQueue -= 1

# if len(queue) > 0 :
#     queue[myQueue]["name"]
#     print("ตอนนี้คิวของคุณยังไม่ถึง")
