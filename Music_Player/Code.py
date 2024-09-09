from tkinter import*
import turtle
import playsound

root=Tk()
root.title("애니 주제가 플레이어")
root.geometry("300x200")

num=[10,20,30,40,50,60,70,80,90,100,200,300,400,500]

def play0(x,y):
    playsound.playsound("Thomas.mp3")

def play1(x,y):
    playsound.playsound("Sinbi.mp3")


#토마스

def 토마스():
    import turtle
    scr=turtle.Screen()
    scr.clear()
    t=turtle.Turtle()
    scr.bgcolor("lightblue")
    t.speed(5)
    
    #몸체 1
    t.up()
    t.pencolor("black")
    t.goto(-240,200)
    t.down()
    t.fillcolor("dodgerblue")
    t.begin_fill()
    t.forward(470)
    t.right(num[8])
    t.forward(num[12])
    t.right(num[8])
    t.forward(470)
    t.right(num[8])
    t.forward(num[12])
    t.end_fill()

    #몸체 2
    t.up()
    t.pencolor("black")
    t.goto(-255,100)
    t.down()
    t.fillcolor("dodgerblue")
    t.begin_fill()
    t.right(num[8])
    t.forward(num[13])
    t.right(num[8])
    t.forward(num[11])
    t.right(num[8])
    t.forward(num[13])
    t.right(num[8])
    t.forward(num[11])
    t.end_fill()

    #원상태로
    t.up()
    t.home()

    #머리 위 1
    t.pencolor("black")
    t.goto(-45,250)
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(num[8])
    t.right(num[8])
    t.forward(num[9])
    t.right(num[8])
    t.forward(num[8])
    t.right(num[8])
    t.forward(num[9])
    t.end_fill()

    #머리 위 2
    t.up()
    t.goto(-50,240)
    t.right(num[8])
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(num[9])
    t.right(num[8])
    t.forward(num[2])
    t.right(num[8])
    t.forward(num[9])
    t.right(num[8])
    t.forward(num[2])
    t.end_fill()

    #얼굴
    t.up()
    t.pencolor("black")
    t.goto(80,-130)
    t.right(num[5])
    t.down()
    t.fillcolor("lightgray")
    t.begin_fill()
    t.circle(160)
    t.end_fill()

    #왼쪽 눈
    t.up()
    t.goto(-30,40)
    t.left(num[5])
    t.pencolor("black")
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(num[4])
    t.end_fill()

    #왼쪽 눈알
    t.up()
    t.goto(-50,40)
    t.down()
    t.color("black")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    #왼쪽 눈알(빛)
    t.up()
    t.goto(-42,60)
    t.color("white")
    t.begin_fill()
    t.circle(num[0])
    t.end_fill()

    #오른쪽 눈
    t.up()
    t.goto(95,83)
    t.left(num[5])
    t.pencolor("black")
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(num[4])
    t.end_fill()

    #오른쪽 눈알
    t.up()
    t.goto(85,65)
    t.down()
    t.color("black")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    #오른쪽 눈알(빛)
    t.up()
    t.goto(95,75)
    t.color("white")
    t.begin_fill()
    t.circle(num[0])
    t.end_fill()

    #코
    t.up()
    t.goto(-40,5)
    t.left(90)
    t.down()
    t.color("black")
    t.circle(num[3],240)

    #팔자주름(왼쪽)
    t.up()
    t.goto(-92,-80)
    t.right(95)
    t.down()
    t.circle(num[9],43)

    #팔자주름(오른쪽)
    t.up()
    t.goto(33,-25)
    t.right(140)
    t.down()
    t.circle(num[9],45)

    #입
    t.up()
    t.goto(-65,-65)
    t.down()
    t.circle(150,num[4])

    #몸체 3
    t.up()
    t.goto(190,130)
    t.pencolor("black")
    t.fillcolor("yellow")
    t.down()
    t.begin_fill()
    t.circle(num[2])
    t.end_fill()

    #몸체 4
    t.up()
    t.goto(187,138)
    t.color("black")
    t.down()
    t.begin_fill()
    t.circle(num[1])
    t.end_fill()

    #토마스와 친구들 글씨
    t.up()
    t.goto(-240,-250)
    t.down()
    t.pencolor("royalblue")
    t.write("토마스와 친구들",font=('나눔고딕',50,'normal'))

    #주제가
    scr.onscreenclick(play0)
    t.up()
    t.goto(-55,-260)
    t.down()
    t.pencolor("red")
    t.write("*주의: 노래가 끝나기 전까지 화면 클릭 금지", font=('나눔고딕',10,'normal'))
    t.up()
    t.goto(-190,-260)
    t.pencolor("black")
    t.write("화면을 클릭해보세요 :)",font=('나눔고딕',10,'normal'))
    t.hideturtle()




