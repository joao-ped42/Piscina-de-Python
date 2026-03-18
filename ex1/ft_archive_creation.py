def main() -> None:
    print("Initializing new storage unit: new_discovery.txt")
    try:
        lines: list[str] = ["[ENTRY 001] New quantum algorithm discovered",
                            "[ENTRY 002] Efficiency increased by 347%",
                            "[ENTRY 003] Archived by Data Archivist trainee"]
        file = open("../data-generator-tools/new_discovery.txt",
                    "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for line in lines:
            file.write(line)
            file.write("\n")
            print(line)
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term"
              "preservation.")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        file.close()


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    main()
