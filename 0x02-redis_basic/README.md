iTo set up and complete the "0x02. Redis Basic" project, follow these detailed steps:

Prerequisites
Install Docker (if not already installed):

bash
Copy code
sudo apt-get update
sudo apt-get install -y docker.io
Pull the Redis Docker image:

bash
Copy code
sudo docker pull redis
Project Directory Structure
Create the project directory and necessary files:

css
Copy code
0x02-redis_basic/
│
├── README.md
├── Dockerfile
├── main.py
└── my_module.py
Step-by-Step Guide
1. Create a Dockerfile
This Dockerfile ensures the Redis server starts when the container runs.

Dockerfile
Copy code
# Use the official Redis image as the base image
FROM redis

# Start the Redis server
CMD ["redis-server"]
2. Build the Docker Image
Build the custom Redis image:

bash
Copy code
cd 0x02-redis_basic
sudo docker build -t custom-redis .
3. Run the Redis Container
Run a container from the custom image:

bash
Copy code
sudo docker run -d --name my-custom-redis-container custom-redis
4. Obtain the Redis Container's IP Address
Get the container's IP address to connect to it from your Python application:

bash
Copy code
sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-custom-redis-container
5. Create README.md
Document the project details:

markdown
Copy code
# Redis Basic Operations

This project demonstrates basic operations using Redis in Python and shows how to use Redis as a simple cache.

## Installation

1. Install Docker:
    ```bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    ```

2. Pull the Redis image:
    ```bash
    sudo docker pull redis
    ```

3. Build the custom Redis image:
    ```bash
    sudo docker build -t custom-redis .
    ```

4. Run the Redis container:
    ```bash
    sudo docker run -d --name my-custom-redis-container custom-redis
    ```

5. Get the Redis container's IP address:
    ```bash
    sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-custom-redis-container
    ```

## Usage

Run the main script to see Redis operations in action:
```bash
python3 main.py
python
Copy code

#### 6. **Create `my_module.py`**

Implement Redis interactions in this module:

```python
#!/usr/bin/env python3
"""
Module to perform basic Redis operations.
"""

import redis
from typing import Any, Optional

class RedisClient:
    """
    A simple Redis client to perform basic operations and caching.
    """
    def __init__(self, host: str, port: int = 6379, db: int = 0):
        """
        Initializes the Redis client.

        Args:
            host (str): Redis server hostname.
            port (int): Redis server port.
            db (int): Redis database number.
        """
        self.client = redis.Redis(host=host, port=port, db=db)

    def set(self, key: str, value: Any) -> bool:
        """
        Sets a key-value pair in Redis.

        Args:
            key (str): The key.
            value (Any): The value.

        Returns:
            bool: True if successful, False otherwise.
        """
        return self.client.set(key, value)

    def get(self, key: str) -> Optional[Any]:
        """
        Gets a value by key from Redis.

        Args:
            key (str): The key.

        Returns:
            Optional[Any]: The value, or None if key does not exist.
        """
        return self.client.get(key)

    def delete(self, key: str) -> bool:
        """
        Deletes a key from Redis.

        Args:
            key (str): The key.

        Returns:
            bool: True if successful, False otherwise.
        """
        return self.client.delete(key)
Replace host in the __init__ method with the IP address obtained from the container.

7. Create main.py
Use the RedisClient to perform basic operations:

python
Copy code
#!/usr/bin/env python3
"""
Main script to demonstrate Redis operations.
"""

from my_module import RedisClient

def main():
    """
    Main function to perform basic Redis operations.
    """
    redis_host = "your_redis_container_ip"  # Replace with actual IP
    redis_client = RedisClient(host=redis_host)

    # Set key-value pairs
    redis_client.set('name', 'Alice')
    redis_client.set('age', 30)

    # Get values
    name = redis_client.get('name')
    age = redis_client.get('age')
    print(f'Name: {name.decode("utf-8")}, Age: {age.decode("utf-8")}')

    # Delete a key
    redis_client.delete('name')
    print(f'Name after deletion: {redis_client.get("name")}')

if __name__ == '__main__':
    main()
Replace "your_redis_container_ip" with the actual IP address obtained from the container.

8. Ensure Code Style and Type Annotations
Check your code against pycodestyle and ensure all functions and methods are type-annotated.

bash
Copy code
pip3 install pycodestyle
pycodestyle main.py my_module.py
Testing and Verification
Run your main script to verify that the basic Redis operations work as expected:

bash
Copy code
python3 main.py
Summary
By following these steps, you will have completed the Redis basic operations project, using Docker to run Redis in a container and connecting to it from a Python application. You will have met all the requirements, including proper documentation and adherence to coding standards.







