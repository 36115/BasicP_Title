# sum = 0
# n = 3

# for i in range(n) :
#     sum += i + 1

# print(sum)

# ------------------------------------- #

# for i in range (10) :
#     i += 1
#     # if (i % 2) == 0 :
#     #     print("Even number: ", i)
#     print (i * i)

# ------------------------------------- #

# x = int(input("ใส่แม่สูตรคูณ: "))

# print("# ------------------------------------- #")

# for i in range (12) :
#     print(x, "x", i+1, "=", x * i)

# print("# ------------------------------------- #")

# ------------------------------------- #

# i = 0
# while i < 5 :
#     print("WOW")
#     i += 1
#     if i == 4 :
#         break

# ------------------------------------- #

# start = True

# while start :
#     print("เลือกข้อที่ต้องการเล่น")
#     print("ข้อที่ [1] โจทย์แรก")
#     print("ข้อที่ [2] โจทย์สอง")
#     print("ข้อที่ [3] โจทย์สาม")
#     x = int(input("กรุณาเลือก: "))
#     if x == 1 :
#         print("WOWOWOWOWOW")
#     elif x == 2 :
#         print("XD")
#     elif x == 3 :
#         print("sdfijijodfgjfdg")
#     else :
#         print("กรุณาเลือกใหม่อีกครั้ง")

#     start = False

# ------------------------------------- #

health = 100
weapon = {1: 50, 2: 20, 3: 60}

state = True
fight = False
add = False

while state and fight == False :
    print("--- เลือกเมนู ---")
    print("ตัวเลือก [1] สู้")
    print("ตัวเลือก [2] ไปละบาย")
    options = int(input("กรุณาเลือก: "))
    if options == 1 :
        fight = True
        attack = int(input("กรุณาใส่จำนวนครั้งที่จะโจมตี: "))
        while add == False and attack > 0  :
            print("--- Monster Info ---")
            print("Monster: Tung Tung Tung Sahur")
            print("Health: ", health)
            print("Attack left:", attack)
            print("--- เลือกอาวุธที่จะโจมตี ---")
            print("อาวุธ [1] Damage: 50 HP")
            print("อาวุธ [2] Damage: 20 HP")
            print("อาวุธ [3] Damage: 60 HP")
            print("-----------------------")
            options = int(input("กรุณาเลือก: "))
            health -= weapon[options]
            attack -= 1

            if health == 0 :
                print("ยินดีด้วยคุณชนะ!!!!")
                break
            elif health < 0 :
                add = True
                health = 100
                while fight and add and health > 0 :
                    print("ยินดีด้วย! คุณได้ปลุก Monster ตัวใหม่ขึ้นมานั้นก็คือ Bombombini Guzzini")
                    attack = int(input("กรุณาใส่จำนวนครั้งที่จะโจมตี: "))
                    while add == True and attack > 0 :
                        print("--- Monster Info ---")
                        print("Monster: Bombombini Guzzini")
                        print("Health: ", health)
                        print("Attack left:", attack)
                        print("--- เลือกอาวุธที่จะโจมตี ---")
                        print("อาวุธ [1] Damage: 50 HP")
                        print("อาวุธ [2] Damage: 20 HP")
                        print("อาวุธ [3] Damage: 60 HP")
                        print("-----------------------")
                        options = int(input("กรุณาเลือก: "))
                        health -= weapon[options]

                        if health < 0 :
                            print("เสียใจด้วย คุณตายแล้ว!!")
                            break

    elif options == 2 :
        print("เคกลับบ้านนอน T_T")
        break
    else :
        print("what da hell are you talking bout???")
        break
