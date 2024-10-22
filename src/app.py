import jupyter
import os

def main():
    # Start jupyter notebook web server
    os.system("jupyter notebook --ip=0.0.0.0")
    
if __name__ == "__main__":
    main()