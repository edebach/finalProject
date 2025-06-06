# scripts/gen_trips.py
import subprocess, random, json, os, itertools, pathlib

SUMO_TOOLS = os.environ["SUMO_HOME"] + "/tools"
net = "../data/osm/shanghai.net.xml"

SCENARIOS = {
    "base":  {"period":5,  "begin":0,   "end":3600,  "prefix":"base"},
    "peak":  {"period":2,  "begin":0,   "end":7200,  "prefix":"peak_am"},
    "event": {"period":1,  "begin":5400,"end":9000, "prefix":"event"}
}

def make_trips(tag, cfg):
    outdir = pathlib.Path(f"../scenarios/{tag}")
    outdir.mkdir(parents=True, exist_ok=True)
    trips = outdir / f"{cfg['prefix']}.trips.xml"
    seed  = random.randint(0,2**31-1)
    cmd = [
        "python", f"{SUMO_TOOLS}/randomTrips.py",
        "-n", net, "--trip-file", trips,
        "--period", str(cfg["period"]),
        "--begin", str(cfg["begin"]),
        "--end", str(cfg["end"]),
        "--seed", str(seed),
        "--validate", "true"
    ]
    subprocess.run(cmd, check=True)
    return trips

if __name__ == "__main__":
    for tag,cfg in SCENARIOS.items():
        print("Generating", tag)
        make_trips(tag,cfg)
