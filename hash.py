import hashlib
successful_matches = 0

def encrypt_hash(user_file, buffer_size=65536):
    sha_256 = hashlib.sha256()
    try:
        with open(user_file, "rb") as file:
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                sha_256.update(data)
            return sha_256.hexdigest()
    except FileNotFoundError:
        print("Error: File '" + user_file + "' not found.\n")

def compare_hash(user_hash, *user_files):
    global successful_matches
    results = []
    for user_file in user_files:
        file_hash = encrypt_hash(user_file)
        results.append(user_hash == file_hash)

        if user_hash == file_hash:
            successful_matches += 1
    return results

def main():
    global successful_matches
    print("Welcome to the file integrity system.\n\n")
    num_files = int(input("How many files would you like to check? | Files: "))

    print("\n\n")
    user_files = []

    for i in range(num_files):
        user_file = input("Enter the path for file " + str(i + 1) + ": ").strip()
        user_files.append(user_file)

    print("\n\n")
    user_hashes = []

    for i in range(num_files):
        user_hash = input("Enter the file hash for file " + str(i + 1) + ": ").strip()
        user_hashes.append(user_hash)

    print("\n\n")
    pass

    for i in range(num_files):
        if len(user_hashes[i]) == 64 and user_hashes[i].lower().isalnum():
            result = compare_hash(user_hashes[i], user_files[i])
            if result[0]:
                print("Success: The hash matches for file " + user_files[i] + ".")
            else:
                print("Error: The hash does not match for file " + user_files[i] + ".")
        else:
            print("Error: Invalid hash format for file " + user_files[i] + ". Please provide a valid SHA-256 hash.")
    print("\n\n")
    print("Summary: " + str(successful_matches) + " out of "+ str(num_files) + " files matched their expected hashes.")
  
main()
