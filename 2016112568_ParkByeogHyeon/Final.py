class member(object):
    def __init__(self):
        self.member_account_info=[]
        self.member_info=[]
        self.current_login_num=-1
        self.timeline_num=[]
    def create_member(self):
        self.name=input("이름을 입력하세요")
        self.ID=input("아이디를 입력하세요")
        self.password=input("비밀번호를 입력하세요")
        self.member_account_info.append([self.name,self.ID,self.password])
        self.timeline_num.append(0)
        self.member_info.append([])

    def input_member_info(self):
        if(len(self.member_info[self.current_login_num])==0):
            self.email=input("이메일을 입력해주세요 :")
            self.profile=input("프로필을 설명해주세요 :")
            self.gender=input("성별을 입력해주세요 : ")
            self.member_info[self.current_login_num].append(self.email)
            self.member_info[self.current_login_num].append(self.profile)
            self.member_info[self.current_login_num].append(self.gender)
        elif(len(self.member_info[self.current_login_num])==3):
            answer=int(input("이미 입력된 회원 정보가 있습니다.\n 수정하시겠습니까?\n 네 - 1\n아니오 - 2"))
            if(answer==1):
                self.new_email=input("이메일을 입력해주세요 :")
                self.new_profile=input("프로필을 설명해주세요 :")
                self.new_gender=input("성별을 입력해주세요 : ")
                self.member_info[self.current_login_num][0]=self.new_email
                self.member_info[self.current_login_num][1]=self.new_profile
                self.member_info[self.current_login_num][2]=self.new_gender
    def update_member_info(self):
        kind=int(input("수정하고 싶은 정보를 입력하시오 :\n1 - ID\n2 - password\n3 - profile\n"))
        if(kind==1):
            new_ID=input("수정할 ID를 입력하시오 :")
            self.member_account_info[self.current_login_num][1]=new_ID
        elif(kind==2):
            new_password=input("수정할 password를 입력하시오 :")
            self.member_account_info[self.current_login_num][2]=new_password


    def remove_member_info(self):
        del self.member_account_info[self.current_login_num]

    def show_member_info(self):
        if(len(self.member_info[self.current_login_num])==0):
            print("이름 : %s"%self.member_account_info[self.current_login_num][0])
            print("ID : %s"%self.member_account_info[self.current_login_num][1])
        else :
            print("이메일 : %s"%self.member_info[self.current_login_num][0])
            print("프로필 설명 : %s"%self.member_info[self.current_login_num][0])
            print("성별 : %s"%self.member_info[self.current_login_num][0])



    def log_in(self):
        num=10
        while(True):
            input_id=input("아이디를 입력하시오 : ")
            for i in range(len(self.member_account_info)):
                if(input_id==self.member_account_info[i][1]):
                    num=i
                    break
                else:
                    num=10
            if(num==10):
                print("아이디가 올바르지 않습니다.")
            else:
                input_pw=input("비밀번호를 입력하시오 :")
                if(input_pw==self.member_account_info[num][2]):
                    print("로그인 되었습니다.")
                    self.current_login_num=num
                    break
                else:
                    print("비밀번호를 잘못 입력하셨습니다.")
    def log_out(self):
        self.current_login_num=-1





