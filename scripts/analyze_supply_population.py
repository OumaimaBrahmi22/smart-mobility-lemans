import csv
from pathlib import Path

COMMUNES_FILE = Path("data/reference/communes.csv")
STOPS_FILE = Path("data/gtfs_static/stops_frequency.csv")
OUTPUT_FILE = Path("data/analysis/supply_vs_population.csv")


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


communes = read_csv(COMMUNES_FILE)
stops = read_csv(STOPS_FILE)

# Total scheduled stop-level supply for each commune
supply_by_commune = {}

for stop in stops:
    commune = stop["nearest_commune"].strip()
    if not commune:
        continue

    daily_count = int(float(stop["daily_trip_count"] or 0))
    supply_by_commune[commune] = (
        supply_by_commune.get(commune, 0) + daily_count
    )

# Compare supply with population
results = []

for commune in communes:
    name = commune["commune"].strip()
    population = int(float(commune["population"] or 0))
    supply = supply_by_commune.get(name, 0)

    if population <= 0:
        continue

    results.append({
        "commune": name,
        "population": population,
        "daily_stop_trip_total": supply,
        "supply_per_1000_inhabitants": round(
            supply / population * 1000, 2
        ),
    })

# Highest supply relative to population first
results.sort(
    key=lambda row: row["supply_per_1000_inhabitants"],
    reverse=True,
)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[
        "rank",
        "commune",
        "population",
        "daily_stop_trip_total",
        "supply_per_1000_inhabitants",
    ])
    writer.writeheader()

    for rank, result in enumerate(results, start=1):
        writer.writerow({"rank": rank, **result})

print(f"Analysis generated: {OUTPUT_FILE}")
print(f"Communes ranked: {len(results)}")

