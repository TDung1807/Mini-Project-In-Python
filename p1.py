
print ("Chào mừng đến với game : 'Mr.Dũng :))'")

play = input ("Bạn có muốn chơi game không (Y : yes ; N : no): ")

if play.lower() != "y":
        quit()

score = 0


print ("okay let's play :))")

answer1 = input ("Tên đầy đủ của Mr.Dũng ? Viết không dấu : ")

if answer1 == "Nguyen Tien Dung":
        print ("Correct !!")
        score += 2
else :
        print ("Incorrect !")
        score -= 1
answer2 = input ("Mr.Dũng mấy tuổi ? ")

if answer2 == "13":
        print ("Correct !")
        score +=2
else :
        input("Incorrect !")
        score -=1


answer3 = input ("Mr.Dũng học trường nào ? ")

if answer3 == "Tran Quoc Toan":
    print ("Correct")
    score +=2

elif answer3 == "TQT":
    print ("Correct")
    score +=2
else :
    print ("Incorect !")
    score -=1
answer4 = input ("Mr.Dũng học lớp 8 mấy ? ")
if answer4 == "8.4":
     print ("Correct !")
     score +=2

elif answer4 == "8/4":
    print ("Correct")
    score +=2
elif answer4 == "8-4":
    print ("Correct")
    score +=2
elif answer4 == "8_4":
    print ("Correct")
    score +=2
elif answer4.lower() == "tám tư":
    print ("Correct")
    score +=2
elif answer4.lower() == "tám bốn":
    print ("Correct")
    score +=2
else :
    input ("Incorrect")
    score -=1
answer5 = input ("Mr.Dũng có đẹp trai không ? Viết không dấu : Y : có ; N : không : ")

if answer5.lower() == "y":
    score += 2
    input ("Correct. Bấm enter để xem điểm : ")
else :
    input ("Incorrect. Bấm enter để xem điểm")
    score -=1


print("Điểm của bạn : " + str (score))



if score > 5 : 
    input ("Cũng biết khá nhiều về Dũng đấy .")
    
if score < 5 :
    print ("Biết hơi ít về Dũng đấy . Tìm hiểu Dũng thêm đi !!")