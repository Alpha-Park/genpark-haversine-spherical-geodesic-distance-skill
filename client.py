import math

class SphericalGeodesicCalculator:
    """Haversine spherical great-circle geodesic calculator."""
    def calculate_distance_km(self, lat1: float, lon1: float, lat2: float, lon2: float) -> dict:
        radius_km = 6371.0
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlam = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * (math.sin(dlam / 2.0) ** 2)
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(max(0.0, 1.0 - a)))
        distance = radius_km * c

        return {
            "origin": {"lat": lat1, "lon": lon1},
            "destination": {"lat": lat2, "lon": lon2},
            "distance_km": round(distance, 2)
        }
