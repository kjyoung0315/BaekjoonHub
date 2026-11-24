import sys

tokens = sys.stdin.read().split()

if tokens:
    print(
        "\n".join(
            str(int(tokens[i + 1]) // (int(tokens[i]) + 1))
            for i in range(0, len(tokens), 2)
        )
    )