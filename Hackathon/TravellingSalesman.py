"""Simple travelling salesman problem between cities."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import Graph


def create_data_model(graph_object):
    """Stores the data for the problem."""
    data = {}
    # distanceMatrix = Graph.Graph(postcodeList)
    data['distance_matrix'] = graph_object.getIncidence()
    data['numList'] = 1
    data['depot'] = 0
    return data

"""
def print_solution(manager, routing, assignment):
    print('Objective: {} miles'.format(assignment.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ,'.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)
"""

#function that should return a list of the route and a its distance
def print_solution(manager, routing, assignment) :
    index = routing.Start(0)
    route_distance = 0
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        return route, route_distance 

#AFTER TESTING - CHANGE FUNCTION MAIN TO 'travellingSalesmanAlgorithm(postcodesList)' where postcodesList is a list of postcodes  
def travellingSalesmanAlgorithm(graph_object):
    """Entry point of the program."""
    # Instantiate the data problem.
    # postcodeList = ["TN21 0TQ","RG1 6PF","RM11 2EH","S017 1AW","SO16 4UF","SO18 2NU","SO17 3RE","HS7 5PG","GL5 1JY","L22 7RA","OX14 5JZ","RG19 8BT","TN32 5BP"]
    data = create_data_model(graph_object)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['numList'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if assignment:
        return print_solution(manager, routing, assignment)[0]