class timeline(object):
    def __init__(self):
        self.timeline=[]
        self.timeline_time=[]
        self.timeline_comment=[]
        self.timeline_writer=[]

    def add_timeline(self,num,num2,member_info):
        num2[num]+=1
        thing=input()
        self.timeline.append([thing,[0,[]],[num,num2[num]],[]])
        import time
        now=time.localtime()
        self.timeline_time.append([now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min])
        self.timeline_comment.append([])
        self.timeline_writer.append(member_info[num][1])


    def update_timeline(self,num,num2,a):
        for i in range(len(self.timeline)):
            if(self.timeline[i][2][0]==num):
                if(self.timeline[i][2][1]==a):
                    new_timeline=input("타임라인을 새로 작성해 주세요 :")
                    self.timeline[i][0]=new_timeline

    def tag_friends(self,num,num2,member_info):
        a=int(input(print("다른사람을 태그하시겠습니까? \n1 - 네\n2 - 아니오")))
        if(a==1):
            print("태그하고싶은 사람의 번호를 입력해주세요 :")
            for j in range(len(member_info)):
                print("%d - %s"%(j+1,member_info[j][1]))
            b=int(input())
            for i in range(len(self.timeline)):
                if(self.timeline[i][2][0]==num):
                    if(self.timeline[i][2][1]==num2):
                        if member_info[b-1][1] in self.timeline[i][3]:
                            print("이미 태그된 회원 입니다.")
                        else:
                            self.timeline[i][3].append(member_info[b-1][1])





    def show_my_timeline(self,num):
        for j in range(len(self.timeline)):
            if(self.timeline[j][2][0]==num):
                if(self.timeline[j][2][1]==0):
                    print("게시물이 존재하지 않습니다 :\n")
                else:
                    print("작성자 : %s" %self.timeline_writer[j])
                    print('-------------------------------------------')
                    print(self.timeline[j][0])
                    print("%04d/%02d/%02d  %02d:%02d \t좋아요 수 : %d" %(self.timeline_time[j][0],self.timeline_time[j][1],
                                                        self.timeline_time[j][2],self.timeline_time[j][3],self.timeline_time[j][4],self.timeline[j][1][0]))
                    print('-------------------------------------------')
                    print("태그 목록")
                    for i in range(len(self.timeline[j][3])):
                        print("아이디 : %s"%(self.timeline[j][3][i]))
                    print('-------------------------------------------')
                    print("댓글")
                    if(len(self.timeline_comment[j])==0):
                        print("")
                    else :
                        for i in range(len(self.timeline_comment[j])):
                            print("ID: %s \t%s" %(self.timeline_comment[j][i][0],self.timeline_comment[j][i][1]))
                    print("=====================================")

    def show_other_timeline(self,num):
        for j in range(len(self.timeline)):
            if(self.timeline[j][2][0]==num-1):
                if(self.timeline[j][2][1]==0):
                    print("게시물이 존재하지 않습니다.\n")
                else :
                    print("작성자 : %s" %self.timeline_writer[j])
                    print('-------------------------------------------')
                    print(self.timeline[j][0])
                    print('-------------------------------------------')
                    print("%04d/%02d/%02d  %02d:%02d \t좋아요 수 : %d" %(self.timeline_time[j][0],self.timeline_time[j][1],
                                                        self.timeline_time[j][2],self.timeline_time[j][3],self.timeline_time[j][4],self.timeline[j][1][0]))
                    print('-------------------------------------------')
                    print("태그 목록")
                    for i in range(len(self.timeline[j][3])):
                        print("아이디 : %s"%(self.timeline[j][3][i]))
                    print('-------------------------------------------')
                    print("댓글")
                    if(len(self.timeline_comment[j])==0):
                        print("")
                    else :
                        for i in range(len(self.timeline_comment[j])):
                            print("ID: %s \t%s" %(self.timeline_comment[j][i][0],self.timeline_comment[j][i][1]))
                    print("=================================================")


    def input_like(self,num,num2,current_num):
        a=int(input("몇번째 게시물을 좋아요 누르시겠습니까? "))
        for j in range(len(self.timeline)):
            if(self.timeline[j][2][0]==num-1):
                if(self.timeline[j][2][1]==a):
                    if(current_num in self.timeline[j][1][1]):
                        print("이미 좋아요를 누른 게시물 입니다.")
                    else :
                        self.timeline[j][1][0]+=1
                        self.timeline[j][1][1].append(current_num)

    def input_comment(self,num,num2,current_num,who):
        a=int(input("몇번째에 댓글을 남기시겠습니까 "))
        for j in range(len(self.timeline)):
            if(self.timeline[j][2][0]==num-1):
                if(self.timeline[j][2][1]==a):
                    b=input("댓글을 입력해주세요 : ")
                    self.timeline_comment[j].append([who,b])
    def remove_timeline(self,num,num2):
        a=int(input("지우고싶은 피드의 번호를 입력하시오 :\n"))
        for j in range(len(self.timeline)):
            if(self.timeline[j][2][0]==num):
                if(num2[num]==0):
                    print("게시물이 존재하지 않습니다.")
                elif(self.timeline[j][2][1]==a):
                    del self.timeline[j]
                    del self.timeline_time[j]
                    del self.timeline_comment[j]
                    del self.timeline_writer[j]
                    break
        for i in range(len(self.timeline)):
            if(self.timeline[i][2][0]==num):
                if(self.timeline[i][2][1]>a):
                    self.timeline[i][2][1]+=-1
        num2[num]+=-1

        num2[num]+=-1

    def remove_timeline_all(self,current_num,num):
        for i in range(len(self.timeline)):
            if(self.timeline[i][2][0]==current_num):
                del self.timeline[i]
                del self.timeline_time[i]
                del self.timeline_comment[i]
                del num[current_num]
                break
    def show_tagged_timeline(self,current_num,member_info):
        for j in range(len(self.timeline)):
            if member_info[current_num][1] in self.timeline[j][3]:
                print("작성자 : %s" %self.timeline_writer[j])
                print('-------------------------------------------')
                print(self.timeline[j][0])
                print('-------------------------------------------')
                print("%04d/%02d/%02d  %02d:%02d \t좋아요 수 : %d" %(self.timeline_time[j][0],self.timeline_time[j][1],
                                                        self.timeline_time[j][2],self.timeline_time[j][3],self.timeline_time[j][4],self.timeline[j][1][0]))
                print('-------------------------------------------')
                print("태그 목록")
                for i in range(len(self.timeline[j][3])):
                    print("아이디 : %s"%(self.timeline[j][3][i]))
                print('-------------------------------------------')
                print("댓글")
                if(len(self.timeline_comment[j])==0):
                    print("")
                else :
                    for i in range(len(self.timeline_comment[j])):
                        print("ID: %s \t%s" %(self.timeline_comment[j][i][0],self.timeline_comment[j][i][1]))
                print("=================================================")




