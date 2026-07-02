# Contributing to sent

Thank you for your interest in contributing to **sent**! This project is open source under the [MIT License](LICENSE).

## Getting started

### Prerequisites

- Python 3.8 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Development setup

```bash
git clone https://github.com/kalanakt/sent.git
cd sent
uv sync --all-extras
```

Or with pip:

```bash
pip install -e ".[dev]"
```

## Running tests

```bash
uv run pytest test/ -v
```

Tests run automatically in CI on Python 3.10, 3.11, and 3.12 for every push and pull request to `main`.

## Linting

```bash
ruff check sent test
```

CI runs the same check (configured in `pyproject.toml`, excluding auto-generated TL modules). Please fix lint issues before opening a PR.

## Regenerating TL types

TL types and RPC functions under `sent/tl/` are **auto-generated**. Do not edit them by hand.

After updating schema files in `sent/_codegen/data/`:

```bash
python -m sent._codegen.generate
```

Commit the regenerated output together with any schema changes.

## Documentation site

After API or TL changes, regenerate and **commit** the MDX (Vercel does not run the generator):

```bash
uv run python -m sent._codegen.generate   # if TL schema changed
cd docs && bun run generate-docs
```

The generator writes to `docs/src/pages/api/` and `docs/src/pages/tl/`. **Commit the updated MDX files** with your changes.

Vercel and `bun run build` only compile what is already in the repo — they do not run the Python generator.

### Local docs dev

```bash
cd docs
bun install
bun run dev    # http://localhost:5173
```

### Production build

```bash
cd docs
bun run build  # output → docs/dist/
bun run preview
```

## Pull request guidelines

1. Fork the repository and create a feature branch from `main`.
2. Keep changes focused — one logical change per PR.
3. Add or update tests when fixing bugs or adding behavior.
4. Ensure `pytest` and `ruff` pass locally.
5. Write clear commit messages (e.g. `fix: correct IGE decrypt IV chaining`).
6. Open a PR against `main` with a short description of what changed and why.

## Project structure

| Path | Purpose |
|------|---------|
| `sent/client/` | High-level `TelegramClient` API |
| `sent/network/` | MTProto transport and sender |
| `sent/crypto/` | AES, auth key, SRP |
| `sent/tl/` | Generated TL types and functions |
| `sent/_codegen/` | TL schema parser and code generator |
| `sent/events/` | Event handlers |
| `sent/sessions/` | Session persistence |
| `examples/` | Runnable bot and user-account examples |
| `test/` | Unit tests |
| `bench/` | Performance benchmarks |

## Releasing to GitHub and PyPI

Version `1.0.0` is defined in `pyproject.toml`, `sent/version.py`, and `sent/__init__.py`. Keep these in sync when bumping versions.

### One-time PyPI Trusted Publisher setup

1. Log in to [PyPI](https://pypi.org) and open the **sent** project.
2. Go to **Publishing** → **Add a new pending publisher** (or manage trusted publishers).
3. Configure:
   - **PyPI project name:** `sent`
   - **Owner:** `kalanakt`
   - **Repository:** `sent`
   - **Workflow name:** `publish.yml`
   - **Environment name:** `pypi`
4. On GitHub, create an environment named `pypi` under **Settings → Environments** (no secrets required — OIDC handles auth).

### Publishing a new release

1. Merge all changes into `main`.
2. Update the version in `pyproject.toml`, `sent/version.py`, and `sent/__init__.py`.
3. Commit, tag, and push:

   ```bash
   git tag v1.0.0
   git push origin main
   git push origin v1.0.0
   ```

4. Create a **GitHub Release** from the tag on https://github.com/kalanakt/sent/releases.
   - Publishing the release triggers `.github/workflows/publish.yml`, which builds and uploads to PyPI automatically.

### Manual PyPI upload (fallback)

```bash
python -m pip install build twine
python -m build
twine check dist/*
twine upload dist/*
```

You will need a PyPI API token for manual uploads.

## Questions?

Open an [issue](https://github.com/kalanakt/sent/issues) if you run into problems or want to discuss a larger change before coding.
