import sys


def main() -> None:
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    arch_id: str = sys.stdin.readline().strip()
    print("Input Stream active. Enter status report: ", end="", flush=True)
    status_report: str = sys.stdin.readline().strip()
    print(f"\n[STANDARD] Archive status from {arch_id}: {status_report}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete",
          file=sys.stdout)


if (__name__ == "__main__"):
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        main()
    except Exception as e:
        print(e)
    print("\nThree-channel communication test successful.")
