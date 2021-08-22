import sys
import math

def test_cases_reader():
    all_lines = tuple(sys.stdin.readlines())
    line_pos = 0

    while True:
        lines = []
        while line_pos < len(all_lines):
            line = all_lines[line_pos]
            line_pos += 1
            if len(line.strip()) == 0:
                break
            lines.append(line)
        
        if not lines:
            return

        tokens = tuple(map(float, "".join(lines).split()))
        lot_area = tokens[0]

        def _roofs_reader():
            for i in range(1, len(tokens), 4):
                yield tokens[i:i + 4]
        
        yield lot_area, _roofs_reader()

col_sep = "     "

n_lots = 0
total_lot_area = total_roof_surface_area = total_roof_floor_area = 0

print(
    "Roof Area{s}Floor Area{s}% Covered\n"
    "---------{s}----------{s}---------".format(s=col_sep)
)

for lot_area, roofs_reader in test_cases_reader():
    total_lot_area += lot_area
    n_lots += 1

    roof_surface_area = roof_floor_area = 0
    for roof_info in roofs_reader:
        baseline_len, ridge_len, br_distance, inclination = roof_info
        roof_surface_area += ((baseline_len + ridge_len) * br_distance) / 2
        projected_distance = br_distance * math.cos(math.radians(inclination))
        roof_floor_area += ((baseline_len + ridge_len) * projected_distance) / 2
    
    rain_interception_portion = roof_floor_area / lot_area

    total_roof_surface_area += roof_surface_area
    total_roof_floor_area += roof_floor_area

    print("{surface_area:9.2f}{s}{floor_area:10.2f}{s}{covered:9.2%}".format(
        surface_area=roof_surface_area,
        floor_area=roof_floor_area,
        covered=rain_interception_portion,
        s=col_sep
    ))

total_area_covered_portion = total_roof_floor_area / total_lot_area
average_root_surface_area = total_roof_surface_area / n_lots
average_floor_surface_area = total_roof_floor_area / n_lots

print(f"""
Total surface area of roofs{total_roof_surface_area:12.2f}
Total area covered by roofs{total_roof_floor_area:12.2f}
Percentage of total area covered by roofs{total_area_covered_portion:9.2%}
Average roof surface area per lot{average_root_surface_area:16.2f}
Average floor space covered per lot{average_floor_surface_area:14.2f}""")
