from PIL import Image, ImageSequence

def diviser_gif(image_path, dossier_sortie, prefixe_nom):
    gif = Image.open(image_path)
    frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
    
    for i, frame in enumerate(frames):
        nom_image = f"{prefixe_nom}{i+1:03d}.tga"
        chemin_image = fr"{dossier_sortie}\{nom_image}"
        frame.save(chemin_image)

diviser_gif(r"Chemin d'acces a votre gif", r"Chemin d'acces a vos nouvelle texture", "NOM DE VOTRE TEXTURE") # Le nom de votre texture et par exemple: chevrolet
