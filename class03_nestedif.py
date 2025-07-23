# username = input("Username: ")
# password = input("Password: ")

# if username == "admin":
#     if password == "admin123":
#         print("You're admin")
#     else:
#         print("Wrong")
# elif username == "user":
#     if password == "user123":
#         print("You're user")
#     else:
#         print("Wrong")
# else:
#     print("Not found")

# -------------------------------------- #

meme = str(input("เลือก Meme (ตะแน่ว หรือ brainrot): "))

if meme == "ตะแน่ว" :
    word = int(input("เลือกเนื้อเรื่องของคุณ (1. เดอะมอล์บางกะปิ 2. เดอะมอล์ลาดพร้าว 3. สยามสแควร์): "))
    if word == 1 :
        meme += "เดอะมอล์บางกะปิ"
    elif word == 2 :
        meme += "เดอะมอล์ลาดพร้าว"
    elif word == 3 :
        meme += "สยามสแควร์"
    else :
        print("Are you serious?")
elif meme == "brainrot" :
    word = int(input("เลือกเนื้อเรื่องของคุณ (1. Tung Tung Tung Sahur 2. Bombombini Gusini 3. Chimpanzini Bananini): "))
    meme += " - "
    if word == 1 :
        meme += "Tung Tung Tung Sahur"
    elif word == 2 :
        meme += "Bombombini Gusini"
    elif word == 3 :
        meme += "Chimpanzini Bananini"
    else :
        print("Are you serious?")
else:
    print("Wrong Meme")
    exit

print(meme)
