a = float(input())
y = ((a*120)%3600)//60 #кол-во минут 
z = ((a*120)%3600)%60  #кол-во секунд
x = y*6 + z/10
print(x)
