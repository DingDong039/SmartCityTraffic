def find_busiest_intersections(intersections):
    """
    This function takes a dictionary of intersections with vehicle counts
    and returns a list of intersections with the highest number of vehicles.
    
    Parameters:
    intersections (dict): A dictionary where keys are intersection names (str)
                          and values are the number of vehicles (int).
    
    Returns:
    list: A list of intersections (str) with the highest number of vehicles.
    """
    if not intersections:
        return []
    
    # Find the highest number of vehicles
    max_vehicles = max(intersections.values())
    
    # Return all intersections with the highest number of vehicles
    busiest_intersections = [name for name, count in intersections.items() if count == max_vehicles]
    
    return busiest_intersections

if __name__ == "__main__":
    intersections = {
        "A": 100,
        "B": 200,
        "C": 150,
        "D": 200
    }
    busiest = find_busiest_intersections(intersections)
    print(f"Busiest intersections: {busiest}")