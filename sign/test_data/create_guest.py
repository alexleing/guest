f = open("guest.txt", 'w')

for i in range(1, 1000):
    str_i = str(i)
    real_name = "alex" + str_i
    phone = 15900000000 + i
    email = "alex" + str_i + "@mail.com"
    sql = 'INSERT INTO sign_guest(real_name,phone,email,sign,event_id)values ' \
          '("'+real_name+'," '+str(phone)+ ',"'+email+'",0,1);'
    f.write(sql)
    f.write("\n")


f.close()