#
# student_scores = {
#     "Zahid": 89,
#     "Namal": 56,
#     "Ali": 78,
#     "Umair": 90,
#     "Wahab": 80,
# }
#
# student_grades = {}
#
# for student in student_scores:
#     score = student_scores[student]
#
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     elif score > 60:
#         student_grades[student] = "Below Average"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)
#
#
# country = input("Add Country")   # Add country
# visits = int(input("Number of visits"))   # Add number of visits
# list_of_cities = eval(input())  # create list from formatted string
#
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lilly", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
# def add_new_country(name, times_visited, cities_visited):
#     new_country = {"country": name, "visits": times_visited, "cities": cities_visited}
#     travel_log.append(new_country)
#
# # Final Running
# add_new_country(country, visits, list_of_cities)
# print(f"I have been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
# print(f"My favorite citry was {travel_log[2]['cities'][0]}.")
#
# bidders_dict = {}
# other_user = True
#
# def ask_user():
#     name = input("What is your name: ")
#     bid_price = int(input("What is your bid price: "))
#     bidders_dict[name] = bid_price
#
# while other_user:
#     ask_user()
#     other_bidder = input("Is there any other bidder? yes or no: ")
#     if other_bidder == "yes":
#         other_user = True
#     elif other_bidder == "no":
#         other_user = False
#     else:
#         print("Only choose between yes or no!")
#
# # Initialize variables to find the highest bid and bidder
# h_bid = 0
# highest_bidder = ""
#
# # Iterate through the dictionary to find the highest bid
# for bidder, bid in bidders_dict.items():
#     if bid > h_bid:
#         h_bid = bid
#         highest_bidder = bidder
#
# print(bidders_dict)
# print(f"Highest Bid is: {h_bid} by {highest_bidder}")