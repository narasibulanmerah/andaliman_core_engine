from config import OUTPUT_DIR


def write_runtime(content, filename="andaliman_full.md"):
    OUTPUT_DIR.mkdir(exist_ok=True)

    output = OUTPUT_DIR / filename
    output.write_text(content, encoding="utf-8")

    return output