mem=member()
line=timeline()
while(True):
    while(True):
        a=int(input("로그인을 원하시면 1, 회원가입을 원하시면하시면 2를 입력하세요"))
        if (a==1):
            mem.log_in()
            while(True):
                b=int(input("하고싶은 작업을 입력해주세요\n1 - 회원정보 입력\n2 - 회원정보 수정\n3 - 회원탈퇴\n4 - 회원정보 보이기\n5 - 타임라인 글 입력\n6 - 타임라인 수정하기\n7 - 게시물 삭제하기\n8 - 게시물 보기\n9 - 내가 태그된 게시물 보기\n10 - 로그아웃\n"))
                if(b==1):
                    mem.input_member_info()
                elif(b==2):
                    mem.update_member_info()
                elif(b==3):
                    mem.remove_member_info()
                    line.remove_timeline_all(mem.current_login_num,mem.timeline_num)
                    mem.log_out()
                    break
                elif(b==4):
                    mem.show_member_info()
                elif(b==5):
                    print("게시물을 입력해주세요 : \n")
                    line.add_timeline(mem.current_login_num,mem.timeline_num,mem.member_account_info)
                    line.tag_friends(mem.current_login_num,mem.timeline_num[mem.current_login_num],mem.member_account_info)
                    print(len(line.timeline))
                    for i in range(len(line.timeline)):
                        print(len(line.timeline[i][2]))

                elif(b==6):
                    if(mem.timeline_num[mem.current_login_num]==0):
                        print("게시물이 존재하지 않습니다.")
                    else :
                        print("수정하고 싶은 게시물의 번호를 입력해주세요 :")
                        line.show_my_timeline(mem.current_login_num)
                        a=int(input())
                        line.update_timeline(mem.current_login_num,mem.timeline_num,a)
                        line.tag_friends(mem.current_login_num,a,mem.member_account_info)
                elif(b==7):
                    line.remove_timeline(mem.current_login_num,mem.timeline_num)
                elif(b==8):
                    for i in range(len(mem.member_account_info)):
                        if(i==mem.current_login_num):
                            print(" %d - %s" %(i+1,"내 타임라인"))
                        else :
                            print(" %d - %s" %(i+1,mem.member_account_info[i][1]))
                    x=int(input("보고싶은 사람의 번호를 입력하시오 :"))
                    line.show_other_timeline(x)
                    like=int(input("좋아료를 누르시려면 1\n댓글을 남기시려면 2\n메뉴로 돌아가시려면 3번을 눌러주세요."))
                    if(like==1):
                        line.input_like(x,mem.timeline_num,mem.current_login_num)
                    elif(like==2):
                        line.input_comment(x,mem.timeline_num,mem.current_login_num,
                                          mem.member_account_info[mem.current_login_num][1])

                elif(b==9):
                    line.show_tagged_timeline(mem.current_login_num,mem.member_account_info)


                elif(b==10):
                    mem.log_out()
                    break
        elif a==2:
            name=input
            mem.create_member()
            break

        else:
            break
