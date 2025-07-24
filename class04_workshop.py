# Variable
import os, time

# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    for movie in movie_list :
        print("Movie name: ", movie["movie_name"])
        print("Ticket price: ", movie["ticket_price"])
        print("=================================================")

# # ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
# def check_age(user_age, age_restriction):
#     # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
#     # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
 
# # ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
# def calculate_price(base_price, genre):
#     # TODO: ถ้า genre เป็น 'Romantic' บวกเพิ่ม 50 บาท
#     # ถ้าไม่ใช่ คืนราคาเดิม
 
# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO:
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    show_movies(movie_list)

    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = int(input("เลือกเมนู: "))
    if menu <= 1 or menu <= 5 :
        movie = menu
    else :
        print("Invalid menu!")
        time.sleep(5)
        os.system('cls')
    
    user_age = int(input("Type your age: "))
    check_age(user_age, age_restriction)

    # 3. รับอายุผู้ใช้
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
 
def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    menuPage = True

    while menuPage :
        # TODO: แสดงเมนูให้ผู้ใช้เลือก
        # 1. แสดงหนังทั้งหมด
        # 2. ซื้อตั๋วหนัง

        os.system('cls')
        print("=================================================")
        print("=                                               =")
        print("=  Welcome to super sigma skibidi ohio Theater  =")
        print("=                                               =")
        print("================== Theater Menu =================")
        print("=                                               =")
        print("= [1]: Show movies list                         =")
        print("= [2]: Buy movies list                          =")
        print("=                                               =")
        print("=================================================")

        # รับค่าตัวเลือกเมนูจากผู้ใช้
        menu = int(input("เลือกเมนู: "))
        if menu == 1 :
            menuPage = False
            while not menuPage :
                os.system('cls')
                print("================== Movies List ==================")
                show_movies(movies)
                print("=                                               =")
                print("= [x]: Exit                                     =")
                print("=                                               =")
                print("=================================================")

                # รับค่าตัวเลือกเมนูจากผู้ใช้
                menu = input("เลือกเมนู: ")
                if menu == "x" or menu == "X" :
                    menuPage = True
                else :
                    print("Invalid menu!")
        elif menu == 2 :
            menuPage = False
            while not menuPage :
                os.system('cls')
                print("=========== Choose Movies [1] - [5] =============")
                buy_ticket(movies)
        else :
            print("Invalid menu!")

    
        # TODO: ตรวจสอบเมนูที่เลือก
        # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
        # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
        # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง
 
# เรียก main เพื่อเริ่มโปรแกรม
main()
