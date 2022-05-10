import datetime
def meter_to_feet(meter):
	FEET=3.281
	feet =FEET*meter
	round(feet,1)
	return feet
def age_person_info(year_born, CURRENT_YEAR):
	return CURRENT_YEAR- year_born
def ask_yes_no(prompt):
	yes_answer_list=["yes", "y", "YES", "Y"]
	no_answer_list=["no", "n", "NO", "N"]
	answer=input(prompt)
	while True:
		if answer in yes_answer_list:
			return True
		elif answer in no_answer_list:
			return False
		else:
			continue
def print_height_info(height_feet, last_name, is_male):
	if is_male==True:
		if height_feet>6.5:
			i=0
			print(last_name+"'s", end=" ")
			while i<=10:
				i+=1
				print("very", end=" ")
			print("tall as a man")
		elif height_feet>6.0:
			print(last_name+"'s tall as a man")
		else:
			print(last_name+"'s short as a man")

	elif is_male==False:
		if height_feet>6.0:
			print(last_name+"'s", end=" ")
			for i in range(10):
				print("very", end=" ")
			print("tall as a woman")
		elif height_feet>5.7:
			print(last_name+"'s tall as a woman")
		else:
			print(last_name+"'s short as a woman")
def input_person_info():
	first_name=input("What's your first_name: ")
	last_name=input("What's your last_name: ")
	year_born=int(input("When you were born: "))
	height_meter=float(input("Your height (meter): "))
	is_male=ask_yes_no("Are you male (yes/no): ")
	is_vietnamese=ask_yes_no("Are you Vietnamese (yes/no): ")
	return first_name, last_name, year_born, height_meter, is_male, is_vietnamese
def print_person_info(first_name, last_name, age, height_feet, is_male, is_vietnamese,CURRENT_YEAR):
	print("Your name is "+first_name+" "+last_name)
	print("{0}'s {1} years old in {2}".format(last_name, age, CURRENT_YEAR))
	print(last_name+" 's "+str(height_feet)+" feet tall")
	if True:
		print("You're from Vietnam")
	else:
		print("You're not from Vietnam")
	print_height_info(height_feet, last_name, is_male)
def main():
	now=datetime.datetime.now()
	CURRENT_YEAR=now.year
	first_name, last_name, year_born, height_meter, is_male, is_vietnamese = input_person_info()
	age = age_person_info(year_born, CURRENT_YEAR)
	height_feet = meter_to_feet(height_meter)
	print_person_info(first_name, last_name, age, height_feet, is_male, is_vietnamese,CURRENT_YEAR)
main()