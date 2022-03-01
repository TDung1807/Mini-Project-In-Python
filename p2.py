# Nguyễn Tiến Dũng đẹp trai làm cái này đó ...


print ("Xin chào đến với game : Điền vào chỗ trống")

print ("Luật chơi khá đơn giản :")
print ("Bạn sẽ điền những từ trong khung gợi ý vào đoạn văn . \n Mỗi câu trả lời đúng bạn sẽ được cộng 2 điểm .")
print ("Nhưng , nếu bạn chỉ cần sai một câu thì bạn sẽ thua ngay lập tức và bị loại khỏi vòng chơi ! \n Vậy nên hãy làm nó thật cẩn thận nhé !!")
print ("Nếu bạn được 10 điểm thì bạn thật giỏi !")

# Nguyễn Tiến Dũng đẹp trai làm cái này đó ...

input ("Bấm enter để bắt đầu")
score = 0

print ("Những từ gợi ý : (Bạn sẽ điền những từ này vào những ô trống dưới đây)")
print ("Ô gợi ý nằm ở         ||")
print ("                      ||")
print ("                      ||")
print ("                      vv")
print ("|-----------------------------------------------------|")
print ("|  1. Đẹp trai                           2. Rất giỏi  |")
print ("|                                                     |")
print ("|                5. Nguyễn Tiến Dũng                  |")
print ("|  3. Lớp 8/4                  4. có rất nhiều bạn bè |")
print ("|_____________________________________________________|")

print ("")
print ("")

# Nguyễn Tiến Dũng đẹp trai làm cái này đó ...


print ("Tên tôi là 1._______ .Tôi học 2._______ và tôi 3.________________ để chơi cùng.")
print ("Tôi học trường Trần Quốc Toản , và tôi học 4.________ nên tôi thường được bố mẹ thưởng.\n Tóm lại , tôi rất 5.________.")


ans1 = input ("1 : ")
if ans1 == "5":
    print ("Đúng rồi ! ")
    score +=2
    print ("Bạn đang có "+ str(score)+ " điểm")
else :
    print ("Sai ! ")
    input ("Bạn bị loại !")
    quit()

# Nguyễn Tiến Dũng đẹp trai làm cái này đó ...

ans2 = input("2 : ")
if ans2 == "3":
    print ("Đúng rồi")
    score +=2
    print ("Bạn đang có "+ str(score)+ " điểm")
else :
    input ("Bạn bị loại !")
    quit()

# Nguyễn Tiến Dũng đẹp trai làm cái này đó ...

ans3 = input ("3 : ")
if ans3 == "4":
    print ("Đúng rồi")
    score +=2
    print ("Bạn đang có "+ str(score)+ " điểm")
else :
    input ("Bạn bị loại !")
    quit()

ans4 = input ("4 : ")
if ans4 == "2":
    print ("Đúng rồi")
    score +=2
    print ("Bạn đang có "+ str(score)+ " điểm")
else :
    input ("Bạn bị loại !")
    quit()

ans5 = input ("5 : ")
if ans5 == "1":
    input ("Ghê =)))")
    score +=2
else :
    input ("Non vậy :))?")
    quit()

print("")
print("")
print("")
input ("Bấm enter để xem điểm ")
print ("Điểm của bạn : "+ str(score))

if score == 10 :
    print ("Bạn giỏi thật đấy")

# Nguyễn Tiến Dũng đẹp trai làm cái này đó ...