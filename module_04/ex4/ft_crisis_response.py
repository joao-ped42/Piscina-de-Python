def file_check(file_name: str, mode: str) -> None:
    print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
    with open(f"data-generator-tools/{file_name}", mode) as file:
        line: str = file.read()
        print(f"SUCCESS: Archive recovered ''{line}''")


def main() -> None:
    try:
        file_check("lost_archive.txt", "r")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")
    try:
        file_check("classified_data.txt", "r+")
    except PermissionError:
        print("RESPONSE: : Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")
    try:
        file_check("standard_archive.txt", "r")
    except Exception:
        print("STATUS: An error has occurred")
    print("STATUS: Normal operations resumed")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    main()
