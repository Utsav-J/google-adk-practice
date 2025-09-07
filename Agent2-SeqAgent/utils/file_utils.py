def load_instructions_file(filename: str, default: str = "") -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()  # Read and return the entire contents of the file.
    except FileNotFoundError:
        print(f"File not found: {filename}. Using default.")
    except Exception as e:
        # Catch any other exception (e.g. permission issues, IO errors) and log it.
        print(f"Failed to load {filename}: {e}")

    return default