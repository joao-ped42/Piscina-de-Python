def main() -> None:
    try:
        print("Initiating secure vault access...")
        with open("classified_data.txt", "r") as file1:
            print("Vault connection established with failsafe protocols\n")
            lines1: str = file1.read()
            print("SECURE EXTRACTION:")
            print(lines1)
        with open("security_protocols.txt", "r") as file2:
            print("\nSECURE PRESERVATION:")
            lines2: str = file2.read()
            print(lines2)
        print("Vault automatically sealed upon completion")
    except Exception as e:
        print(f"An error has occurred: {e}")
    finally:
        print("\nAll vault operations completed with maximum security.")


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    main()
