# scripts/run_batch.py
import subprocess, itertools, pathlib, datetime, os, json

scenarios = ["base","peak","event"]
reps      = range(5)           # five seeds per scenario
sumo_bin  = "sumo"             # or sumo-gui

for sc,rep in itertools.product(scenarios,reps):
    sce_path = f"../scenarios/{sc}/{sc}.sumocfg"
    log_dir  = pathlib.Path(f"../outputs/{sc}/run{rep}")
    log_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sumo_bin, "-c", sce_path,
        "--seed", str(rep),
        "--tripinfo-output", str(log_dir/"tripinfo.xml"),
        "--netstate-dump",   str(log_dir/"netstate.xml"),
        "--summary-output",  str(log_dir/"summary.xml")
    ]
    subprocess.run(cmd, check=True)
