from PIL import Image
image = Image.open("images/FIFA-World-Cup-Winner.gif")
image = image.resize((500,350),Image.ANTIALIAS)
image.save(fp="images/FIFA-World-Cup-Winner.gif")