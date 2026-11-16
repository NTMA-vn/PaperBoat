from pathlib import Path

root = Path('c:/Users/Etudiant/Desktop/PaperBoatOriginal_apres_modifs/PaperBoatOriginal_apres_modifs')
for path in root.glob('*.py'):
    text = path.read_text(encoding='utf-8', errors='surrogateescape')
    path.write_text(text, encoding='utf-8', newline='\n')
    print(f'normalized: {path.name}')
