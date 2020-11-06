#구분을 위해 줄바꿈을 구분으로 1,2,3,4, 번을 출력하였습니다.
f_name=open('D:/박병현/동국대학교/3학년 1학기/파이썬프로그래밍/박병현 파이썬/CH8과제/파이썬2_수강생_이름.txt','r')
f_major=open('D:/박병현/동국대학교/3학년 1학기/파이썬프로그래밍/박병현 파이썬/CH8과제/파이썬2_수강생_학과.txt','r')
f_HakBurn=open('D:/박병현/동국대학교/3학년 1학기/파이썬프로그래밍/박병현 파이썬/CH8과제/파이썬2_수강생_학번.txt','r')
s_name=f_name.readlines()
s_major=f_major.readlines()
s_HakBurn=f_HakBurn.readlines()
total_list=[(s_name[i].replace("\n",""),s_HakBurn[i].replace("\n",""),s_major[i].replace("\n","")) for i in range(len(s_name))]
total_dict={}
for i in range(len(s_name)):
    total_dict[s_name[i].replace("\n","")]=[s_HakBurn[i].replace("\n",""),s_major[i].replace("\n","")]
print(total_list)
print()
print(total_dict)
print()
fake_dict=sorted(total_dict.items())
sort_dict={}
for i in fake_dict:
    sort_dict[i[0]]=[i[1][0],i[1][1]]
print(sort_dict)
print()
HakBurn_sort=sorted(total_dict.items(),key=lambda item:item[1])
print("{}\t{}\t\t{}\t\t{}".format("No.","학번","이름","학과"))
for i in range(len(s_name)):
    if len(HakBurn_sort[i][0])==4:
        print("{}\t{}\t{}\t{}".format(i+1,HakBurn_sort[i][1][0],HakBurn_sort[i][0],HakBurn_sort[i][1][1]))
    else:
        print("{}\t{}\t{}\t\t{}".format(i+1,HakBurn_sort[i][1][0],HakBurn_sort[i][0],HakBurn_sort[i][1][1]))
f_HakBurn.close()
f_major.close()
f_HakBurn.close()
