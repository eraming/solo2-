from utils import main, page_generator
import sys



command = sys.argv[1]
print(command)
if command == "build":
    print("Build was specified")
    if __name__ == "__main__":
        main()
elif command == "new":
    print("New page was specified")
    print("Create new page: python manage.py new")
    page_generator()
else:
    print("Please specify 'build' or 'new'")
