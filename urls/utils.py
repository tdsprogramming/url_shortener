import string
import random

def format_user_input(user_input):
    user_input = user_input.split("://")
    user_input = user_input[-1].split("www.")
    return user_input[-1]
