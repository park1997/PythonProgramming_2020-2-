id_list=["asd"]
while 1:
    a=input("id")
    if a in id_list:
        print("이미 존재하는 아이디")
        continue
    else:
        print("성공")
        break
