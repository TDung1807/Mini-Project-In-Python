# Rock Paper Scissor game 


import random


print ("Chào mừng đến với game kéo búa bao.")


play = input ("Nhấn số 1 nếu bạn muốn bắt đầu trò chơi , số 2 nếu bạn muốn rời khỏi game.")



if play != "1":
    quit()



input ("okay bắt đầu thôi nào !")


chơi = True

while chơi == True :

    biendoi = ""


    computer = random.randint (1 ,3)


    if computer == 1:
        biendoi = "kéo"
    elif computer == 2 :
        biendoi = "búa"
    elif computer == 3 :
        biendoi = "bao"


    user = input ("Bạn chọn gì ? " + "1 : Kéo ; 2 : Búa ; 3 : Bao \n" + "Nhập lựa chọn của bạn : " )


    if user == "1" and biendoi == "kéo":
        print ("Hòa")

    elif user == "2" and biendoi == "búa" :
        print ("Hòa")


    elif user == "3" and biendoi == "bao":
        print ("Hòa")


    elif user == "1" and biendoi == "búa":
        print ("Bạn thua")

    elif user == "1" and biendoi == "bao":
        print ("Bạn thắng ")

    elif user == "2" and biendoi == "kéo":
        print ("Bạn thắng")
  

    elif user == "2" and biendoi == "bao":
        print ("Bạn thua")

    elif user == "3" and biendoi == "kéo":
        print ("Bạn thua")

    elif user == "3" and biendoi == "búa":
        print ("Bạn thắng")

    else :
        input ("Sai dữ liệu đầu vào , vui lòng chạy lại chương trình.")
        quit()

    again = input ("Bạn có muốn chơi lại hay không ? (Y / N) : ")

    if again.lower () != "y":
        break



