from pathlib import Path

# This points to the folder where this current script lives
my_dir = Path(__file__).parent
file_path = my_dir / "Eggs.txt"

if file_path.exists():
    print("Egg text found with pathlib!")
    

from pathlib import Path
Path("empty_egg_carton.txt").touch()