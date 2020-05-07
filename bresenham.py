from PIL import Image, ImageDraw
#Image fornece uma classe com o mesmo nome que é usado para representar uma imagem PIL.
#ImageDrawfornece gráficos 2D simples para Image, criar e editar imagens.

def bresenhamLow(draw,x0,y0,x1,y1):
  dx = x1 - x0 #calcula tamanho de x (dx)
  dy = y1 - y0 #calcula tamanho de y (dy)
  
  yi = 1
  if dy < 0: #se dy for negativo
    yi = -1 
    dy = -dy #inverte dy

  p = 2*dy - dx #calcula a variavel de decisao p
  y = y0 #seta o valor de y igual ao valor inicial de y (y0)

  for x in range(x0,x1): #roda ponto a ponto pelo tamanho de x
    draw.point((x,y),0) #desenha o ponto
    if p >= 0: #se p >= 0, o próximo ponto será (x+1, y+1) e recalcula p= p + 2dy – 2dx
      y = y + yi 
      p -= 2*dx 
    p += 2*dy #se p < 0, o próximo ponto será (x+1, y) e recalcula p = p + 2dy

def bresenhamHigh(draw,x0,y0,x1,y1):
  dx = x1 - x0 #calcula tamanho de x (dx)
  dy = y1 - y0 #calcula tamanho de y (dy)
  
  xi = 1
  if dx < 0: #se dy for negativo
    xi = -1
    dx = -dx #inverte dx

  p = 2*dx - dy #calcula a variavel de decisao p
  x = x0 #seta o valor de x igual ao valor inicial de x (x0)

  for y in range(y0,y1): #roda ponto a ponto pelo tamanho de y
    draw.point((x,y),0) #desenha o ponto
    if p >= 0: #se p >= 0, o próximo ponto será (x+1, y+1) e recalcula p= p + 2dy – 2dx
      x = x + xi #acrescenta (x+1)
      p -= 2*dy #recalcula p
    p += 2*dx #se p < 0, o próximo ponto será (x+1, y) e recalcula p = p + 2dy

def bresenham(draw,x0,y0,x1,y1):
    dx = x1 - x0 #calcula tamanho de x (dx)
    dy = y1 - y0 #calcula tamanho de y (dy)
    
    if abs(dx) > abs(dy): #abs() retorna o valor absoluto
      bresenhamLow(draw,x0, y0, x1, y1)
    else:
      bresenhamHigh(draw,x0, y0, x1, y1)


im = Image.new('L',(100, 100),255) #cria uma nova imagem do tamanho 100px X 100px da cor branca(255)
draw = ImageDraw.Draw(im) #cria um objeto do tipo imagem

              #x0,y0,x1,y1
bresenham(draw,10,10,80,70) #reta horizontal (dx = 70,dy = 0)
bresenham(draw,10,10,80,70) #reta horizontal (dx = 70,dy = 0)
bresenham(draw,10,10,10,80) #reta vertival (dx = 0,dy = 70)
bresenham(draw,10,80,80,80) #reta horizontal (dx = 70,dy = 0)
bresenham(draw,80,10,80,80) #reta vertival (dx = 0,dy = 70)

im2 = im.resize((800,800)) #redimensiona a imagem utilizam a biblioteca ImageDraw
im2.show() #exibi a imagem criada
im2.save("bresenham.png") #salva a imagem no diretorio