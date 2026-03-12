def main() -> None:
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        file: open = open("data-generator-tools/ancient_fragment.txt", "r")
        text: str = file.read()
        print("Connection established...\n")
        print("RECOVERED DATA")
        print(text)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception as error:
        print(f"An error occurred: {error}")


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    main()
