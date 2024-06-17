# MartinezP6
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Demonstrate use of functions
# Python version: 3.12.3

from math import sin, cos, sqrt, atan2, radians

# Header function and program summary
def header():
  print("Welcome!")
  print("This program calculates the distance between two geographic points")
  print("You will enter the latitude and longitude for each point in decimal degrees")

  # write "get_location" function, get user input(latitude, longitude)
  def get_location():
    lat = float(input("Enter latitude in decimal degrees: "))
    lon = float(input("Enter longitude in decimal degrees: "))
    # Return lat and lon
    return (lat, lon)
  
  # write "distance" function to take in two points(args), calculate the distance
  def distance(point1, point2):
    r = 6371 # Radius of the earth in kilometers
    lat1, lon1 = point1
    lat2, lon2 = point2

    # Convert lat and long from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat1 = radians(lat2)
    lon2 = radians(lon2)