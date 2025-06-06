# scripts/build_net.py
import os
import subprocess
import osmnx as ox
from pathlib import Path

CITY     = "Shanghai, China"
OUT_DIR  = Path("../data/osm")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. download OSM graph
G = ox.graph_from_place(CITY, network_type="drive", simplify=False)
osm_path = OUT_DIR / "shanghai.osm"
ox.io.save_graph_xml(G, filepath=osm_path)

# 2. convert to SUMO .net.xml via netconvert
net_path = OUT_DIR / "shanghai.net.xml"
cmd = [
    "netconvert",
    "--osm-files", str(osm_path),
    "--output-file", str(net_path),
    # optional clean-ups
    "--speed-centesimal", #keeps integer speeds that work well with detectors
    "--remove-loops", "true",
    "--junctions.map-signaled", "true" #creates proper TLS logic for complex Shanghai crossings
]
subprocess.run(cmd, check=True)
print("Network ready:", net_path)
