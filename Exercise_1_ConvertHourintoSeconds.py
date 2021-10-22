hours = input("How many hours to you want to convert into seconds? ")
hours = int(hours)
seconds = hours*3600
print("{} hours are {} seconds!".format(hours, seconds))

print("Now with usage of a function")

def convert_hours (hrs):
	sec = hrs * 3600
	print(f"{hrs} are {sec}")


convert_hours(8)