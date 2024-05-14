import random

def generate_requests_file(file_path):
    with open(file_path, 'w') as file:
        for _ in range(1000):
            request = random.randint(0, 4999)
            file.write(str(request) + '\n')

if __name__ == "__main__":
    file_path = "requests.txt"
    generate_requests_file(file_path)
    print("requests.txt generated successfully.")
