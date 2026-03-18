def main() -> None:
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        file: open = open("../ancient_fragment.txt", "r")
        text: str = file.read()
        print("Connection established...\n")
        print("RECOVERED DATA")
        print(text)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("File wasn't found")
    except Exception as error:
        print(f"An error occurred: {error}")
        file.close()


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    main()
