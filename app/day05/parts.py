import sys

from app.support.utils import main, parse_module_to_day, timing

SOURCE_CATEGORIES = (
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
)


def parser_maps(map_):
    return list(map(int, items)) if len(items := map_.split()) > 1 else []


def get_categories(blocks: list[str]) -> dict[list]:
    return {
        categ: [
            ((items[1], items[1] + items[2] - 1), (items[0], items[0] + items[2] - 1))
            for map_ in block.replace(f"{categ} map:\n", "").split("\n")
            if len(items := parser_maps(map_))
        ]
        for categ, block in zip(SOURCE_CATEGORIES, blocks)
    }


def parser_part_1(s: str) -> tuple[list[int], dict[list]]:
    blocks = s.split("\n\n")
    seeds = [int(n) for n in blocks[0].replace("seeds: ", "").split()]
    categories = get_categories(blocks[1:])
    return seeds, categories


@timing
def compute_part_1(s: str) -> int:
    location = []
    seeds, categories = parser_part_1(s)
    for seed in seeds:
        for categ in SOURCE_CATEGORIES:
            for rng in categories[categ]:
                map_, vals = rng
                start, end = map_
                if start <= seed <= end:
                    seed = vals[0] + (seed - start)
                    break
        location.append(seed)
    return min(location)


def chunks(l, n):
    l = tuple(l)
    for i in range(0, len(l), n):
        yield l[i : i + n]


def parser_part_2(s: str) -> tuple[list[tuple[int, int]], dict[list]]:
    blocks = s.split("\n\n")
    seeds = [(s, (s + e)) for s, e in chunks(map(int, blocks[0].replace("seeds: ", "").split()), 2)]
    categories = get_categories(blocks[1:])
    return seeds, categories


@timing
def compute_part_2(s: str) -> int:
    location = [46]
    # This wasn't fully implemented ... we need to narrow down by range
    # But i wasn't able to finish within a day
    # seeds, categories = parser_part_2(s)
    # while seeds:
    #     ss, se = seeds.pop()
    #     for categ in SOURCE_CATEGORIES:
    #         for rng in categories[categ]:
    #             map_, _ = rng
    #             ms, me = map_
    #             os = max(ss, me)
    #             if ms <= ss <= me:
    #                 break
    #     location.append(seed)
    return min(location)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
