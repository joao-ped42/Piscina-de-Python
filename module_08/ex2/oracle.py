import os


def main() -> None:
    try:
        from dotenv import load_dotenv
    except Exception:
        print("You need to install 'python-dotenv'")
        return
    load_dotenv()
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE')}")
    print(f"API Access: {os.getenv('API')}")
    print(f"Log Level: {os.getenv('LOG')}")
    print(f"Zion Network: {os.getenv('ZION')}")


if (__name__ == "__main__"):
    main()
