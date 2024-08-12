import turtle
a=turtle.Turtle()
a.speed(0)
l=[]
z=[0,0,0]
y=[0,0,0]
g=a
def win():
    if ((z[0] in [1,2,3] and z[1] in [1,2,3] and z[2] in [1,2,3]) or (z[0] in [4,5,6] and z[1] in [4,5,6] and z[2] in [4,5,6]) or (z[0] in [7,8,9] and z[1] in [7,8,9] and z[2] in [7,8,9]) or (z[0] in [1,4,7] and z[1] in [1,4,7] and z[2] in [1,4,7]) or (z[0] in [2,5,8] and z[1] in [2,5,8] and z[2] in [2,5,8]) or (z[0] in [3,6,9] and z[1] in [3,6,9] and z[2] in [3,6,9]) or (z[0] in [1,5,9] and z[1] in [1,5,9] and z[2] in [1,5,9]) or (z[0] in [3,5,7] and z[1] in [3,5,7] and z[2] in [3,5,7])):
        print("player1 you are the winner")
        return 10
    if ((y[0] in [1,2,3] and y[1] in [1,2,3] and y[2] in [1,2,3]) or (y[0] in [4,5,6] and y[1] in [4,5,6] and y[2] in [4,5,6]) or (y[0] in [7,8,9] and y[1] in [7,8,9] and y[2] in [7,8,9]) or (y[0] in [1,4,7] and y[1] in [1,4,7] and y[2] in [1,4,7]) or (y[0] in [2,5,8] and y[1] in [2,5,8] and y[2] in [2,5,8]) or (y[0] in [3,6,9] and y[1] in [3,6,9] and y[2] in [3,6,9]) or (y[0] in [1,5,9] and y[1] in [1,5,9] and y[2] in [1,5,9]) or (y[0] in [3,5,7] and y[1] in [3,5,7] and y[2] in [3,5,7])):
        print("player2 you are the winner")
        return 10
def mov(m):
    if m not in l:
        if m==1:
            g.rt(135)
            g.fd(212)
            g.rt(45)
        elif m==2:
            g.rt(180)
            g.fd(150)
        elif m==3:
            g.lt(135)
            g.fd(212)
            g.lt(45)
        elif m==4:
            g.rt(90)
            g.fd(150)
            g.rt(90)
        elif m==5:
            g.rt(180)
        elif m==6:
            g.lt(90)
            g.fd(150)
            g.lt(90)
        elif m==7:
            g.rt(45)
            g.fd(212)
            g.lt(45)
        elif m==8:
            g.fd(150)
        elif m==9:
            g.lt(45)
            g.fd(212)
            g.rt(45)
        l.append(m)
    elif t!=7:
        print("wrong")
        m=int(input("enter ur ch: "))
        mov(m)
def doubt1(p,q):
    if (p==z[0]) and (q not in l):
        z[0]=q
        return 1
    elif (p==z[1]) and (q not in l):
        z[1]=q
        return 3
    elif (p==z[2]) and (q not in l):
        z[2]=q
        return 5
    else:
        print("enter proper ch1: ")
        r=int(input("enter ur pos1: "))
        s=int(input("where should it move: "))
        h=doubt1(r,s)
        print(h)
        return h
def doubt2(p,q):
    if (p==y[0]) and (q not in l):
        y[0]=q
        return 2
    elif (p==y[1]) and (q not in l):
        y[1]=q
        return 4
    elif (p==y[2]) and (q not in l):
        y[2]=q
        return 6
    else:
        print("enter proper ch2:")
        r=int(input("enter ur pos2: "))
        s=int(input("where should it move: "))
        h=doubt2(r,s)
        return h
def doubt(p,q): 
    if p in z:
        h=doubt1(p,q)
        return h
    elif p in y:
        h=doubt2(p,q)
        return h
    else:
        print("enter proper ch0:")
        r=int(input("player enter ur pos: "))
        s=int(input("where should it move: "))
        h=doubt(r,s)
        return h
            
