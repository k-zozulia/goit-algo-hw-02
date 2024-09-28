import queue
import random
import time

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1000, 9999)  
    request_data = f"Request {request_id}"
    request_queue.put(request_data)
    print(f"Added {request_data} to the queue.")


def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Processing {request_data}...")
        time.sleep(2) 
        print(f"{request_data} processed.\n")
    else:
        print("The queue is empty, no requests to process.\n")

def main():
    try:
        while True:
            generate_request()

            process_request()

            time.sleep(3)
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()