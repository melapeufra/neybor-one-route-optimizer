from typing import List, Dict
from math import radians, sin, cos, sqrt, atan2
import argparse

try:
    import matplotlib.pyplot as plt
except Exception as e:
    plt = None

HOUSES = [
    #{"name": "Duden 26", "address": "Rue Egide Walschaerts 26, Saint-Gilles 1060", "lat": 50.826828311543565, "lon": 4.33677586917812, "is_airbnb": True},
    #{"name": "Louise 32", "address": "Rue Jourdan 32, Saint-Gilles 1060", "lat": 50.83428780731322, "lon": 4.354435782671721, "is_airbnb": True},
    #{"name": "Duden 3", "address": "Avenue Reine Marie-Henriette 3, Forest 1190", "lat": 50.82345878988992, "lon": 4.33436130965701, "is_airbnb": True},
    #{"name": "Congres 46", "address": "Rue de la Croix de Fer 46, Brussels 1000", "lat": 50.848541593328044, "lon": 4.365480126851019, "is_airbnb": True},
    #{"name": "Congres 22", "address": "Rue de la Tribune 22, Brussels 1000", "lat": 50.84854488903282, "lon": 4.365122150137942, "is_airbnb": True},
    {"name": "Ambiorix 46", "address": "Rue des Deux Tours 46, 1210 Saint-Josse-ten-Noode", "lat": 50.85105495407479, "lon": 4.3782560115086575, "is_airbnb": False},
    {"name": "Artan 112", "address": "Rue Artan 112, 1030 Schaerbeek", "lat": 50.85364680806313, "lon": 4.383660167330543, "is_airbnb": False},
    {"name": "Botanique 31", "address": "Chau. de Haecht 31, 1210 Saint-Josse-ten-Noode", "lat": 50.85592825310391, "lon": 4.367923365481105, "is_airbnb": False},
    {"name": "Botanique 42", "address": "Rue du Méridien 42, 1210 Saint-Josse-ten-Noode", "lat": 50.854565830029024, "lon": 4.369158338494917, "is_airbnb": False},
    {"name": "Brugman 53", "address": "Av. Louis Lepoutre 53, 1050 Ixelles", "lat": 50.81912136605574, "lon": 4.357256511506246, "is_airbnb": False},
   # {"name": "Chatelin 63", "address": "Rue de Florence 63, 1060 Saint-Gilles", "lat": 50.82881048643311, "lon": 4.35739712684958, "is_airbnb": False},
    {"name": "Colignon 31", "address": "Rue Herman 31, 1030 Schaerbeek", "lat": 50.86468744645891, "lon": 4.377417184523553, "is_airbnb": False},
    {"name": "Colignon 39", "address": "Rue Emmanuel Hiel 39, 1030 Schaerbeek", "lat": 50.86635253901819, "lon": 4.371428511509731, "is_airbnb": False},
    {"name": "Fernand 12", "address": "Rue Mercelis 12, 1050 Ixelles", "lat": 50.832579262484806, "lon": 4.3660458673289915, "is_airbnb": False},
    {"name": "Fernand 3", "address": "Rue du Viaduc 3, 1050 Ixelles", "lat": 50.832376723699724, "lon": 4.3676680961646195, "is_airbnb": False},
    {"name": "Flagey 16", "address": "Rue Maes 16, 1050 Ixelles", "lat": 50.831473175030396, "lon": 4.369378880821944, "is_airbnb": False},
    {"name": "Flagey 21", "address": "Rue du Serpentin 21, 1050 Ixelles", "lat": 50.82793441321475, "lon": 4.374789453835611, "is_airbnb": False},
    #{"name": "Flagey 33", "address": "Rue Wéry 33, 1050 Ixelles", "lat": 50.83133348701857, "lon": 4.3755055384932175, "is_airbnb": False},
    {"name": "Louise 13", "address": "Rue d'Ecosse 13, 1060 Saint-Gilles", "lat": 50.83328226728295, "lon": 4.352356296164707, "is_airbnb": False},
    {"name": "Louise 65", "address": "Rue Mercelis 65, 1050 Ixelles", "lat": 50.83107722398169, "lon": 4.363488094314956, "is_airbnb": False},
    #{"name": "Montgomery 17", "address": "Rue de la Duchesse 17, 1150 Woluwe-Saint-Pierre", "lat": 50.838650744291066, "lon": 4.406603980822448, "is_airbnb": False},
    {"name": "Parvis 4", "address": "Rue de la Filature 4, 1060 Saint-Gilles", "lat": 50.83203942132771, "lon": 4.345137138493248, "is_airbnb": False},
    {"name": "Leopold 1", "address": "Rue Vandenbroeck 1", "lat": 50.835676118178, "lon": 4.374911192465664, "is_airbnb": False},
    {"name": "Leopold 55", "address": "Rue du Chateau 55", "lat": 50.83131861580924, "lon": 4.380596035899892, "is_airbnb": False},
    {"name": "Neybor Office", "address": "Chaussée de Boondael 365, Ixelles 1050", "lat": 50.8177318, "lon": 4.3864221, "is_airbnb": False},
]

