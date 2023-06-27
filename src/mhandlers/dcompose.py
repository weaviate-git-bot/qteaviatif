import subprocess

def start_docker_compose(compose_file_path):
    try:
        # Run the docker-compose command
        subprocess.run(["docker-compose", "-f", compose_file_path, "up", "-d"], check=True)
        print("docker-compose up command executed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running docker-compose up command: {e}")
        return False


def stop_docker_compose(compose_file_path):
    try:
        # Run the docker-compose command
        subprocess.run(["docker-compose", "-f", compose_file_path, "down"], check=True)
        print("docker-compose up command executed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running docker-compose up command: {e}")
        return False
