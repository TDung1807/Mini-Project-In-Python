
import os




input ("Chương trình mới :))) Bấm enter để vào luôn chương trình :))")



socau =  input ("Bạn muốn tạo bao nhiêu câu hỏi . (Tối đa : 5 câu) : ")



if socau == "1":
    
    input ("Vì bài làm của bạn có một câu hỏi nên chương trình đề xuất một câu hỏi của bạn có giá trị bằng 10 điểm")
    
    os.system("cls")

    nhap1 = input ("Nhập câu hỏi số 1 : ")

    c1 = input ("Câu hỏi đầu tiên sẽ là : " + nhap1 + ". Nếu chắc chắn hãy nhấn enter ")

    ans1 = input ("Đáp án của câu hỏi : " + nhap1 + ": ")

    print ("Ok đã nhận đủ hết tất cả thông tin bây giờ chuyển sang bước 3 :")


    input ("Bấm enter để chuyển sang trang làm bài cho học sinh :))) .")

    os.system ("cls")
    ten = input ("Họ và tên : ")
    os.system ("cls")

    input ("Nếu sẵn sàng rồi bấm enter để bắt đầu làm bài . ")

    print ("                              Phần làm bài của thí sinh :"+ ten)

    lambai1 = input (nhap1 + " Đáp án của bạn : ")

    if lambai1 == ans1 :
        input ("Đúng !")
        
    else :
        input ("Sai !")
        
    input ("Vậy là đã câu hỏi do thầy / cô bạn ra . Chúc bạn một ngày mới tốt lành và càng ngày càng học giỏi .")
    input = ("Bấm enter để xem điểm .")
    quit()


elif socau == "2":
    nhap1 = input ("Nhập câu hỏi số 1 : ")

    c1 = input ("Câu hỏi đầu tiên sẽ là : " + nhap1 + ". Nếu chắc chắn hãy nhấn enter ")

    ans1 = input ("Đáp án của câu hỏi : " + nhap1 + "Viết thường" +": ")

    nhap2 = input ("Nhập câu hỏi số 2 : ")

    c2 = input ("Câu hỏi đầu tiên sẽ là : " + nhap2 + ". Nếu chắc chắn hãy nhấn enter ")

    ans2 = input ("Đáp án của câu hỏi : " + nhap2 + "Viết thường" +": ")

    print ("Ok đã nhận đủ hết tất cả thông tin bây giờ chuyển sang bước 3 :")


    input ("Bấm enter để chuyển sang trang làm bài cho học sinh :))) .")

    os.system ("cls")

    ten = input ("Họ và tên : ")
    os.system ("cls")
    input ("Nếu sẵn sàng rồi bấm enter để bắt đầu làm bài . ")
    
    print ("                              Phần làm bài của thí sinh :"+ ten)
    
    
    lambai1 = input (nhap1 + " Đáp án của bạn : ")

    if lambai1 == ans1 :
        input ("Đúng !")

    else :
        input ("Sai !")

    lambai2 = input (nhap2 + " Đáp án của bạn : ")


    if lambai2 == ans2 :
        input ("Đúng")
    else :
        input ("Sai")
    
    input ("Vậy là đã hết câu hỏi do thầy / cô bạn ra . Chúc bạn một ngày mới tốt lành và càng ngày càng học giỏi .")
    input ("VUI LÒNG ĐỂ YÊN BÀI LÀM KHÔNG ĐƯỢC ẤN BẤT CỨ THỨ GÌ .")
    quit()



