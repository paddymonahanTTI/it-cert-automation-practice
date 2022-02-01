#!/usr/bin/env python3

import re

def validate_user(username, minlen):
  if not re.match('^[a-z0-9._]*$', username):
    return False
    # Usernames can't begin with a number
  if username[0].isnumeric():
    if username[0].isnumeric():
      return False
    # Usernames cant begin with anything else than a character
  if re.search('^[a-z]', username) == None:
    return False
  return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


