#Note that the story is a string, and we can use string methods to manipulate it and strings are immutable, which means that we cannot change the original string, but we can create new strings based on the original one.

story = "joy!!!!!!!!!!!!!."

print(story.upper())

print(story.lower())

print(story.rstrip("!."))

print(story.replace("joy", "Tnu"))

print(story.split("!"))


me = "watashi wa namae wa Amito desu"
print(me.capitalize())

print(me.center(75))

print(me.count("w"))

print(me.endswith("desu"))

print(me.find("namae"))