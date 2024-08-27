from AjedrezCli import AjedrezCli


class Chess:
    def __init__(self):
        self.game = AjedrezCli()

    def start(self):
        self.game.initialize_pieces()


def main():
    cli = Chess()
    cli.start()


if __name__ == "__main__":
    main()
