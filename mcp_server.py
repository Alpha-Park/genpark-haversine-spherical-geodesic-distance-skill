import sys
import json
from client import SphericalGeodesicCalculator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "distance_km":
        c = SphericalGeodesicCalculator()
        return c.calculate_distance_km(params["lat1"], params["lon1"], params["lat2"], params["lon2"])
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
