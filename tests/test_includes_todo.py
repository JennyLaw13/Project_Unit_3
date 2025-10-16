"""
Given a line that starts with "#TODO"
It returns True
"""
""" includes_todo("#TODO buy milk") => True """

from lib.includes_todo import includes_todo

def test_includes_todo_at_start():
    assert includes_todo("#TODO buy milk") == True

"""
Given a line that ends with "#TODO"
It returns True
"""
"""includes_todo("learn to test drive my code #TODO") => True"""

def test_includes_todo_at_end():
    assert includes_todo("learn to test drive my code #TODO") == True


"""
Given a line contains "#TODO" 
It returns True 
"""
"""includes_todo("here is a #TODO example") => True"""

def test_includes_todo_at_all():
    assert includes_todo("here is a #TODO example") == True


"""
Given a line without "#TODO"
It returns False 
"""
"""includes_todo("drink tea") => False"""

def test_includes_no_todo():
    assert includes_todo("drink tea") == False


"""
Given a line contains "#todo"
It returns False
"""
"""includes_todo("#todo buy milk") => False"""

def test_includes_lowercase_todo():
    assert includes_todo("#todo buy milk") == False


"""
Given a line contains a similar string without # like "TODO"
It returns False
"""
"""includes_todo("TODO buy milk") => False"""

def test_includes_todo_no_hash():
    assert includes_todo("TODO buy milk") == False


"""
Given an empty string 
It returns False
"""
"""includes_todo("") => False"""

def test_empty_string():
    assert includes_todo("") == False