#password1 = input("最多輸入3次密碼: ")
password = 'a123456'
times = 3
while times > 0 :
	pwd = input("請輸入密碼: ")
	if password != pwd :
		times = times - 1
		if times == 0:
			print("對不起你沒機會了,再見")
			break
		print("密碼錯誤! 還有" ,times , "次機會")

		#times = times - 1
		
	elif password == pwd :
		print("登入成功!")
		break

