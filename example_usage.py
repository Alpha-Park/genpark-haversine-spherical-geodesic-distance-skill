from client import SphericalGeodesicCalculator

def main():
    print("=== Haversine Spherical Geodesic Calculator ===")
    calc = SphericalGeodesicCalculator()
    # SF (37.7749, -122.4194) to LA (34.0522, -118.2437)
    res = calc.calculate_distance_km(37.7749, -122.4194, 34.0522, -118.2437)
    print("Geodesic Distance:", res)
    assert 550 < res["distance_km"] < 570

    print("Spherical Geodesic Calculator verified successfully!")

if __name__ == "__main__":
    main()
