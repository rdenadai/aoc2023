# Advent of Code 2023

Advent of Code 2023

## Config

Create a .env file at the root of the project.

```bash
session=<cookie session from logged in browser>
```

## Executing

### Python

Install (create venv and install deps)

```bash
$> poetry shell
```

Run tests:

```bash
$> pytest -s --cov=app --cov-report term-missing tests/
```

Run single day, to get the results:

```bash
$> python -m app.day01.parts
```

Debug:

```bash
$> python -m debugpy --listen localhost:5678 --wait-for-client -m app.day01.parts
```

### Javascript

```bash
$> node app/day01/parts.js
```

### OCaml

```bash
$> dune build @all
$> dune exec app/day01/parts.exe
```
