from Chess import Chess


class Cli:
    def __init__(self):
        self.game = Chess()

    def start(self):
        while True:
            if not self.game.play_turn():
                break


def main():
    cli = Cli()
    cli.start()


if __name__ == "__main__":
    main()
