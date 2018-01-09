import string
import random

def format_user_input(user_input):
    user_input = user_input.split("://")
    user_input = user_input[-1].split("www.")
    return user_input[-1]

# def create_rand_ending(qs):
#     temp="".join(random.choice(string.ascii_uppercase + string.digits))
#     while
#         Entry.objects.values_list('column_name', flat=True)
