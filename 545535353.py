a= int(input("введіть число ")) #користувач вводить число
b=a//100 #знаходимо 1 цифру трьохзначного числа
c=a//10%10 #знаходимо 2 цифру числа
d=a%10 #знаходимо 3 цифру числа
print(b)
print(c)
print(d)
print(d*100+c*10+b)
