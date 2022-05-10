# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name: str, msg: str = "Hello, <name>!") -> str:
    return msg.replace("<name>", name)


def force(mass: float, body: str = "earth") -> float:
    gravity = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    return round(mass * gravity[body], 2)


def pull(m1: float, m2: float, d: float) -> float:
    g = 6.674 * 10 ** -11
    return g * m1 * m2 / d ** 2


def main():
    greet('Jurre')
    force(0.1, 'saturn')
    pull(800, 900, 5)


if __name__ == "__main__":
    main()
