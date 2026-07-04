from datetime import datetime


def build_runtime(files):
    build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header = f"""# Andaliman Runtime Specification

Generated : {build_time}

============================================================

"""

    runtime = [header]
    runtime.append("# ANDALIMAN CORE ENGINE\n\n")

    for file in files:
        runtime.append("=" * 60 + "\n")
        runtime.append(file.name + "\n")
        runtime.append("=" * 60 + "\n\n")
        runtime.append(file.read_text(encoding="utf-8"))
        runtime.append("\n\n")

    return "".join(runtime)
