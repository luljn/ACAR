# hooks.py

from PyInstaller.utils.hooks import collect_all


hiddenimports = collect_all('Fonts/font.ttf')
datas = [
    ('fonction_principale.py', '.'),
    ('classes.py', '.'),
    ('classe_1.py', '.'),
    ('auto_move.py', '.')
]