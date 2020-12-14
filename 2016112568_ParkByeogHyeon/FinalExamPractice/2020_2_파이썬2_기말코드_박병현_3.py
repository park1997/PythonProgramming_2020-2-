import csv
f = open("korea_floating_population_data.csv", 'r')
s = csv.reader(f)
jongro_20num,jongro_50num,dobong_20num,dobong_50num,jongro_all,dobong_all=0,0,0,0,0,0
for i in s:
    if "종로구" in i[7]:
        jongro_20num+=int(i[10])+int(i[15])
        jongro_50num+=int(i[13])+int(i[18])
        jongro_all+=sum(map(int,i[9:]))
    if "도봉구" in i[7]:
        dobong_20num+=int(i[10])+int(i[15])
        dobong_50num+=int(i[13])+int(i[18])
        dobong_all+=sum(map(int,i[9:]))
print("{}".format("*"*80))
print("{:6} {:6} {:6} {:6} {:6} {:6}".format("조사지역","전체수","20대","20대비율","50대","50대비율"))
print("{:10} {:10} {:8} {:8} {:8} {:6}".format("Area","Total","No.","Rate%","No.","Rate%"))
print("{}".format("*"*80))
print("{:6} {:7}  {:6} {:9}  {:6} {:9}".format("종로구",jongro_all,jongro_20num,round(jongro_20num*100/jongro_all,3),jongro_50num,round(jongro_50num*100/jongro_all,3)))
print("{:6} {:7}  {:6} {:9}  {:6} {:9}".format("도봉구",dobong_all,dobong_20num,round(dobong_20num*100/dobong_all,3),dobong_50num,round(dobong_50num*100/dobong_all,3)))
print("{}".format("-"*80))
