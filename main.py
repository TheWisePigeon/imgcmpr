from PIL import Image
import imagehash
cutoff = 5
image1 = Image.open('images/homer.png')
image2 = Image.open('images/image.png')
image4 = Image.open('images/homer.png')

def imageComparator(model, images):
    scores, values= {}, []
    for img in images:
        score = imagehash.average_hash(model) - imagehash.average_hash(img)
        scores[f"{img.filename}"] = score
    
    sorted_values = sorted(scores.values())
    print(sorted_values)
    sorted_dict = {}
    for i in sorted_values:
        for k in scores.keys():
            if scores[k] == i:
                sorted_dict[k] = scores[k]
                break
    return sorted_dict
    
print(imageComparator(image1, [image2, image4]))

