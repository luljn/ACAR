pyinstaller --onefile --windowed --add-data "img/*.PNG;img" --add-data "img/*.png;img" --add-data "img/*.bmp;img" --additional-hooks-dir=. Main.py