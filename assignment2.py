# Assignment 2 – Movie Ticket Booking

# Build a complete movie ticket booking program using functions for every operation: listing available shows, booking seats, calculating the total price (including any applicable discounts), and cancelling a booking.
# Requirements:
# •	Write a function list_shows() that displays available movies, show timings, and ticket prices using a list/dictionary of show data. 
# •	Write a function book_tickets(show_name, number_of_tickets, *seat_numbers) that uses variable-length arguments (*args) to accept any number of seat numbers. 
# •	Write a function calculate_total(price, quantity, discount=0) using a default argument for optional discounts. Apply the following payment-based pricing: 
# 	               - GPay : Add ₹30 convenience fee. 
# 	               - Credit Card : Apply 30% discount. 
# 	               - Cash : Use the normal ticket price of ₹230 per ticket. 
# •	Write a recursive function to calculate the total bill when a loyalty combo offer applies cumulative discounts for every 2 tickets booked. 
# •	Write a cancel_booking() function that reverses a booking and issues a refund amount using the same pricing function. 
# •	Tie all functions together in a menu-driven program that lets the user book, view, and cancel tickets.

show_name=""
number_of_tickets=0
seat_numbers=[]
total_amt=0
price=230

def list_shows():
    print("\n----MOVIE TICKET BOOKING----")
    movies_timings={"BKU":"10 AM","Jigra":"11 PM","Alpha":"2 PM","Lokah":"4 PM","Lucky Bhaskar":"9 PM"}
    print("Available movies and timings:")
    for k,v in movies_timings.items():
        print(f"-{k} : {v}")
    print("Ticket price: Rs.230 per ticket")
    show_name=input("Enter the movie name:")
    while show_name not in movies_timings:
        print("Invalid movie name")
        show_name=input("Enter the movie name:")
    number_of_tickets=int(input("Enter the number of tickets required:"))
    seat_numbers=[]
    print("Choose seat numbers:")
    for i in range(number_of_tickets):
        s=input()
        seat_numbers.append(s)
    return show_name,number_of_tickets,seat_numbers
# list_shows()


def book_tickets(show_name, number_of_tickets, *seat_numbers):
    if show_name=="":
        print("No movie ticket has been booked yet")
    else:
        print("\n----TICKET DETAILS----")
        print("Show name:",show_name)
        print("Number of tickets:",number_of_tickets)
        print("Seats booked:",seat_numbers)
       
        price=230
        total_amt=number_of_tickets*price
        return total_amt,price
    # return show_name,number_of_tickets,seat_numbers
# book_tickets("Lokah",4,10,11,12,13)

def loyalty_combo_offer(total_amt,number_of_tickets):
    if number_of_tickets<2:
        return total_amt
    total_amt-=230*2*(0.1)
    return loyalty_combo_offer(total_amt,number_of_tickets-2)


    

def calculate_total(total_amt,price, number_of_tickets, discount=30):
    pay_method=input("Enter your payment method:")
    # nonlocal amt
    
    if pay_method=="Gpay":
        print("Convenience fee:30")
        total_amt=total_amt+30
    elif pay_method=="Credit card":
        print("30 % discount applied")
        total_amt-=total_amt*(discount/100)
    elif pay_method=="Cash":
        total_amt=total_amt
    return total_amt,pay_method
# calculate_total(total_amt,230, 4, discount=0)


def cancel_booking(price,total_amt):
    if show_name=="":
        print("No movie ticket has been booked yet")
    else:
        # movie=input("Enter the name of the movie:")
        cancel_tickets=int(input("Number of tickets to be cancelled:"))
        print(f"{cancel_tickets} tickets cancelled for the movie {show_name}")
        refund=(total_amt/number_of_tickets)*cancel_tickets
        print("Refund amount:",refund)
        return cancel_tickets

while 1:
    print("\n1.Book movie ticket")
    print("2.View the ticket")
    print("3.Cancel ticket")
    print("4.Exit")
    ch=int(input("Choose an option:"))
    if ch==1:
        show_name,number_of_tickets,seat_numbers=list_shows()
        total_amt,price=book_tickets(show_name, number_of_tickets, *seat_numbers)
        total_amt=loyalty_combo_offer(total_amt,number_of_tickets)
        total_amt,pay_method=calculate_total(total_amt,price, number_of_tickets, discount=30)
        print("Total amount to pay:",total_amt)
    elif ch==2:
        book_tickets(show_name, number_of_tickets, *seat_numbers)
        print("Total amount paid:",total_amt)
    elif ch==3:
        cancel_tickets=cancel_booking(price,total_amt)
    elif ch==4:
        print("Exit successful")
        break
    else:
        print("Invalid option")