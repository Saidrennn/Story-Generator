# This is my second Python assignment.
# In this script, I take the user's name and the city they live in,
# and use that information to generate a custom short story.
# I used f-strings to insert the variables into the story dynamically.

name = input("Please enter your name: ")
location = input("Please enter the city you live in: ")

print(f"""{name} woke up early and started walking through the streets of {location}.
The sun was just rising and the weather was slightly chilly.
They found a small cafe and had a hot cup of tea.
Suddenly, a dog started barking outside.
Curiously, {name} went out to see the dog.
The dog looked at them kindly and wagged its tail
{name} thought the dog might be hungry, so they went to a bakery and bought some bread.
When they offered it, the dog ate it quickly. This made {name} happy.
For the rest of the day, they explored the beautiful places in {location}.
{name} thought about how beautiful {location} really was.
In the evening, they started walking home.
On the way, they saw an old friend.
They had coffee and chatted together.
Later, while heading home, they looked up at the sky.
The stars were shining, and the character felt peaceful and calm.
""")
