#!/usr/bin/env python3
"""
A simple Hello World program to demonstrate code in a GitHub repository.
This file can be used to practice making commits, creating branches, and more!
"""

def greet(name="World"):
    """
    Greet someone by name.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Main function to run the greeting."""
    print(greet())
    print(greet("GitHub Explorer"))
    print("\n🎉 Welcome to GitHub!")
    print("Try editing this file and committing your changes!")


if __name__ == "__main__":
    main()