elif socau == "3":
    nhap1 = input ("Nhập câu hỏi số 1 : ")

    c1 = input ("Câu hỏi đầu tiên sẽ là : " + nhap1 + ". Nếu chắc chắn hãy nhấn enter ")

    ans1 = input ("Đáp án của câu hỏi : " + nhap1 + "Viết thường" +": ")

    nhap2 = input ("Nhập câu hỏi số 2 : ")

    c2 = input ("Câu hỏi đầu tiên sẽ là : " + nhap2 + ". Nếu chắc chắn hãy nhấn enter ")

    ans2 = input ("Đáp án của câu hỏi : " + nhap2 + "Viết thường" +": ")

    nhap3 = input ("Nhập câu hỏi số 3 : ")

    c3 = input ("Câu hỏi đầu tiên sẽ là : " + nhap3 + ". Nếu chắc chắn hãy nhấn enter ")

    ans3 = input ("Đáp án của câu hỏi : " + nhap3 + "Viết thường" +": ")

    print ("Ok đã nhận đủ hết tất cả thông tin bây giờ chuyển sang bước 3 :")


    input ("Bấm enter để chuyển sang trang làm bài cho học sinh :))) .")

    os.system ("cls")
    ten = input ("Họ và tên : ")
    os.system ("cls")

    input ("Nếu sẵn sàng rồi bấm enter để bắt đầu làm bài . ")


    print ("                              Phần làm bài của thí sinh :"+ ten)


    lambai1 = input (nhap1 + " Đáp án của bạn : ")

    if lambai1 == ans1 :
        input ("Đúng !")

    else :
        input ("Sai !")

    lambai2 = input (nhap2 + " Đáp án của bạn : ")


    if lambai2 == ans2 :
        input ("Đúng")
    else :
        input ("Sai")

    lambai3 = input (nhap3 + " Đáp án của bạn : ")


    if lambai3 == ans3 :
        input ("Đúng")
    else :
        input ("Sai")    

    input ("Vậy là đã hết câu hỏi do thầy / cô bạn ra . Chúc bạn một ngày mới tốt lành và càng ngày càng học giỏi .")
    input ("VUI LÒNG ĐỂ YÊN BÀI LÀM KHÔNG ĐƯỢC ẤN BẤT CỨ THỨ GÌ .")
    quit()



elif socau == "4":
    nhap1 = input ("Nhập câu hỏi số 1 : ")

    c1 = input ("Câu hỏi đầu tiên sẽ là : " + nhap1 + ". Nếu chắc chắn hãy nhấn enter ")

    ans1 = input ("Đáp án của câu hỏi : " + nhap1 + "Viết thường" +": ")

    nhap2 = input ("Nhập câu hỏi số 2 : ")

    c2 = input ("Câu hỏi đầu tiên sẽ là : " + nhap2 + ". Nếu chắc chắn hãy nhấn enter ")

    ans2 = input ("Đáp án của câu hỏi : " + nhap2 + "Viết thường" +": ")

    nhap3 = input ("Nhập câu hỏi số 3 : ")

    c3 = input ("Câu hỏi đầu tiên sẽ là : " + nhap3 + ". Nếu chắc chắn hãy nhấn enter ")

    ans3 = input ("Đáp án của câu hỏi : " + nhap3 + "Viết thường" +": ")

    nhap4 = input ("Nhập câu hỏi số 4 : ")

    c4 = input ("Câu hỏi đầu tiên sẽ là : " + nhap4 + ". Nếu chắc chắn hãy nhấn enter ")

    ans4 = input ("Đáp án của câu hỏi : " + nhap4 + "Viết thường" +": ")


    print ("Ok đã nhận đủ hết tất cả thông tin bây giờ chuyển sang bước 3 :")


    input ("Bấm enter để chuyển sang trang làm bài cho học sinh :))) .")

    os.system ("cls")
    ten = input ("Họ và tên : ")
    os.system ("cls")

    input ("Nếu sẵn sàng rồi bấm enter để bắt đầu làm bài . ")


    print ("                              Phần làm bài của thí sinh :"+ ten)

    lambai1 = input (nhap1 + " Đáp án của bạn : ")

    if lambai1 == ans1 :
        input ("Đúng !")

    else :
        input ("Sai !")

    lambai2 = input (nhap2 + " Đáp án của bạn : ")


    if lambai2 == ans2 :
        input ("Đúng")
    else :
        input ("Sai")

    lambai3 = input (nhap3 + " Đáp án của bạn : ")


    if lambai3 == ans3 :
        input ("Đúng")
    else :
        input ("Sai")    

    lambai4 = input (nhap4 + " Đáp án của bạn : ")


    if lambai4 == ans4 :
        input ("Đúng")
    else :
        input ("Sai")


    input ("Vậy là đã hết câu hỏi do thầy / cô bạn ra . Chúc bạn một ngày mới tốt lành và càng ngày càng học giỏi .")
    input ("VUI LÒNG ĐỂ YÊN BÀI LÀM KHÔNG ĐƯỢC ẤN BẤT CỨ THỨ GÌ .")
    quit()

