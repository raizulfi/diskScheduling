def read_requests_from_file(file_path):
    requests = []
    with open(file_path, 'r') as file:
        for line in file:
            request = int(line.strip())
            requests.append(request)
    return requests

def FCFS(initial_head, requests):
    total_head_movements = 0
    current_head = initial_head
    for request in requests:
        total_head_movements += abs(current_head - request)
        current_head = request
    return total_head_movements

def SCAN(initial_head, requests, direction='inward'):
    total_head_movements = 0
    current_head = initial_head
    requests.sort()
    if direction == 'outward':
        requests.reverse()
    for request in requests:
        total_head_movements += abs(current_head - request)
        current_head = request
    return total_head_movements

def C_SCAN(initial_head, requests):
    total_head_movements = 0
    current_head = initial_head
    requests.sort()
    idx = requests.index(initial_head)
    clockwise_requests = requests[idx:] + requests[:idx]
    anticlockwise_requests = requests[idx:] + requests[:idx]
    total_head_movements_clockwise = SCAN(initial_head, clockwise_requests, direction='outward')
    total_head_movements_anticlockwise = SCAN(initial_head, anticlockwise_requests, direction='inward')
    total_head_movements = min(total_head_movements_clockwise, total_head_movements_anticlockwise)
    return total_head_movements

def rearrange_SCAN(initial_head, requests):
    requests.sort()
    idx = requests.index(initial_head)
    return requests[idx+1:] + requests[:idx], requests[idx::-1]

def rearrange_C_SCAN(initial_head, requests):
    requests.sort()
    idx = requests.index(initial_head)
    clockwise_requests = requests[idx:] + requests[:idx]
    anticlockwise_requests = requests[idx:] + requests[:idx]
    return clockwise_requests, anticlockwise_requests[::-1]

def main():
    file_path = "requests.txt"  # Example file path
    requests = read_requests_from_file(file_path)

    initial_head = requests[0]  # Use the first request as the initial head position

    print("Task 1:")
    print("FCFS Head Movements (Original):", FCFS(initial_head, requests))
    print("SCAN Head Movements (Original):", SCAN(initial_head, requests))
    print("C-SCAN Head Movements (Original):", C_SCAN(initial_head, requests))

    print("\nTask 2:")
    print("FCFS Head Movements (Optimized):", FCFS(initial_head, requests))

    rearranged_SCAN_inward, rearranged_SCAN_outward = rearrange_SCAN(initial_head, requests)
    rearranged_C_SCAN_clockwise, rearranged_C_SCAN_anticlockwise = rearrange_C_SCAN(initial_head, requests)
    
    print("SCAN Head Movements (Optimized, Inward):", min(SCAN(initial_head, rearranged_SCAN_inward), SCAN(initial_head, rearranged_SCAN_outward)))
    print("C-SCAN Head Movements (Optimized, Clockwise):", min(C_SCAN(initial_head, rearranged_C_SCAN_clockwise), C_SCAN(initial_head, rearranged_C_SCAN_anticlockwise)))

if __name__ == "__main__":
    main()
