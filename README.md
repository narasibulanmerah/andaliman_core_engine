# Andaliman Core Engine

Andaliman Core Engine is a specification-driven runtime builder for Large Language Models (LLMs).

The project compiles modular Markdown specifications into a unified runtime document that can be consumed by GPT, Claude, Gemini, or other LLMs.

---

## Features

- Specification-first architecture
- Runtime builder
- Canonical specification pipeline
- Markdown compiler
- Git-based workflow

---

## Project Structure

```
andaliman_core_engine/

specification/
scripts/
output/

install.sh
run.sh
README.md
LICENSE
CHANGELOG.md
```

---

## Installation

Clone repository

```bash
git clone git@github.com:narasibulanmerah/andaliman_core_engine.git
```

Enter project

```bash
cd andaliman_core_engine
```

Run installer

```bash
./install.sh
```

---

## Build Runtime

```bash
./run.sh
```

Generated runtime

```
output/
    andaliman_full.md
```

---

## Development Workflow

```
Edit Specification

↓

Build Runtime

↓

Commit

↓

Push
```

---

## License

MIT License
