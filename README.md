# flaskSessionDebugErrors

# 1. CLONE this project into your machine
# 2. ACTIVATE your virtual environment, if it isn't already
# 3. RUN the project
# 4. READ the error messages
# 5. FIX as many of the bugs as you can. There are 7 bugs.
# 6. Have it checked!


# FOR INSTRUCTOR:

#Note: Ask them to troubleshoot on their own and remind to print which route they’re in and print request.form etc. to see what’s happening.

## BEGINNING ##
1. Error: “Method Not Allowed”
	Correction:
	index.html; line 19: method = post

2. Error: “Key Error”
	Correction:
	server.py; line 35: key errors in request.form

3. Error: “Key Error”
	Correction: 
	in both:
	server.py, line 41
	leaderboard.html, line 46
	method for both should be post

## INTERMEDIATE ##
4. Error: “Unexpected argument ‘first’ ”
	Correction:
	Don’t pass in variables to redirect method

5. Logic Problem: How to show ranks on leaderboard
	Solution: Use session in both
	changeRanks() in server.py, and
	leaderboard.html

## ADVANCED ##
6. Logic problem: Show page only shows 3rd place name
	Solution: rank variable is a string, 
	must cast as int or test against a string instead.

7. Logic Problem: Clicking show before assigning ranks throws error
	Solution: Various. Can handle in different ways