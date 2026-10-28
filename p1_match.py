Seats=int(input("Enter Number of Seats: "))

match Seats:
    case 0:
        print("No Seats are Selected")
    case _ if Seats>=1 and Seats <=5:
        print("Booking's are Allowed")
    case _ if Seats>5:
        print("Maximum Seats are 5 Allowed")
    case _ if Seats<0:
        print("Invalid Number!")