import sys


def stream_management():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        print("Input Stream active. Enter archivist ID: ", end="", flush=True)
        arch_id = sys.stdin.readline()
        arch_id = arch_id[:-1]
        print("Input Stream active. Enter status report: ", end="", flush=True)
        report = sys.stdin.readline()
        report = report[:-1]
        print()
        sys.stdout.write(f"[STANDARD] Archive status from {arch_id}:"
                         f" {report}\n")
        sys.stdout.flush()
        raise Exception
    except Exception:
        sys.stderr.write("[ALERT] System diagnostic: Communication "
                         "channels verified\n")
        sys.stderr.flush()
    finally:
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        sys.stdout.flush()
        print()
        print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
