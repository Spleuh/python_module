def crisis_response(filename: str) -> None:
    try:
        with open(filename, "r") as fd:
            content: str = fd.read()
            print(f"{content}")
    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        if e.__class__.__name__ == "FileNotFoundError":
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        elif e.__class__.__name__ == "PermissionError":
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
    else:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")
    finally:
        print()


def crisis_demo():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        crisis_response("lost_archive.txt")
        crisis_response("classified_vault.txt")
        crisis_response("standard_archive.txt")
    except Exception as e:
        print(f"{e}")
    else:
        print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_demo()
