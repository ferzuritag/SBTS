def get_tsp_instance_data(instance_name: str):
    with open(f"./instances/{instance_name}.tsp", "r") as f:
        content = f.read()

    lines = content.strip().splitlines()
    name = ""
    coords = []
    reading_coords = False

    for line in lines:
        line = line.strip()
        if line.startswith("NAME"):
            name = line.split(":", 1)[1].strip()
        elif line.startswith("NODE_COORD_SECTION"):
            reading_coords = True
        elif line.startswith("EOF"):
            break
        elif reading_coords:
            parts = line.split()
            if len(parts) >= 3:
                _, x, y = parts
                coords.append((int(x), int(y)))

    return name, coords