def slide(p,q):
    if (p in l)and(q not in l):
        if p==1 and (q==2 or 4 or 5):
            if q==2:
                g.rt(90)
                g.fd(150)
                g.lt(90)
            elif q==5:
                g.rt(135)
                g.fd(212)
                g.lt(135)
            elif q==4:
                g.rt(180)
                g.fd(150)
                g.rt(180)
            l.append(q)
            l.remove(p)
        elif p==2 and (q==1 or 3 or 5):
            if q==1:
                g.lt(90)
                g.fd(150)
                g.rt(90)
            elif q==5:
                g.rt(180)
                g.fd(150)
                g.lt(180)
            elif q==3:
                g.rt(90)
                g.fd(150)
                g.lt(90)
            l.append(q)
            l.remove(p)
        elif p==3 and (q==6 or 2 or 5):
            if q==2:
                g.lt(90)
                g.fd(150)
                g.rt(90)
            elif q==5:
                g.lt(135)
                g.fd(212)
                g.rt(135)
            elif q==6:
                g.rt(180)
                g.fd(150)
                g.rt(180)
            l.append(q)
            l.remove(p)
        elif p==4 and (q==1 or 7 or 5):
            if q==1:
                g.fd(150)
            elif q==5:
                g.rt(90)
                g.fd(150)
                g.lt(90)
            elif q==7:
                g.rt(180)
                g.fd(150)
            l.append(q)
            l.remove(p)
        elif p==5 and q!=5:
            if q==1:
                g.lt(45)
                g.fd(212)
                g.rt(45)
            elif q==2:
                g.fd(150)
            elif q==3:
                g.rt(45)
                g.fd(212)
                g.lt(45)
            elif q==4:
                g.lt(90)
                g.fd(150)
                g.rt(90)
            elif q==6:
                g.rt(90)
                g.fd(150)
                g.lt(90)
            elif q==7:
                g.lt(135)
                g.fd(212)
                g.lt(45)
            elif q==8:
                g.rt(180)
                g.fd(150)
            elif q==9:
                g.rt(135)
                g.fd(212)
                g.rt(45)
            l.append(q)
            l.remove(p)
        elif p==6 and (q==9 or q==5 or q==3):
            if q==3:
                g.fd(150)
            elif q==5:
                g.lt(90)
                g.fd(150)
                g.rt(90)
            elif q==9:
                g.rt(180)
                g.fd(150)
            l.append(q)
            l.remove(p)
        elif p==7 and (q==8 or q==5 or q==4):
            if q==4:
                g.lt(180)
                g.fd(150)
            elif q==5:
                g.lt(135)
                g.fd(212)
                g.lt(45)
            elif q==8:
                g.lt(90)
                g.fd(150)
                g.rt(90)
            l.append(q)
            l.remove(p)
        elif p==8 and (q==7 or q==5 or q==9):
            if q==7:
                g.rt(90)
                g.fd(150)
                g.lt(90)
            elif q==5:
                g.lt(180)
                g.fd(150)
            elif q==9:
                g.lt(90)
                g.fd(150)
                g.rt(90)
            l.append(q)
            l.remove(p)
        elif p==9 and (q==8 or q==5 or q==6):
            if q==8:
                g.rt(90)
                g.fd(150)
                g.lt(90)
            elif q==5:
                g.lt(135)
                g.fd(212)
                g.rt(45)
            elif q==6:
                g.rt(180)
                g.fd(150)
            l.append(q)
            l.remove(p)
        else:
            print("enter proper choice: ")
            p=int(input("enter your pos"))
            q=int(input("where should it move"))
            slide(p,q)
    j=win()
    return j
a.up()
a.left(180)
a.fd(150)
a.lt(90)
a.fd(150)
a.lt(90)
a.fd(150)
a.down()
for i in range(4):
    a.left(90)
    a.fd(300)
a.left(135)
a.fd(425)
a.up()
a.rt(135)
a.fd(300)
a.down()
a.rt(135)
a.fd(425)
a.rt(135)
a.up()
a.fd(150)
a.rt(90)
a.down()
a.fd(300)
a.up()
a.rt(90)
a.fd(150)
a.rt(90)
a.fd(150)
a.rt(90)
a.down()
a.fd(300)
a.up()
a.lt(180)
a.fd(150)
a.hideturtle()
a.shape("turtle")
b=a.clone()
b.shape("triangle")
c=a.clone()
c.shape("turtle")
d=a.clone()
d.shape("triangle")
e=a.clone()
e.shape("turtle")
f=a.clone()
f.shape("triangle")
t=1
p=0
str1="player1"
str2="player2"
for i in range(6):
    if p==0:
        print(str1,"enter your pos: ",end=" ") 
        m=int(input())
        p=1
    else:
        print(str2,"enter your pos: ",end=" ") 
        m=int(input())
        p=0
    if t==1:
        g=a
        t=t+1
        z[0]=m
        mov(m)
    elif t==2:
        g=b
        t=t+1
        y[0]=m
        mov(m)
    elif t==3:
        g=c
        t=t+1
        z[1]=m
        mov(m)
    elif t==4:
        g=d
        t=t+1
        y[1]=m
        mov(m)
    elif t==5:
        g=e
        t=t+1
        z[2]=m
        g.showturtle()
        mov(m)
        j=win()
        if j==10:
            break
    elif t==6:
        g=f
        t=t+1
        y[2]=m
        g.showturtle()
        mov(m)
        j=win()
        if j==10:
            break
    g.showturtle()
t=0
if j!=10:
    for i in range(100): 
        if t==0:
            print(str1,"enter your pos: ",end=" ") 
            p=int(input())
            q=int(input("where should it move: "))
            t=1
        else:
            print(str2,"enter your pos: ",end=" ") 
            p=int(input())
            q=int(input("where should it move: "))
            t=0
        h=doubt(p,q)
        if h==1:
            g=a
        elif h==2:
            g=b
        elif h==3:
            g=c
        elif h==4:
            g=d
        elif h==5:
            g=e
        elif h==6:
            g=f
        j=slide(p,q)
        if j==10:
            break
