from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    print(os.getenv('API_LOGIN'))

if __name__ == "__main__":
    main()