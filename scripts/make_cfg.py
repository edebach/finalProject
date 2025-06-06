# scripts/make_cfg.py
import xml.etree.ElementTree as ET
from pathlib import Path

def make_sumocfg(scenario):
    root = ET.Element("configuration")
    ET.SubElement(root,"input", **{
        "net-file":"../../data/osm/shanghai.net.xml",
        "route-files":f"{scenario}.trips.xml"
    })
    ET.SubElement(root,"time", **{
        "begin":"0", "end":"10800", "step-length":"1"
    })
    out = Path(f"../scenarios/{scenario}/{scenario}.sumocfg")
    ET.ElementTree(root).write(out, encoding="utf-8", xml_declaration=True)
    return out
