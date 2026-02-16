def data_recovery() -> None:
    try:
        file = open("ancient_fragment.txt", "r")
        content: str = file.read()
        file.close()
    except Exception:
        print("ERROR: Storage vault not found.")
    else:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print("Accessing Storage Vault: ancient_fragment,txt")
        print("Connection established...\n")
        print(f"RECOVERED DATA:\n{content}\n")
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    data_recovery()
