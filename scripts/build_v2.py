from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_DIR = ROOT / "specification"
OUTPUT_DIR = ROOT / "output"

files = sorted(SPEC_DIR.glob("*.md"))

print(f"Found {len(files)} specification(s)\n")

for file in files:
    print(file.name)
print("\nReading files...\n")

for file in files:

    content = file.read_text(
        encoding="utf-8"
    )
runtime = []

runtime.append("# ANDALIMAN CORE ENGINE\n\n")

for file in files:

    runtime.append("=" * 60 + "\n")
    runtime.append(file.name + "\n")
    runtime.append("=" * 60 + "\n\n")

    runtime.append(
        file.read_text(
            encoding="utf-8"
        )
    )

    runtime.append("\n\n")

OUTPUT_DIR.mkdir(exist_ok=True)

output_file = OUTPUT_DIR / "andaliman_full.md"

output_file.write_text(
    "".join(runtime),
    encoding="utf-8"
)

print("\nBuild Success")
print(output_file)
