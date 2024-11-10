# try:
#     x = 10
#     y = "5"
#     z = x + int(y)

# except TypeError as e:
#     print(f"An error occurred: {e}")
# else:
#     print(f"from else")
# finally:
#     print("from finally")

def process_file():
    try:
        print("Opening file")
        try:
            print("Reading file contents")
            raise ValueError("File format error") # simulating a file format error
        except ValueError as e:
            print(f"Error while reading file: (e)")
            return "Error handled in read operation"
        finally:
            print("Ensuring file read operations are finalized")
            return "File read finalized"
    except Exception as e:
        print(f"Outer exception handler: (e)")
        return "Outer exception handler return"
    finally:
        print("Closing file")
        return "File closed"

result = process_file()
print("Result:", result)