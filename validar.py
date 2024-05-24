import argparse
import os

from VRPTW import *


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Validador de soluciones para el problema de VRPTW')
    parser.add_argument('problem', type=str, help='Archivo de problema (en formato Solomon)')
    parser.add_argument('solution', type=str, default=False, help="Archivo de solución")
    return parser.parse_args()


def check_route(problem, line):
    route_customers, timestamps = line.split()[::2], line.split()[1::2]
    assert route_customers[0] == route_customers[-1] == '0', "Cada ruta debe comenzar y terminar en el DEPÓSITO."
    customers = []
    for c, t in zip(route_customers, timestamps):
        customer = list(filter(lambda x: x.number == int(c), problem.customers))[0]
        customers.append(customer)
        customer.is_serviced = True
        assert customer.ready_time <= float(t) < customer.due_date, f"Violación de tiempo para el cliente {c}"
    assert sum([x.demand for x in customers]) <= problem.vehicle_capacity, f"Violación de capacidad para la línea {line}"


def check_solution(problem: Problem, solution_file: str):
    with open(solution_file, 'r') as f:
        routes = f.readlines()
    assert len(routes) <= problem.vehicle_number, "Violación del número de vehículo"

    for route in routes:
        check_route(problem, route)
    assert all(map(lambda x: x.is_serviced, problem.customers)), "Cada cliente debe ser atendido."


if __name__ == '__main__':
    args = arguments()
    assert os.path.exists(args.problem), "Archivo de problema incorrecto"
    assert os.path.exists(args.solution), "Archivo de solución incorrecto"
    problem = SolomonFormatParser(os.path.abspath(args.problem)).get_problem()
    check_solution(problem, os.path.abspath(args.solution))
    print("Bien hecho.")
