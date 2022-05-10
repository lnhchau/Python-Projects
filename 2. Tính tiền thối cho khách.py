#MÁY BÁN HÀNG TỰ ĐỘNG: Cân số kg nhân giá tiền -> tổng, khách đưa tiền thì thối bao nhiêu (bao nhiêu tờ 5K, 10K, 50K).
def calc_total_price(APPLE_PRICE, apple_weight):
	return APPLE_PRICE * apple_weight

def calc_return(total_price, money_given): 
	if money_given < total_price:
		return -1 
	return money_given - total_price

def print_return_info(total):
	count_500=int(total/500)
	total=total-count_500*500
	if count_500 !=0:
		print("500K: "+str(count_500))
	
	count_200=int(total/200)
	total=total-count_200*200
	if count_200 !=0:
		print("200K: "+str(count_200))
	
	count_100=int(total/100)
	total=total-count_100*100
	if count_100 !=0:
		print("100K: "+str(count_100))
	
	count_50=int(total/50)
	total=total-count_50*50
	if count_50 !=0:
		print("50K: "+str(count_50))
	
	count_20=int(total/20)
	total=total-count_20*20
	if count_20 !=0:
		print("20K: "+str(count_20))
	
	count_10=int(total/10)
	total=total-count_10*10
	if count_10 !=0:
		print("10K: "+str(count_10))
	
	count_5=int(total/5)
	total=total-count_5*5
	if count_5 !=0:
		print("5K: "+str(count_5))
	
	count_2=int(total/2)
	total=total-count_2*2
	if count_2 !=0:
		print("2K: "+str(count_2))
	
	count_1=int(total/1)
	total=total-count_1*1
	if count_1 !=0:
		print("1K: "+str(count_1))

def main():
	APPLE_PRICE=21
	apple_weight=input("Enter weight of apples: ")
	apple_weight=float(apple_weight)
	total_price = calc_total_price(APPLE_PRICE, apple_weight)
	print("Total price: "+str(total_price))

	money_given=input("Total money customer give you: ")
	money_given=float(money_given)
	money_return= calc_return(total_price, money_given)
	money_return=round(money_return,1)

	if money_return ==-1:
		enough_cash=total_price - money_given
		print("Sorry you give not enough money: "+str(enough_cash))
	else:
		print("You need to return to customer: "+str(money_return))
		print_return_info(money_return)
main()