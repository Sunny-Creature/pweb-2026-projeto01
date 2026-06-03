from django.shortcuts import render

# Create your views here.

# página inicial
def index(request):
    return render(request, 'website/index.html')

# página de personagens
def personagens(request):
    lista_personagens = [
        {
            "nome": "Monkey D. Luffy",
            "biografia": "Monkey D. Luffy é o protagonista e capitão dos Chapéu de Palha. Quando pequeno, comeu a Gomu-Gomu no Mi acreditando ser uma fruta comum e adquire um poder que faz o seu corpo ter características de borracha e consiga se esticar."
        },
        {
            "nome": "Roronoa Zoro",
            "biografia": "Após a morte da sua amiga de infância, Shimotsuki Kuina, Zoro continua com a promessa de se tornar o maior espadachim do mundo. É o primeiro membro da tripulação quando convencido pelo Luffy. Sua antiga profissão era de caçador de recompensas."
        },
        {
            "nome": "Usopp",
            "biografia": "É o atirador de elite dos Piratas do Chapéu de Palha em One Piece. Natural da Vila Syrup, ele sonha em se tornar um bravo guerreiro do mar como seu pai, Yasopp. Conhecido por sua covardia cômica e pontaria impecável, ele também assumiu a identidade secreta de 'Sogeking'."
        },
        {
            "nome": "Nami",
            "biografia": "Ela é uma ladra.",
        },
        {
            "nome": "Vinsmoke Sanji",
            "biografia": "Vinsmoke Sanji, conhecido como 'Perna Preta', é o cozinheiro dos Piratas do Chapéu de Palha. Nascido no North Blue como um príncipe do Reino Germa, ele abandonou sua família abusiva e encontrou seu caminho na culinária e nas artes marciais com o lendário pirata Zeff. Seu grande sonho é encontrar o mítico mar All Blue."
        },
        {
            "nome": "Tony Tony Chopper",
            "biografia": "Tony Tony Chopper é o médico dos Piratas do Chapéu de Palha em One Piece. Originalmente uma rena rejeitada por nascer com o nariz azul, ele comeu a Fruta Hito Hito no Mi, ganhando habilidades humanas. Após aprender medicina com o Dr. Hiriluk e a Dra. Kureha, ele se juntou a Monkey D. Luffy."
        },
        {
            "nome": "Nico Robin",
            "biografia": "Nico Robin é a arqueóloga dos Piratas do Chapéu de Palha em One Piece. Única sobrevivente da ilha de Ohara, ela é a única pessoa no mundo capaz de ler os Poneglyphs. Seu principal objetivo é encontrar o Rio Poneglyph e descobrir a verdadeira história do Século Perdido."
        },
        {
            "nome": "Franky",
            "biografia": "Franky, cujo nome verdadeiro é Cutty Flam, é o carpinteiro naval do bando dos Piratas do Chapéu de Palha em One Piece. Ele é um ciborgue excêntrico, conhecido pelo topete, óculos escuros e por sua famosa frase 'SUUUPER!'."
        },
        {
            "nome": "Brook",
            "biografia": "Brook, conhecido como o 'Soul King', é o músico e espadachim dos Piratas do Chapéu de Palha na obra One Piece. Ele é um esqueleto ressuscitado de 2,66 m de altura, famoso por sua cartola, bengala-espada, personalidade brincalhona e seu amor pela música."
        },
        {
            "nome": "Shanks",
            "biografia": "Shanks, conhecido como 'O Ruivo', é o capitão dos Piratas do Ruivo e um dos Quatro Imperadores (Yonko) que governam o Novo Mundo em One Piece. Ele é uma das figuras mais influentes do mundo, tendo iniciado a jornada de Monkey D. Luffy e servido como seu mentor."
        },
        {
            "nome": "Buggy",
            "biografia": "Buggy, o Palhaço Estrela, é um dos Quatro Imperadores do Mar em One Piece e líder da Cross Guild. Ele começou sua jornada como aprendiz no navio do Rei dos Piratas, Gol D. Roger. Apesar de seu poder de combate relativamente baixo, sua sorte absurda e conexões lendárias o transformaram em uma das figuras mais influentes do mundo."
        },
    ]
    context = {"personagens": lista_personagens,}
    return render(request, 'website/personagens.html', context)

# página sobre o site
def sobre(request):
    return render(request, 'website/sobre.html')