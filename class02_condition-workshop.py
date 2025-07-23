distance = int(input("ระยะทาง: "))

if distance <= 4:
    price = 0
elif distance <= 5 or distance <= 50:
    price = 10
elif distance <= 51 or distance <= 100:
    price = 15
elif distance <= 101 or distance <= 300:
    price = 25
elif distance <= 301 or distance <= 500:
    price = 35
else:
    price = 45

if distance >= 5 and distance <= 500:
    print("ราคา", price, "บาท")
else:
    print("ไม่มีค่าจัดส่ง ส่งฟรี")
    