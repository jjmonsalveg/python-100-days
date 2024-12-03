# Example 1
try:
    file = open("unexistent.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asd"])
except FileNotFoundError:
    file = open("unexistent.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

    raise ZeroDivisionError("This a manually raised error")

# Example 2
# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")
# bmi = weight / height ** 2
# print(bmi)


# Example 3
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")

# make_pie(4)

# Example 4
# facebook_posts = [
#     {"Likes": 21, "Comments": 2},
#     {"Likes": 13, "Comments": 2, "Shares": 1},
#     {"Likes": 33, "Comments": 8, "Shares": 3},
#     {"Comments": 4, "Shares": 2},
#     {"Comments": 1, "Shares": 1},
#     {"Likes": 19, "Comments": 3},
# ]


# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post["Likes"]
#         except KeyError:
#             pass
#     return total_likes


# count_likes(facebook_posts)
