import sys


def read_line():
    return sys.stdin.readline().strip()


def get_word_lengths(line):
    return tuple(len(word) for word in line.split())


def iter_test_case_lines():
    while True:
        try:
            line = read_line()
            if line:
                yield line
            else:
                break
        except:
            break


def find_valid_encryption_schema(line, known_line):
    encryption_schema = {}
    used_dst_letters = set()

    for src_letter, dst_letter in zip(line, known_line):
        if (src_letter == ' ') and (dst_letter == ' '):
            continue

        if src_letter in encryption_schema:
            if dst_letter == encryption_schema[src_letter]:
                continue
            else:
                return None
        else:
            if dst_letter in used_dst_letters:
                return None

        encryption_schema[src_letter] = dst_letter
        used_dst_letters.add(dst_letter)

    return encryption_schema


def decrypt_line(line, encryption_schema):
    return ''.join(
        (encryption_schema[letter] if letter != ' ' else ' ') for letter in line
    )


def main():
    n_cases = int(read_line())
    read_line()

    known_line = 'the quick brown fox jumps over the lazy dog'
    known_word_lengths = get_word_lengths(known_line)

    case_sep = ""

    for _ in range(n_cases):
        lines = []
        encryption_schemas = []

        for line in iter_test_case_lines():
            lines.append(line)

            word_lengths = get_word_lengths(line)
            if word_lengths == known_word_lengths:
                encryption_schema = find_valid_encryption_schema(
                    line, known_line
                )
                if encryption_schema is not None:
                    encryption_schemas.append(encryption_schema)

        curr_output = "No solution."

        if encryption_schemas:
            for encryption_schema in encryption_schemas:
                try:
                    curr_output = "\n".join(
                        decrypt_line(line, encryption_schema) for line in lines
                    )
                except KeyError:
                    continue
                else:
                    break

        print(f"{case_sep}{curr_output}")
        case_sep = "\n"


if __name__ == '__main__':
    sys.exit(main())
