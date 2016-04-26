#  extension to main
#
#  in order to do several tries and save the best maps


# list to hold the best of the best and corresponding value
the_best = []
best_value = 0

# sum all total values
sum_of_total_values = 0

# loop over code
for session in range(50):
	
	#####################
	# main.py code here #
	#####################
	
	# initiate the best list and update in later sessions
	if (session == 0 or total_value > best_value):
		the_best = houses
		best_value = total_value
	
	# update sum of total values variable
	sum_of_total_values =+ total_value
		
# calculate mean value of total
mean_value = sum_of_total_values / 50
