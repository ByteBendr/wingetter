import subprocess

def install_dependencies():
    try:
        with open('requirements.txt') as file:
            requirements = file.read().splitlines()

        for requirement in requirements:
            subprocess.run(["pip", "install", requirement], check=True)
        
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing dependencies: {e}")

if __name__ == "__main__":
    install_dependencies()
