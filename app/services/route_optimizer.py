import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from typing import List, Dict, Any
from app.schemas import LogisticsNode

def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

class LogisticsRouteService:
    @staticmethod
    def solve_cvrp(nodes: List[LogisticsNode], vehicle_capacity: float) -> Dict[str, Any]:
        num_nodes = len(nodes)
        if num_nodes < 2:
            return {"success": False, "message": "At least 2 nodes required to calculate route."}

        distance_matrix = []
        for i in range(num_nodes):
            row = []
            for j in range(num_nodes):
                if i == j:
                    row.append(0)
                else:
                    dist = haversine_km(nodes[i].lat, nodes[i].lng, nodes[j].lat, nodes[j].lng)
                    row.append(int(dist * 1.25 * 1000))
            distance_matrix.append(row)

        demands = [int(n.demand_kg) for n in nodes]

        manager = pywrapcp.RoutingIndexManager(num_nodes, 1, 0)
        routing = pywrapcp.RoutingModel(manager)

        def distance_callback(from_index, to_index):
            return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        def demand_callback(from_index):
            return demands[manager.IndexToNode(from_index)]

        demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
        routing.AddDimensionWithVehicleCapacity(
            demand_callback_index,
            0,
            [int(vehicle_capacity)],
            True,
            "Capacity"
        )

        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )

        solution = routing.SolveWithParameters(search_parameters)

        if not solution:
            return {"success": False, "message": "No feasible route found for current constraints."}

        route_sequence = []
        index = routing.Start(0)
        total_distance_meters = 0
        current_load = 0

        while not routing.IsEnd(index):
            node_idx = manager.IndexToNode(index)
            node_obj = nodes[node_idx]
            current_load += node_obj.demand_kg
            route_sequence.append({
                "step": len(route_sequence) + 1,
                "node_id": node_obj.id,
                "name": node_obj.name,
                "node_type": node_obj.node_type,
                "lat": node_obj.lat,
                "lng": node_obj.lng,
                "action": "PICKUP" if node_obj.demand_kg > 0 else ("START" if node_obj.demand_kg == 0 else "DELIVERY"),
                "load_change_kg": node_obj.demand_kg,
                "vehicle_load_kg": current_load
            })
            prev_index = index
            index = solution.Value(routing.NextVar(index))
            total_distance_meters += routing.GetArcCostForVehicle(prev_index, index, 0)

        start_node = nodes[0]
        route_sequence.append({
            "step": len(route_sequence) + 1,
            "node_id": start_node.id,
            "name": f"{start_node.name} (Return/End)",
            "node_type": start_node.node_type,
            "lat": start_node.lat,
            "lng": start_node.lng,
            "action": "COMPLETE",
            "load_change_kg": 0,
            "vehicle_load_kg": 0
        })

        return {
            "success": True,
            "total_distance_km": round(total_distance_meters / 1000.0, 1),
            "vehicle_capacity_kg": vehicle_capacity,
            "itinerary": route_sequence
        }
