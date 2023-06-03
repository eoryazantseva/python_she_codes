light_color = input("What is the color of the lights?")
question = input("Was the car detected?")
car_detected = False
if question == "Yes":
    car_detected = True


if (light_color == "Red" and car_detected):
    print("Flash!")
else:
    print("Do nothing")