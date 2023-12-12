# menu.py

def display_startup_menu():
    menu = """
    Salesforce Describe Utility
    ---------------------------
    Available Commands:
    - Describe a specific object: python sf_describe.py -e [env] -o [object]
    - List all available objects: python sf_describe.py -e [env]
    - Exit: Ctrl+C
    ---------------------------
    """
    print(menu)

# Add more menu-related functions as needed
