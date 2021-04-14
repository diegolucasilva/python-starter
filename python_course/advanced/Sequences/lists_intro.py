computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])

print("0 to 3 {}".format(computer_parts[0:3]))

print(computer_parts)


computer_parts[0:] = ["trackball"]
print(computer_parts)
