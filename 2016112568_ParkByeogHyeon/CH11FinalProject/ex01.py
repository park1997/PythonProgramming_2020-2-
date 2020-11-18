import time
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import requests
from notebook import Note
from notebook import NoteBook

class DonggukTime:
    """
    DonggukTime class(For Engineers)
    Author : Park ByeongHyeon
    Date : 2020-11-18
    """
    user_index=0
    df_timeline=pd.read_excel("timeline.xlsx")
    def __init__(self,details):
        self.name=details[0]
        self.id=details[1]
        self.pw=details[2]
        self.post_info=[]
        print(self.name, self.id, self.pw)

    def log_in(self):
        main()

    def show_timeline(self):
        for i in range(len(DonggukTime.df_timeline)):
            name,time,context,likes_num,grade,lecture_name,head_name=DonggukTime.df_timeline.loc[i]
            print("{} 번째 강의 평 : {}".format(i+1,head_name))
            print("{}".format("-"*50))
            print("작성자 : {}\n작성 시간: {}".format(name,time))
            print("{}".format("-"*50))
            print("과목 명 : {}\n강의 평점 : {}".format(lecture_name,grade))
            print("{}".format("-"*50))
            print("강의 평 내용\n")
            print(context)
            print("{}".format("-"*50))
            print()
            print()

    def write_timeline(self):
        post_head_name=input("글 제목을 입력 하세요.  >>  ")
        post_context=input("글 내용을 입력 하세요.  >>  ")
        post_lecture=input("강의 이름을 입력 하세요.  >>  ")
        while 1:
            post_grade=float(input("강의 평점을 0점 이상 10점 이하로 입력해 주세요. >> "))
            if post_grade>10:
                print("점수 범위를 초과 하셨습니다. 10점 이하로 입력해 주세요.  >>  ")
            elif post_grade<0:
                print("점수를 양수로 입력해 주세요.  >>  ")
            else:
                break
        now=time.localtime()
        post_now_time="%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)

        #나중에 글 삭제를 위해 정보 저장
        self.post_info.append([post_head_name,post_lecture,post_context])
        DonggukTime.df_timeline=DonggukTime.df_timeline.append({"작성자":self.name,"작성시간":post_now_time,"글내용":post_context,"좋아요수":0,"평점":post_grade,"과목명":post_lecture,"글제목":post_head_name},ignore_index=True)
        print("성공적으로 글을 포스팅 하셨습니다. ")
    def delete_post(self):
        pass

    def lecture_info(self):
        pass




dongguktime=[]
object_index=0
def main():
    print("회원 가입 하기 >> 1\n로그인 하기 >> 2")
    while 1 :
        a=int(input())
        if a==1:
            name=input("성함을 입력해 주세요. >> ")
            id=input("ID 를 입력해 주세요.  >> ")
            pw=input("Password 를 입력해 주세요. >> ")
            dongguktime.append(DonggukTime([name,id,pw]))
            print()
            print("회원가입 완료!")
            print()
            print("회원 가입 하기 >> 1\n로그인 하기 >> 2")
        else:
            log_in_sign=False
            log_in_id=input("ID를 입력해 주세요 >> ")
            log_in_pw=input("Password를 입력해 주세요 >> ")
            print()
            for i in range(len(dongguktime)):
                if (log_in_id ==dongguktime[i].id) and (log_in_pw == dongguktime[i].pw):
                    log_in_sign=True
                    DonggukTime.user_index=i
                    break
            if log_in_sign:
                print("로그인 완료\n")
                break
            else:
                print("ID 혹은 Password를 다시 확인해 주세요")
                print()
                print("회원 가입 하기 >> 1\n로그인 하기 >> 2")



while 1:
    main() #로그인 하기
    user=dongguktime[DonggukTime.user_index] #로그인이 된 인스턴스
    while 1:
        if len(DonggukTime.df_timeline)==0:
            print("현재 게시물은 0 개 입니다.")
        user.show_timeline()
        a=int(input("< 작업 선택 >\n1. 타임라인 보기 --> 1\n2. 타임라인 작성 --> 2\n3. 타임라인 글 삭제 --> 3 "))
        if a==1:
            user.show_timeline()
        elif a==2:
            user.write_timeline()
        elif a==3:
            user.delete_post()
