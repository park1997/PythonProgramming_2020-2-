import time
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import requests


class DonggukTime:
    """
    DonggukTime class(For Engineers)
    Author : Park ByeongHyeon
    Date : 2020-11-20
    """
    #클래스 인스턴스 순서 저장 하기위해
    user_index=0
    #로그인할때 이미 저장된 아이디인지 확인하기위해 아이디만 리스트에 전역 변수로 저장
    ID_list=[]
    #타임라인 게시판 글 목록 클래스변수에 저장
    head_name_list=[]
    #가입된 회원의 정보들(이름과 아이디)
    member_in_this_system=[]
    #df전역변수로 설정
    df_timeline=pd.read_excel("timeline.xlsx")
    #__init__
    def __init__(self,details):
        self.name=details[0]
        self.id=details[1]
        self.pw=details[2]
        self.birth=details[3]
        #작성글 정보 저장
        self.post_info=[]
        #개인 프로필 상태 저장
        self.profile_info=[]
        print(self.name, self.id, self.pw,self.birth)
    #로그인 하기
    def log_in(self):
        main()
    #타입라인 보여주기
    def show_timeline(self):
        if len(DonggukTime.df_timeline)==0:
            print("현재 타임라인에 글이 없습니다.")
        for i in range(len(DonggukTime.df_timeline)):
            name,time,context,likes_num,grade,lecture_name,head_name,comment=DonggukTime.df_timeline.loc[i]
            print("{} 번째 강의 평 : {}".format(i+1,head_name))
            print("{}".format("-"*50))
            print("작성자 : {}\n작성 시간: {}".format(name,time))
            print("{}".format("-"*50))
            print("과목 명 : {}\n강의 평점 : {}".format(lecture_name,grade))
            print("{}".format("-"*50))
            print("강의 평 내용\n")
            print(context)
            print("{}".format("="*50))
            print("댓글\n")
            print("{}".format(comment))
            print()
            print()
    #타임라인 작성하기
    def write_timeline(self):
        post_head_name=input("글 제목을 입력 하세요.  >>")
        post_context=input("글 내용을 입력 하세요.  >>")
        post_lecture=input("강의 이름을 입력 하세요.  >>")
        while 1:
            try:
                post_grade=float(input("강의 평점을 0점 이상 10점 이하로 입력해 주세요. >>"))
                if post_grade>10:
                    print("점수 범위를 초과 하셨습니다. 10점 이하로 입력해 주세요.  >>")
                elif post_grade<0:
                    print("점수를 양수로 입력해 주세요.  >>")
                else:
                    break
            except :
                #강의 평점을 문자로 입력한경우!
                print("숫자로 입력해 주세요!")
        now=time.localtime()
        post_now_time="%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)

        #나중에 글 삭제를 위해 정보 저장
        self.post_info.append([post_head_name,post_lecture,post_context])
        #댓글 혹은 좋아요 하기위해 글 제목 저장
        DonggukTime.head_name_list.append([post_head_name,post_context])
        print("성공적으로 글을 포스팅 하셨습니다. ")
        print()
        DonggukTime.df_timeline=DonggukTime.df_timeline.append({"작성자":self.name,"작성시간":post_now_time,"글내용":post_context,"좋아요수":0,"평점":post_grade,"과목명":post_lecture,"글제목":post_head_name,"댓글":""},ignore_index=True)
        #바뀐 DataFrame을 excel에 저장
        DonggukTime.df_timeline.to_excel("timeline.xlsx",index=False)
    #내가 쓴 글 삭제하기
    def delete_post(self):
        dic_for_delete={}
        for i,j in enumerate(DonggukTime.head_name_list):
            dic_for_delete[i+1]=j
            print("{} - {}".format(i+1,j[0]))
        post_num=int(input("삭제할 본인의 게시물 번호를 입력해 주세요.  >>"))

        #DataFrame에 삭제할 index 계산(글제목과 내용이 같은 사람이 썼을 경우,본인이 썼을 경우)
        index_num_delete=DonggukTime.df_timeline[(DonggukTime.df_timeline["작성자"]==self.name) & (DonggukTime.df_timeline["글제목"]==dic_for_delete[post_num][0]) & (DonggukTime.df_timeline["글내용"]==dic_for_delete[post_num][1])].index
        #DataFrame에 해당 행 삭제
        DonggukTime.df_timeline.drop(index_num_delete,inplace=True)
        #실제엑셀파일에 저장
        DonggukTime.df_timeline.to_excel("timeline.xlsx",index=False)
        print("정상적으로 삭제 되었습니다.")
    #선이수 관계 보여주기
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
            print("\"{}\"의 선 이수 과목은 \"{}\" 입니다. ".format(lec_name,result))
        else:
            print("\"{}\"은 선이수 과목이 없습니다. ".format(lec_name))
    #ID변경
    def edit_profile_id(self):
        while 1:
            first_id_input=input("변경할 ID를 입력해 주세요.  >>")
            second_id_input=input("ID를 다시 한번 입력해 주세요 .  >>\n")
            if first_id_input==second_id_input:
                break
            else:
                print("아이디가 일치 하지 않습니다. 변경할 ID를 다시 입력해 주세요.")
                print()
        self.id=first_id_input
        print("ID 변경에 성공 하셨습니다.\n")
    #PW변경
    def edit_profile_pw(self):
        while 1:
            first_pw_input=input("변경할 Password를 입력해 주세요. >>")
            second_pw_input=input("Password를 다시 한번 입력해 주세요. >>\n")
            if first_pw_input==second_pw_input:
                break
            else:
                print("Password가 일치 하지 않습니다. 변경할 Password를 다시 입력해 주세요.")
                print()
        self.pw=first_pw_input
        print("Password 변경에 성공 하셨습니다.\n")
    #댓글 작성
    def write_comment(self):
        for i,j in enumerate(DonggukTime.df_timeline["글제목"]):
            print("{} - {}".format(i+1,j))
        post_num=int(input("댓글을 달 게시물의 번호를 입력해 주세요.  >>"))
        post_comment=input("댓글을 입력해 주세요. >>")
        #판다스의 경고문을 무시함
        pd.options.mode.chained_assignment = None
        #댓글추가
        temp=DonggukTime.df_timeline["댓글"][post_num-1]
        now=time.localtime()
        commenttime_now_time="%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
        temp+="\n{} : {}\t\t{}".format(self.name,post_comment,commenttime_now_time)
        DonggukTime.df_timeline["댓글"][post_num-1]=temp
        #Unnamed열 생성 억제
        DonggukTime.df_timeline.to_excel("timeline.xlsx",index=False)
        print("댓글 입력 완료!")
    #좋아요 누르기
    def like(self):
        pass

        
