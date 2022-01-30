commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
#your code goes here
x = str (input())
if x in commands:
    print("OK")
else:
    print("Not supported")