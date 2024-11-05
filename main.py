from game import renderer

def main():
    instance = renderer.Game(1200,800,"Cellular Automata")
    instance.start()

if __name__ == "__main__":
    main()