#신비
def 신비():
    import turtle
    scr=turtle.Screen()
    scr.clear()
    t=turtle.Turtle()
    scr.bgcolor("lemonchiffon")
    t.speed(5)
    

    #왼쪽 뿔
    t.up()
    t.goto(-20,214)
    t.left(num[5])
    t.down()
    t.fillcolor("lawngreen")
    t.begin_fill()
    t.circle(13,360,3)
    t.end_fill()

    #오른쪽 뿔
    t.up()
    t.goto(35,215)
    t.down()
    t.fillcolor("lawngreen")
    t.begin_fill()
    t.circle(13,360,3)
    t.end_fill()

    #얼굴
    t.up()
    t.goto(0,-100)
    t.right(60)
    t.down()
    t.fillcolor("lawngreen")
    t.begin_fill()
    t.circle(160)
    t.end_fill()

    #오른쪽 눈
    t.up()
    t.goto(70,50)
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(num[5])
    t.end_fill()

    #오른쪽 눈알
    t.up()
    t.goto(70,75)
    t.down()
    t.color("black")
    t.begin_fill()
    t.circle(num[3])
    t.end_fill()

    #오른쪽 눈알(빛)
    t.up()
    t.goto(80,115)
    t.right(60)
    t.down()
    t.color("yellow")
    t.begin_fill()
    t.circle(num[1],360,3)
    t.end_fill()

    #왼쪽 눈
    t.up()
    t.goto(-65,50)
    t.left(num[5])
    t.pencolor("black")
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(num[5])
    t.end_fill()

    #왼쪽 눈알
    t.up()
    t.goto(-60,75)
    t.down()
    t.color("black")
    t.begin_fill()
    t.circle(num[3])
    t.end_fill()

    #왼쪽 눈알(빛)
    t.up()
    t.goto(-50,115)
    t.right(num[5])
    t.down()
    t.color("yellow")
    t.begin_fill()
    t.circle(num[1],360,3)
    t.end_fill()

    #코
    t.up()
    t.goto(-5,40)
    t.down()
    t.color("black")
    t.left(105)
    t.forward(num[0])
    t.right(85)
    t.forward(12)

    #입(일자)
    t.up()
    t.pencolor("black")
    t.goto(-18,20)
    t.down()
    t.left(num[3])
    t.forward(num[3])

    #입(아래)
    t.up()
    t.goto(-18,20)
    t.down()
    t.fillcolor("salmon")
    t.begin_fill()
    t.right(num[8])
    t.circle(num[1],180)
    t.end_fill()

    #혀
    t.up()
    t.goto(10,-1)
    t.right(num[2])
    t.down()
    t.color("pink")
    t.begin_fill()
    t.circle(num[0],240)
    t.end_fill()

    #왼쪽 귀
    t.up()
    t.pencolor("black")
    t.goto(-155,100)
    t.right(120)
    t.down()
    t.fillcolor("lawngreen")
    t.begin_fill()
    t.circle(num[2],180)
    t.end_fill()

    #오른쪽 귀
    t.up()
    t.left(10)
    t.goto(160,50)
    t.down()
    t.fillcolor("lawngreen")
    t.begin_fill()
    t.circle(num[2],180)
    t.end_fill()

    #신비아파트 글씨
    t.up()
    t.goto(-150,-200)
    t.down()
    t.pencolor("royalblue")
    t.write("신비아파트",font=('나눔고딕',50,'normal'))

    #주제가
    scr.onscreenclick(play1)
    t.up()
    t.goto(-50,-260)
    t.down()
    t.pencolor("red")
    t.write("*주의: 노래가 끝나기 전까지 화면 클릭 금지", font=('나눔고딕',10,'normal'))
    t.up()
    t.goto(-185,-260)
    t.pencolor("black")
    t.write("화면을 클릭해보세요 :)",font=('나눔고딕',10,'normal'))
    t.hideturtle()



#시작 위젯

photo1=PhotoImage(file="토마스.gif")
photo2=PhotoImage(file="신비.gif")

b1=Label(root, text= "애니매이션 주제가")
b2=Button(root, text = "토마스", command=토마스)
b3=Button(root, text = "신비", command=신비)
b4=Label(root, text="", image=photo1)
b5=Label(root, text="", image=photo2)

b1.place(x=10, y=10)
b2.place(x=25, y=35, width = 90, height =40)
b3.place(x=165, y=35, width = 90, height =40)
b4.place(x=20, y=80)
b5.place(x=160, y=80)

root.mainloop()
