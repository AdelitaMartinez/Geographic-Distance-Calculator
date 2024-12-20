# MartinezP6
# Programmer: Adelita Martinez
# Email: 94martinez.adelita@gmail.com
# Purpose: Demonstrate use of functions
# Python version: 3.12.3

from math import sin, cos, sqrt, atan2, radians

# Header function and program summary
def header():
  print("\nWelcome!")
  print("This program calculates the distance between two geographic points.")
  print("You will enter the latitude and longitude for each point in decimal degrees.")

# write "get_location" function, get user input(latitude, longitude)
def get_location():
  lat = float(input("Enter latitude in decimal degrees: "))
  lon = float(input("Enter longitude in decimal degrees: "))
  # Return lat and lon
  return (lat, lon)
  
# write "distance" function to take in two points(args), calculate the distance
def distance(point1, point2):
 r = 3958.8 # Radius of the earth in miles
 lat1, lon1 = point1
 lat2, lon2 = point2

 # Convert lat and long from degrees to radians
 lat1 = radians(lat1)
 lon1 = radians(lon1)
 lat2 = radians(lat2)
 lon2 = radians(lon2)

  # formula 
 dlat = lat2 - lat1
 dlon = lon2 - lon1

 a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 c = 2 * atan2(sqrt(a), sqrt(1 - a))
 distance = r * c

 return distance, dlat, dlon
  
# Main
def main():
  # Call the header function
  header()

  while True: 
    # Get the first location 
    print("\nEnter the first location: ")
    point1 = get_location()

    # Get second location
    print("\nEnter the second location: ")
    point2 = get_location()

    # Calculate the distance between 2 points
    dist, dlat, dlon = distance(point1, point2)

    # Display difference in latitude and longitude
    print(f"lat1: {dlat} lon1: {dlon}")

    # Display results 
    print(f"\nThe distance between the two points is {dist:.2f} miles.")

    # Ask the user if they want to calculate another distance, break if no
    another = input("\nDo you want to calculate another distance? (yes/no): ")
    if another != 'yes':
      break

  # Goodbye message and thanks
  print("\nThank you for using this program, Goodbye!")

# Run main function 
if __name__ == "__main__":
 main()
