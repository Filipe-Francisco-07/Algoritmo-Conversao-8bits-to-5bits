def inserirImagem(arquivo):
    with open(arquivo, 'r') as f:
        cabecalho = f.readline().strip()
        dimensoes = f.readline().strip()
        maiorvalor = int(f.readline().strip())
        pixels = []
        for line in f:
            pixels.extend(map(int, line.split()))
    largura, altura = map(int, dimensoes.split())
    return cabecalho, largura, altura, maiorvalor, pixels

def write_pgm(arquivo, cabecalho, largura, altura, maiorvalor, pixels):
    with open(arquivo, 'w') as f:
        f.write(f"{cabecalho}\n{largura} {altura}\n{maiorvalor}\n")
        for i in range(altura):
            f.write(" ".join(map(str, pixels[i * largura:(i + 1) * largura])) + "\n")

def resize_image(pixels,maiorvalor):
    new_pixels = []
    for pixel in pixels:
        if(pixel * 1.2 <= maiorvalor):
            new_pixel = (pixel * 1.2)
            new_pixels.append(new_pixel)
        else:
            new_pixel = pixel
            new_pixels.append(new_pixel)
    return new_pixels

def resize_and_save(input_arquivo, output_arquivo):
    cabecalho, largura, altura, maiorvalor, pixels = inserirImagem(input_arquivo)
    new_pixels = resize_image(pixels,maiorvalor)
    write_pgm(output_arquivo, cabecalho, largura, altura, maiorvalor, new_pixels)

# Entrando com a imagem inicial
arquivo_entrada = 'imagem5bits.pgm'

# Criando imagem 20% de brilho
resize_and_save(arquivo_entrada, 'imagem20brilho.pgm')
