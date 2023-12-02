import sys
from functools import reduce

from app.support.utils import main, parse_module_to_day, timing


def parse(s):
    games = []
    for line in s.splitlines():
        game, bags = line.split(":")
        game = dict([map(str.lower, game.split())])
        game["game"] = int(game["game"])

        parse_bags = []
        for bag in bags.split(";"):
            play = {}
            for cube in bag.split(","):
                c = cube.strip().split()
                c[0] = int(c[0])
                play = play | dict([reversed(c)])
            parse_bags.append(play)
            game["bags"] = parse_bags
        games.append(game)
    return games


CHECK_FOR_GAMES_WITH = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@timing
def compute_part_1(s: str) -> int:
    games = []
    parsed = parse(s)
    for game in parsed:
        game_ok = True
        for k, v in CHECK_FOR_GAMES_WITH.items():
            for bag in game.get("bags"):
                if bag.get(k, 0) > v:
                    game_ok = False
                    break
            if not game_ok:
                break
        if game_ok:
            games.append(game.get("game"))
    return sum(games)


@timing
def compute_part_2(s: str) -> int:
    parsed = parse(s)
    minimum_power = []
    for game in parsed:
        colors = {"red": 0, "green": 0, "blue": 0}
        for bag in game.get("bags"):
            for color in ("red", "green", "blue"):
                c = bag.get(color, 0)
                if c > colors.get(color, 0):
                    colors[color] = c
        power = reduce(lambda acc, cur: acc * cur, colors.values(), 1)
        minimum_power.append(power)
    return sum(minimum_power)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
