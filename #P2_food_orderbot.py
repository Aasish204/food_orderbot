import pyttsx3
from PIL import Image

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Response templates
response_1 = ("\nWelcome to Aasish restaurant. Here's the menu:\n"
              "Pizza: Rs.600\nMomo: Rs.100\nBurger: Rs.500\n"
              "Chowmin: Rs.110\nCoffee: Rs.180\n")
response_2 = ("Enter the items you want to order (comma-separated): ")
response_3 = ("\nSorry, none of the items you entered are on the menu.\n")
response_4 = ("Are you sure you want to order these items?\nEnter 'yes' or 'no': ")
response_5_template = ("\nOrder Successful.\nTotal amount to pay is Rs.{total}\n")
response_6 = ("Your order will be delivered soon.\nThank you.")
response_7 = ("\nYour order has been cancelled.\nThank you.\n")
response_8 = ("\nInvalid response.\n")
response_9 = ("Choose the payment method:\nEnter 1 for Cash on Delivery\nEnter 2 for Online Payment")
response_10 = ("\nYour order will be delivered soon.\nThank you.")
response_11 = ("\nScan this QR code to make a payment.\nThank you.\n")

# Function to speak messages
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Display menu
print(response_1)
speak("Welcome to Aasish restaurant. Here's the menu.")

# Menu dictionary with lowercase keys
menu = {
    "pizza": 600,
    "momo": 100,
    "burger": 500,
    "chowmin": 110,
    "coffee": 180
}

# Take user input
speak(response_2)
user_input = input(response_2).lower()
items = [item.strip() for item in user_input.split(',')]

# Validate items
valid_items = []
invalid_items = []
order_total = 0

for item in items:
    if item in menu:
        valid_items.append(item)
        order_total += menu[item]
    else:
        invalid_items.append(item)

# Handle invalid items
if invalid_items:
    print(f"\nInvalid items: {', '.join(invalid_items)}")
    speak("Some of the items you entered are not in the menu.")

if not valid_items:
    print(response_3)
    speak(response_3)
    exit()

# Confirm order
speak(response_4)
confirmation = input(response_4).lower()

if confirmation == "yes":
    response_5 = response_5_template.format(total=order_total)
    print(response_5)
    speak(f"Your total amount is {order_total} rupees.")
elif confirmation == "no":
    print(response_7)
    speak(response_7)
    exit()
else:
    print(response_8)
    speak(response_8)
    exit()

# Choose payment method
print(response_9)
speak(response_9)
payment = input("Enter 1 or 2: ")

if payment == "1":
    print(response_10)
    speak(response_10)
elif payment == "2":
    print(response_11)
    speak(response_11)

    # 🔄 Use your own QR image file
    try:
        img = Image.open("my_qr.jpg")
        img.show()
    except FileNotFoundError:
        print("QR code image not found. Make sure 'my_qr.png' exists in the same folder.")
        speak("QR code image not found.")
else:
    print(response_8)
    speak(response_8)





 


 