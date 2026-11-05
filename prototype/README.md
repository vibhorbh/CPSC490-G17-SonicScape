# Prototype

Proof-of-concept code for SonicScape. **Prototype v0 is due Sep 27** with
the proposal, and it grows every sprint; the Week-8 in-class check demos from
this folder.

## How to run

```bash
cd prototype/src/sonicscape
python main.py #no current code as program prototype will be developed in the next sprint
```

## How to test

```bash
cd prototype
pip install pytest              # once
python -m pytest tests -q       # 4 tests
```

CI runs exactly these tests on every pull request (job **Prototype build &
tests**). If you use Node instead of Python, put a `package.json` here with a
`test` script and CI will detect and run that instead.

## What it proves

That the project structure, dependency list, and configuration template are in
place and match the architecture diagram, so Sprint 3 can add the first
end-to-end slice without restructuring.

## Status

| Sprint | Increment |
|---|---|
| Sprint 2 | Project Skeleton, .env.example, README |
| Sprint 3 | Planned: first end-to-end slice |
