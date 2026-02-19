def vault_security():
    """demo vault security using with"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiatig secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as f:
            content: str = f.read()
            print(f"{content}\n")
        print("SECURE PRESERVATION:")
        with open("security_protocols.txt", "r") as sp:
            content = sp.read()
            print(f"{content}")
    except Exception as e:
        print(f"{e}")
    finally:
        print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security()
