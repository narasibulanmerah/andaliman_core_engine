from config import SPEC_DIR


def discover():

    return sorted(
        SPEC_DIR.glob("*.md")
    )
