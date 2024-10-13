from queue import Queue;
from uuid import uuid4;
import time

queue = Queue();

def generate_request(user_input):
    if not user_input:
        print('User input is invalid. Please check and try again.');
        return; 
    
    queue.put({
            "id": uuid4(),
            "task": user_input,
            "success": False
        });

def process_request():    
    if not queue.empty():
        # process
        task = queue.get();
          
        print(f'Start processing task {task['task']}...'); 
        time.sleep(2);
        task['success'] = True;
        
        return f"Your task ID: '{task['id']}' and request '{task['task']}' has been processed";
    else:
        print('Queue is empty');
        
        
while True:
    user_input = input('Enter your request ');
    
    generate_request(user_input);
    print(process_request());