This program saves contacts information including (username, phone number, address, email) in csv file.
It generates new file daily including the date in the name of the file.

It includes four functions:

	
	1) contact_info : This function reads contacts information from user and validate them
			  then send them to the writer function.
			  It makes sure that the username and email do not already exists.
			  It validate the email address.	
			  It checks that the phone number consists of only 10 digits.
			  It calls writer function to save the contact information in the csv file.


	2) writer :	 This function includes two options
			 	first option = write : it checks first if the file already exists or not,
				if it does not exist then it writes name of cloumns and rows in the file.
				but if the file alresy exists then it only enter the value of rows.

				second option = update : it updates the existed contacts information according
				to user choices after being called by update function.


	3) update : 	This function shows the user the name of columns he can chooser from then asks him after
			showing all contests to choose the number of the row he wants to update.
			After that it shows the updated contact.


	4) delete : 	This functions deletes existed contact acorrding to the email address if it exists.
	

	5) Finally the program shows the user all diffrent options and calls the functions according to the
	   user choice. 
