import sys

def add_line_numbers(input_file):
    try:
        with open(input_file, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:6d}  {line}", end='')
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_emulator.py <input_file>")
    else:
        input_file = sys.argv[1]
        add_line_numbers(input_file)
if __name__ == "__main__":
  import sys

def are_files_equal(file1, file2):
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()

            return content1 == content2
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_emulator.py <file1> <file2>")
    else:
        file1, file2 = sys.argv[1], sys.argv[2]
        if are_files_equal(file1, file2):
            print("The files are the same.")
        else:
            print("The files are different.")
if __name__ == "__main__":
    import sys


    def grep(pattern, filename):
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line.strip())


    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: python grep.py <pattern> <filename>")
            sys.exit(1)

        pattern = sys.argv[1]
        filename = sys.argv[2]

        grep(pattern, filename)
if __name__ == "__main__":
    def wc(file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                num_lines = content.count('\n') + 1
                num_characters = len(content)

                print(f"Lines: {num_lines}")
                print(f"Characters: {num_characters}")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    file_name = "file.txt"
    wc(file_name)
if __name__ == "__main__":
    import sys


    def load_dictionary(dictionary_file):
        try:
            with open(dictionary_file, 'r') as file:
                return {word.strip().lower() for word in file}
        except FileNotFoundError:
            print(f"Error: Dictionary file '{dictionary_file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while loading the dictionary: {str(e)}")
            sys.exit(1)


    def spell_check(input_file, dictionary_file):
        dictionary = load_dictionary(dictionary_file)

        try:
            with open(input_file, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    words = line.strip().split()
                    for word in words:
                        word_lower = word.lower()
                        if word_lower not in dictionary:
                            print(f"Line {line_number}: '{word}' is not in the dictionary.")

        except FileNotFoundError:
            print(f"Error: Input file '{input_file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while spell-checking: {str(e)}")
            sys.exit(1)


    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: python spell_checker.py <input_file> <dictionary_file>")
            sys.exit(1)

        input_file = sys.argv[1]
        dictionary_file = sys.argv[2]

        spell_check(input_file, dictionary_file)