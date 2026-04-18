from mutant import Mutant

def simulate():
    m = Mutant("Zyra", "Telekinesis", 5)
    print(m)
    print(m.use_power())

if __name__ == "__main__":
    simulate()