elif socau == "5":
    nhap1 = input ("Nhập câu hỏi số 1 : ")

    c1 = input ("Câu hỏi đầu tiên sẽ là : " + nhap1 + ". Nếu chắc chắn hãy nhấn enter ")

    ans1 = input ("Đáp án của câu hỏi : " + nhap1 + "Viết thường" +": ")

    nhap2 = input ("Nhập câu hỏi số 2 : ")

    c2 = input ("Câu hỏi đầu tiên sẽ là : " + nhap2 + ". Nếu chắc chắn hãy nhấn enter ")

    ans2 = input ("Đáp án của câu hỏi : " + nhap2 + "Viết thường" +": ")

    nhap3 = input ("Nhập câu hỏi số 3 : ")

    c3 = input ("Câu hỏi đầu tiên sẽ là : " + nhap3 + ". Nếu chắc chắn hãy nhấn enter ")

    ans3 = input ("Đáp án của câu hỏi : " + nhap3 + "Viết thường" +": ")

    nhap4 = input ("Nhập câu hỏi số 4 : ")

    c4 = input ("Câu hỏi đầu tiên sẽ là : " + nhap4 + ". Nếu chắc chắn hãy nhấn enter ")

    ans4 = input ("Đáp án của câu hỏi : " + nhap4 + "Viết thường" +": ")


    nhap5 = input ("Nhập câu hỏi số 5 : ")

    c5 = input ("Câu hỏi đầu tiên sẽ là : " + nhap5 + ". Nếu chắc chắn hãy nhấn enter ")

    ans5 = input ("Đáp án của câu hỏi : " + nhap5 + "Viết thường" +": ")

    print ("Ok đã nhận đủ hết tất cả thông tin bây giờ chuyển sang bước 3 :")


    input ("Bấm enter để chuyển sang trang làm bài cho học sinh :))) .")

    os.system ("cls")

    ten = input ("Họ và tên : ")
    os.system ("cls")

    print ("                              Phần làm bài của thí sinh :"+ ten)

    input ("Nếu sẵn sàng rồi bấm enter để bắt đầu làm bài . ")

    print ("                              Phần làm bài của thí sinh :"+ ten)

    lambai1 = input (nhap1 + " Đáp án của bạn : ")

    if lambai1 == ans1 :
        input ("Đúng !")

    else :
        input ("Sai !")

    lambai2 = input (nhap2 + " Đáp án của bạn : ")


    if lambai2 == ans2 :
        input ("Đúng")
    else :
        input ("Sai")

    lambai3 = input (nhap3 + " Đáp án của bạn : ")


    if lambai3 == ans3 :
        input ("Đúng")
    else :
        input ("Sai")    

    lambai4 = input (nhap4 + " Đáp án của bạn : ")


    if lambai4 == ans4 :
        input ("Đúng")
    else :
        input ("Sai")


    lambai5 = input (nhap5 + " Đáp án của bạn :")

    if lambai5 == ans5 :
        input ("Đúng")
    else :
        input ("Sai")

    input ("Vậy là đã hết câu hỏi do thầy / cô bạn ra . Chúc bạn một ngày mới tốt lành và càng ngày càng học giỏi .")
    input ("VUI LÒNG ĐỂ YÊN BÀI LÀM KHÔNG ĐƯỢC ẤN BẤT CỨ THỨ GÌ .")
    quit()

          

else :
    print ("Sai dữ liệu đầu vào . Vui lòng chạy lại chương trình")