START_NAME = "Neybor Office"
END_NAME = "Neybor Office"

def haversine_km(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def pair_distance_km(a: Dict, b: Dict) -> float:
    return haversine_km(a["lat"], a["lon"], b["lat"], b["lon"])

def build_distance_matrix(items: List[Dict]) -> List[List[float]]:
    n = len(items)
    D = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = pair_distance_km(items[i], items[j])
            D[i][j] = D[j][i] = d
    return D

def nearest_neighbor_open(D: List[List[float]], start: int) -> List[int]:
    n = len(D)
    unv = set(range(n))
    route = [start]
    unv.remove(start)
    cur = start
    while unv:
        nxt = min(unv, key=lambda j: D[cur][j])
        route.append(nxt)
        unv.remove(nxt)
        cur = nxt
    return route

def route_length_open(D: List[List[float]], route: List[int]) -> float:
    return sum(D[route[i]][route[i+1]] for i in range(len(route)-1))

def route_length_cycle(D: List[List[float]], route: List[int]) -> float:
    if not route:
        return 0.0
    return route_length_open(D, route) + D[route[-1]][route[0]]

def two_opt_open_fixed_ends(route: List[int], D: List[List[float]]) -> List[int]:
    best = route[:]
    best_len = route_length_open(D, best)
    n = len(best)
    if n < 4:
        return best
    improved = True
    while improved:
        improved = False
        for i in range(1, n-2):
            for k in range(i+1, n-1):
                new_route = best[:i] + best[i:k+1][::-1] + best[k+1:]
                new_len = route_length_open(D, new_route)
                if new_len + 1e-12 < best_len:
                    best, best_len = new_route, new_len
                    improved = True
    return best

def find_index_by_name(houses: List[Dict], name: str) -> int:
    for i, h in enumerate(houses):
        if h["name"] == name:
            return i
    raise ValueError(f"House named '{name}' not found.")

def build_one_zone_route(houses: List[Dict]) -> List[int]:
    start_idx = find_index_by_name(houses, START_NAME)
    end_idx = find_index_by_name(houses, END_NAME)
    D = build_distance_matrix(houses)
    route = nearest_neighbor_open(D, start_idx)
    if route[-1] != end_idx:
        route = [i for i in route if i != end_idx] + [end_idx]
    route = two_opt_open_fixed_ends(route, D)
    return route, D

def print_zone(houses: List[Dict], route: List[int], D: List[List[float]]):
    cycle_len = route_length_cycle(D, route)
    print("=== Zone_1 ===")
    print(f"Stops (incl. cycle back to start): {len(route)} | Route (open): {len(route)} steps | Cycle length ~ {cycle_len:.2f} km")
    for i, idx in enumerate(route, start=1):
        h = houses[idx]
        print(f"{i:2d}. {h['name']}  [{h['address']}]")

def save_map(houses: List[Dict], route: List[int], out_png: str):
    if plt is None:
        print("matplotlib est requis pour générer la carte.")
        return
    xs = [houses[i]["lon"] for i in route]
    ys = [houses[i]["lat"] for i in route]
    plt.figure(figsize=(8,8))
    plt.plot(xs, ys, marker='o')
    for i, idx in enumerate(route, start=1):
        h = houses[idx]
        plt.text(h["lon"], h["lat"], f"{i}. {h['name']}", fontsize=8)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Zone unique — itinéraire de distribuer les bonbons dans toutes les maisons Neybor")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"Carte enregistrée: {out_png}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-png", type=str, default="one_zone_map.png", help="Chemin du PNG")
    args = parser.parse_args()

    route, D = build_one_zone_route(HOUSES)
    print_zone(HOUSES, route, D)
    save_map(HOUSES, route, args.out_png)

if __name__ == "__main__":
    main()
