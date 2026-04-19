def main() -> None:
    print("Initializing new storage unit: new_discovery.txt")
    try:
        lines: list[str] = ["[ENTRY 001] New quantum algorithm discovered\n",
                            "[ENTRY 002] Efficiency increased by 347%\n",
                            "[ENTRY 003] Archived by Data Archivist trainee"]
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for line in lines:
            file.write(line)
            print(line,
                  end="")
        print("\n\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term "
              "preservation.")
        file.close()
    except FileNotFoundError:
        print("File wasn't found")
    except Exception as error:
        print(f"An error occurred: {error}")
        file.close()


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    main()
