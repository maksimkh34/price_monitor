from banners import *
from list_items import *

start_text()
match menu():
    case 0:
        print_items(import_db())
    case 4:
        exit_banner()
        exit(0)