#pd.set_option("mode.chained_assignment",None)
#인스턴스들의 집합소
dongguktime=[]
#로그인 함수
def main():
    print("회원 가입 하기 >> 1\n로그인 하기 >> 2\n")
    while 1 :
        a=int(input())
        if a==1:
            name=input("성함을 입력해 주세요. >>")
            while 1:
                try:
                    birth=int(input("주민번호 앞 6자리(생년월일)를 입력해 주세요. >>"))
                    #6자리로 입력하지 않은 경우!
                    if len(str(birth))!=6:
                        print("띄어쓰기 없이 6자리로 입력해주세요!")
                    else:
                        break
                except :
                    #주민번호를 숫자가아니라 문자열로 입력한 경우
                    print("숫자를 입력해주세요!")
            #중복되는 아이디가 없게 한다.
            while 1:
                id=input("ID 를 입력해 주세요.  >>")
                if id not in DonggukTime.ID_list:
                    break
                else:
                    print("이미 존재하는 ID 입니다.\n새로운 ID를 입력해 주세요.")
            pw=input("Password 를 입력해 주세요. >>")
            #리스트에 객체 저장
            dongguktime.append(DonggukTime([name,id,pw,birth]))
            print()
            print("회원가입 완료!")
            DonggukTime.ID_list.append(id)
            print()
            print("회원 가입 하기 >> 1\n로그인 하기 >> 2\n")
        elif a==2:
            #Boolean형태로 로그인이 되면 True로 바뀌게
            log_in_sign=False
            log_in_id=input("ID를 입력해 주세요 >>")
            log_in_pw=input("Password를 입력해 주세요 >>")
            print()
            for i in range(len(dongguktime)):
                if (log_in_id ==dongguktime[i].id) and (log_in_pw == dongguktime[i].pw):
                    #로그인이 된 상태
                    log_in_sign=True
                    #로그인한 객체의 리스트 index를 클래스 변수에 저장한다.
                    DonggukTime.user_index=i
                    break
            if log_in_sign:
                print("로그인 완료\n")
                break
            else:
                #로그인 실패(객체에 저장된 아이디와 비번이 틀린경우)
                print("ID 혹은 Password를 다시 확인해 주세요")
                print()
                print("회원 가입 하기 >> 1\n로그인 하기 >> 2\n")
        else:
            #1,2번중 하나를 입력하지 않은 경우!
            print("1번 혹은 2번만 입력해 주세요!")



while 1:
    main() #로그인 하기
    user=dongguktime[DonggukTime.user_index] #로그인이 된 인스턴스
    user.show_timeline()
    print()
    while 1:
        a=int(input("<< 작업 선택 >>\n\n1. 타임라인 보기 --> 1\n2. 타임라인 작성 --> 2\n3. 타임라인 글 삭제 --> 3\n4. 아이디 변경 --> 4\n5. 비밀번호 변경 --> 5\n6. 댓글 달기 --> 6\n7. 좋아요 누르기 --> 7\n9. 선 이수과목 조회 --> 9\n0. 로그아웃 --> 0\n"))
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
            #아이디 변경
            user.edit_profile_id()
        elif a==5:
            #password변경
            user.edit_profile_pw()
        elif a==6:
            user.write_comment()
        elif a==7:
            pass
        elif a==8:
            pass
        elif a==9:
            #선이수과목조회
            user.standing_mc_the_max()
        elif a==0:
            #로그인 창으로 가게 만듬
            break
