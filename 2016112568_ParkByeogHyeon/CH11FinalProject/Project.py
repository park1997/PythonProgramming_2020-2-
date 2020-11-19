import time
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import requests


class DonggukTime:
    """
    DonggukTime class(For Engineers)
    Author : Park ByeongHyeon
    Date : 2020-11-18
    """
    #클래스 인스턴스 순서 저장 하기위해
    user_index=0
    #df전역변수로 설정
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

    def standing_mc_the_max(self):
        #모든 엑셀 파일들의 데이터를 불러온다.
        ise_df = pd.read_excel("산시선이수.xlsx")
        cee_df = pd.read_excel("건설환경공학선이수.xlsx")
        mre_df = pd.read_excel("기계공학선이수.xlsx")
        mme_df = pd.read_excel("멀티미디어선이수.xlsx")
        ice_df = pd.read_excel("정보통신공학선이수.xlsx")
        cse_df = pd.read_excel("컴퓨터공학선이수.xlsx")
        cbe_df = pd.read_excel("화생공선이수.xlsx")
        eee_df = pd.read_excel("전자전기공학선이수.xlsx")
        gunchuk_df = pd.read_excel("건축공학선이수.xlsx")
        architec_df = pd.read_excel("건축학선이수.xlsx")
        newmeterial_df = pd.read_excel("융에신선이수.xlsx")
        #불러온 데이터를 모두 이 딕셔너리에 넣는다
        df_dic={}
        k=0
        for i in ise_df['후수교과목']:
            df_dic[i]=ise_df['선수교과목'][k]
            k+=1
        k=0
        for i in cee_df['후수교과목']:
            df_dic[i]=cee_df['선수교과목'][k]
            k+=1
        k=0
        for i in mre_df['후수교과목']:
            df_dic[i]=mre_df['선수교과목'][k]
            k+=1
        k=0
        for i in mme_df['후수교과목']:
            df_dic[i]=mme_df['선수교과목'][k]
            k+=1
        k=0
        for i in ice_df['후수교과목']:
            df_dic[i]=ice_df['선수교과목'][k]
            k+=1
        k=0
        for i in cse_df['후수교과목']:
            df_dic[i]=cse_df['선수교과목'][k]
            k+=1
        k=0
        for i in cbe_df['후수교과목']:
            df_dic[i]=cbe_df['선수교과목'][k]
            k+=1
        k=0
        for i in eee_df['후수교과목']:
            df_dic[i]=eee_df['선수교과목'][k]
            k+=1
        k=0
        for i in gunchuk_df['후수교과목']:
            df_dic[i]=gunchuk_df['선수교과목'][k]
            k+=1
        k=0
        for i in architec_df['후수교과목']:
            df_dic[i]=architec_df['선수교과목'][k]
            k+=1
        k=0
        for i in newmeterial_df['후수교과목']:
            df_dic[i]=newmeterial_df['선수교과목'][k]
            k+=1
        lec_name=input(" 과목명을 입력 하세요  >>  ")
        #혹시 사용자 실수로 띄어쓰기 했을경우 고려.
        lec_name=''.join(lec_name.split())
        if lec_name in df_dic:
            result=df_dic[lec_name]
            print("\"{}\"의 선 이수 과목은 {} 입니다. ".format(lec_name,result))
        else:
            print("\"{}\"은 선이수 과목이 없습니다. ".format(lec_name))


    def log_out(self):
        pass



#인스턴스들의 집합소
dongguktime=[]
def main():
    print("회원 가입 하기 >> 1\n로그인 하기 >> 2")
    while 1 :
        a=int(input())
        if a==1:
            name=input("성함을 입력해 주세요. >> ")
            id=input("ID 를 입력해 주세요.  >> ")
            pw=input("Password 를 입력해 주세요. >> ")
            #리스트에 객체 저장
            dongguktime.append(DonggukTime([name,id,pw]))
            print()
            print("회원가입 완료!")
            print()
            print("회원 가입 하기 >> 1\n로그인 하기 >> 2")
        else:
            #Boolean형태로 로그인이 되면 True로 바뀌게
            log_in_sign=False
            log_in_id=input("ID를 입력해 주세요 >> ")
            log_in_pw=input("Password를 입력해 주세요 >> ")
            print()
            for i in range(len(dongguktime)):
                if (log_in_id ==dongguktime[i].id) and (log_in_pw == dongguktime[i].pw):
                    #로그인이 된 상태
                    log_in_sign=True
                    DonggukTime.user_index=i
                    break
            if log_in_sign:
                print("로그인 완료\n")
                break
            else:
                #로그인 실패
                print("ID 혹은 Password를 다시 확인해 주세요")
                print()
                print("회원 가입 하기 >> 1\n로그인 하기 >> 2")



while 1:
    main() #로그인 하기
    user=dongguktime[DonggukTime.user_index] #로그인이 된 인스턴스
    user.show_timeline()
    while 1:
        if len(DonggukTime.df_timeline)==0:
            print("현재 게시물은 0 개 입니다.")
        a=int(input("< 작업 선택 >\n1. 타임라인 보기 --> 1\n2. 타임라인 작성 --> 2\n3. 타임라인 글 삭제 --> 3\n4. 선 이수과목 조회 --> 4"))
        if a==1:
            #타임라인 보기
            user.show_timeline()
        elif a==2:
            #타밈라인 글 쓰기
            user.write_timeline()
        elif a==3:
            #글 삭제
            user.delete_post()
        elif a==4:
            #선이수과목조회
            user.standing_mc_the_max()
