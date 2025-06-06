import osmnx as ox


ox.settings.use_cache = True     
ox.settings.log_console = True   

# … resto del codice (es. scaricare la rete di Shanghai) …
G = ox.graph_from_place("Shanghai, China",
                        network_type="drive",
                        simplify=False)

ox.io.save_graph_xml(G, filepath="shanghai.osm")


# Variant 2 – only central urban area (lighter)
# G = ox.graph_from_bbox(
#         north=31.30, south=31.10,
#         east=121.55, west=121.35,
#         network_type="drive",
#         simplify=False)
