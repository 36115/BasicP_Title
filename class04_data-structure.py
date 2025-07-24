# x = ["tung", "sahur"]

# print(x[0], x[0], x[0], x[1])

# x[0] = "ta"
# print(x[0], x[0], x[0], x[1])

# x.append("te")
# print(x[2], x[2], x[2], x[1])

# x.pop(0)

# if x[0] == "tung" :
#     print("Found tung tung tung sahur")
#     print(x)
# else :
#     print("RIP tung tung tung sahur")
#     print(x)

# print("========================================")

# for i in range(len(x)) :
#     print("List", i, ":", x[i])

# score = [99, 88, 94, 85]
# sum = 0

# for i in range(len(score)) :
#     sum += score[i]

# print(sum)

# x = {
#         "name": "Tung Tung Tung Sahur",
#         "id": 12424304320
#     }

# print(x["name"])

# x["score"] = 100

# print(x)

students = [
    {"name": "Tung Tung Tung Sahur", "id": 68130500071, "score": 75},
    {"name": "Ta Ta Ta Sahur", "id": 68130500071, "score": 86},
    {"name": "Te Te Te Sahur", "id": 68130500071, "score": 93},
]

for student in students :
    if student["score"] >= 90 :
        student["score"] = "A"
    elif student["score"] >= 80 :
        student["score"] = "B"
    elif student["score"] >= 70 :
        student["score"] = "C"
    else :
        student["score"] = "F"
    
print(students)
