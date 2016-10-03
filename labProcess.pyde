caminho = color(200, 100, 0)
parede = color(0, 100, 200)
quadTam = 50
scrSize = 500
lab = []
dimMatriz = 10
def setup():
    size(scrSize, scrSize)
    background(150)
    frameRate(12)
    global reader
    global endfile
    endfile = False
    reader = createReader("lab30x30.txt")
    dados = reader.readLine().split()
    dimMatriz = int(dados[0])
    lab = [[] for x in range(dimMatriz)]
    
def draw():
    #le todas as linhas
    global endfile
    global lab
    lab = [[] for x in range(dimMatriz)]
    while endfile != True:
        line = reader.readLine()
        if line is None:
            endfile = True
        for y in range(0, dimMatriz):
            line = reader.readLine()
            print line
            if line is not None:
                lab[y] = line.split()
    for i in range (0, scrSize/quadTam):
        for j in range (0, scrSize/quadTam):
            #print len(lab[i])
            #fill(caminho if lab[j][i] == '1' else parede)
            rect(i*quadTam, j*quadTam, quadTam, quadTam)
        