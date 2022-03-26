import discord
import random
import time
from discord.ext import commands


class sorteio(commands.Cog):
    cara = None
    quant = None
    nvl = None

    niveis = ["Calamitoso123",
              "Horrível", "Horrível", "Horrível",
              "Muito Ruim", "Muito Ruim", "Muito Ruim", "Muito Ruim", "Muito Ruim",
              "Ruim", "Ruim", "Ruim", "Ruim", "Ruim", "Ruim", "Ruim", "Ruim",
              "Normal", "Normal", "Normal", "Normal", "Normal", "Normal", "Normal", "Normal", "Normal", "Normal",
              "Normal", "Normal", "Normal", "Normal", "Normal",
              "Bom", "Bom", "Bom", "Bom", "Bom", "Bom", "Bom",
              "Muito Bom", "Muito Bom", "Muito Bom", "Muito Bom", "Muito Bom",
              "Épico", "Épico", "Épico",
              "Lendário123", "Lendário123",
              "Místico"]

    porcentagens = [round((niveis.count("Calamitoso123") / len(niveis)) * 100, 2),
                    round((niveis.count("Horrível") / len(niveis)) * 100, 2),
                    round((niveis.count("Muito Ruim") / len(niveis)) * 100, 2),
                    round((niveis.count("Ruim") / len(niveis)) * 100, 2),
                    round((niveis.count("Normal") / len(niveis)) * 100, 2),
                    round((niveis.count("Bom") / len(niveis)) * 100, 2),
                    round((niveis.count("Muito Bom") / len(niveis)) * 100, 2),
                    round((niveis.count("Épico") / len(niveis)) * 100, 2),
                    round((niveis.count("Lendário123") / len(niveis)) * 100, 2),
                    round((niveis.count("Místico") / len(niveis)) * 100, 2)]

    calamitoso = [["Maldição do Buda", ""], ["Marca da Maldição", "Um Símbolo cravado em alguma parte do seu corpo com uma cicatriz. Ele atrai calamidades, azar e grandes desgraças."],
                  ["Arma/Artefato Poderoso", "Você é encarnado como um artefato com poderes, cujos vão depender das outras roletas."],
                  ["Imortal", "Você é imortal. Esse poder ocupa o espaço duas roletas."], ["Mugen", "Você é mais que esquizofrênico ou maluco. Nos momentos mais importantes você tem delírios "
                            "que são como sonhar acordado. Tu pode passar a pensar que é um dragão faminto por vidas ou simplesmente ficar paralizado assistindo formas geométricas impensáveis "
                            "passando em sua frente. Por ser aleatório, talvez seja benéfico em algumas situações."], ["Alagoinha?", "Sua campanha se passa em um mundo separado dos outros "
                                                                                                                                     "jogadores e é bem pior que a deles diga-se de passagem."],
                  ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."], ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."]]


    horrivel = [["Doença Grave", "uma doença muito grave ou fatal que deixa o paciente dela em estado de enfermidade e fraqueza"],
                ["Parasita", "Há um parasita dentro de você se alimentando do seu corpo e/ou mente, podendo até ter consciência, tentar assumir o controle, etc."],
                ["Aleijamento De vários membros/Paraplegia", "Você não tem um ou mais braços ou pernas"], ["Benção da Kofuku", "seu azar assusta até os deuses."],
                ["Zumbi", ""], ["Fobia frequente", "Você é um morto-vivo, sem tato você não sente nenhuma dor nem toque. Seu corpo morto é super frágil e você é de fato imortal podendo "
                                                   "recosturar todas as partes do seu corpo. Você se manterá vivo enquanto seu cérebro estiver inteiro e seu corpo estiver gelado."],
                ["Cegueira", ""], ["Paranoia", ""], ["Esquizofrenia", ""],
                ["Absoluta Múltipla Escolha", "Do nada você se vê obrigado a escolher fazer uma ação extremamente idiota de 2 ou mais opções, caso contrário sua cabeça explode. Só que acontece "
                                              "em situações um pouco piores..."]]


    muito_ruim = [["Aleijamento de um dos membros", "Você não tem um braço ou perna"],
                  ["Deficiência Mágica", "Você é incapaz de se conectar com mana e portanto, incapaz de realizar feitiços."],
                  ["Fraqueza ao Sol", "Durante o dia você fica extremamente fraco e muito tempo em contato com a luz solar pode até mesmo te matar"],
                  ["Deficiência de sentidos", "Surdez, mudez, sem tato"], ["Calcanhar de Aquiles", "Se o seu calcanhar sofrer um ferimento forte você morre 🤪 ."],
                  ["Man eater", "Sempre que você sente fome a primeira coisa que vem na sua mente é carne humana, você é capaz de saciar sua fome com comida normal mas sempre existirá uma "
                                "vontade imensa e impulsos quase inparáveis de comer a pessoa na sua frente."],
                  ["Hemofílico", "Você tem hemofilia, uma doença que faz com que você sangre do nada e seus feriemntos sangram por muito mais tempo, são muito mais difíceis de curar e tem "
                                 "grandes chances de reabrir."],
                  ["Mesmo de sempre", "Todos os outros resultados da roleta são anulados (inclusive os ruins). Você não possui nenhuma caracteristica diferente."],
                  ["Fobia comum", ""], ["Fuga", ""],
                  ["Absoluta Múltipla Escolha", "Do nada você se vê obrigado a escolher fazer uma ação extremamente idiota de 2 ou mais opções, caso contrário sua cabeça explode."],
                  ["Macaquice aguda", "Você se vê obrigado a explorar o mapa todo."]]


    ruim = [["Problemas de saúde", ""], ["Defeitos na aparência", ""],
            ["Tentação do dragão", "O pecado da ira faz parte de você, você está sempre possuído por um imenso ódio e a coisa mais simples deixa seus nervos á flor da pele."],
            ["Tentação da serpente", "Você transborda de inveja por qualquer pessoa conhecendo ela ou não. Você nunca será feliz enquanto essas pessoas possuírem mais riquezas, "
                                     "conquistas, popularide que você."],
            ["Tentação da raposa", "Tudo tem que estar na sua posse. Você só se sente feliz adquirindo um novo artefato ou então tomando pra si algo que alguém possua. Será incapaz "
                                   "de encontrar felicidade enquanto não for dono do mundo inteiro."],
            ["Tentação do urso", "Você tem uma preguiça sem precedentes. Se sua mãe te pedir pra lavar a louça é mais fácil uma pedra lavar os prato doq vc levantar do chão gelado. "
                                 "Nem com tiroteio você se abaixa. Você é preguiçoso pra caralho e não consegue impedir isso."],
            ["Tentação do bode", "A sua maldição é a luxúria. Você é incapaz de contar seus impulsos e desejos carnais. Só de pensar em Atos libidinosos você se contorcerá de tesão até "
                                 "que se alivie 😉 Você é a pessoa mais pervertida e tarada que já existiu."],
            ["Tentação do javali", "Mai jesus uai, não da ora comer junto contigo não. Você é o cara mais guloso do planeta. Tu come até a mesa nessa porra, devora tudo que tiver até "
                                   "ficar tão redondo que parecem que usaram um compasso e bebe tanto que se desse morria de overdose de cachaça."],
            ["Tentação do leão", "Você é o cara mais insuportável, arrombado e ignorante que existe. É quase impossível ficar ao seu lado de tão nojento que você é. O seu orgulho é "
                                 "tão grande que você acha que todo o resto do mundo exceto você é feio, ínfimo, lixo, podre, fedorento e fraco. Na sua cabecinha, melhor que você só dois de você."],
            ["Nanismo", "ALA O ANÃO KKKKKKKKKKKKKKKKKK"],
            ["Albinismo", "Você não possui melanina, provocando a cor doferenciada nos seus olhos e cabelos esbranquiçados. Uma pessoa albina tem problemas ao ficar exposta muito tempo no sol "
                          "por sua pele ser muito desprotegida contra seus raios."],
            ["Catarata", "Você tem catarata e piora de tempos em tempos. Obviamente prejudica sua visão."],
            ["Rock'n Roll", "Você é surdo de um ouvido ou tem a audição muito prejudicada por ter escutado muito musica alta na vida passada."],
            ["Fragmentado", "Você tem crise de personalidade e é no mínimo duas pessoas no mesmo corpo."],
            ["Bilu Tetetis", "Quando você pensa demais, chega uma hora que você percebe que não vai mais conseguir e então se vê fazendo algo extremamente estúpido"], ["Fobia incomum", ""],
            ["Covardia", ""], ["Mal cheiro", ""], ["Megalomania", ""], ["Gigantismo", ""], ["Dislexia", ""], ["Distraído", ""], ["Obsessão/Compulsão", ""], ["Penis preto", ""]]


    bom = [["Ui que delícia", "Você é bonito até demais"], ["Shitfinder", "a capacidade de achar algo ou alguém que você conhece até uma certa distância"],
           ["Hiperflexibilidade", "você é capaz de mover todas as juntas do seu corpo, conseguindo fazer coisas e posições pertubadoras e fodas que não deveriam ser possíveis (pode pensar "
                                  "no inosuke de demon slayer como exemplo caso n tenha entendido)"],
           ["Olhos de águia", "Você tem verdadeiros olhos de águia, do alto de um cume, poucas coisas escapam da sua visão."],
           ["Audição de ouro", "Sua audição é extremamente avançada. Você é capaz de escutar um alfinte caindo no chão há 100 metros de distância e consegue diferenciar os passos de uma "
                               "galinha em meio a passagem de uma manada de búfalos."],
           ["Olhos de artrópode", "Sua visão é repartida em várias vezes em realinhadas em uma unica imagem no ceu cérebro, dando a você uma visão muito mais rápida (mais frames/segundo) e um "
                                  "senso muito maior de profundidade."],
           ["Visão 360º", "Você possui olhos esbugalhados que lhe permitem enxergar 360° em volta docê."], ["Asas", "Você tem asas e pode voar"],
           ["Utensílio bom", "Você possui algum objeto, instrumento, utensíliso etc. Bom do seu mundo."],
           ["Médium", "Você é capaz de ver espíritos. Muitas vezes eles podem vagar por ai e ser bastante inconvenientes, porém, muitas vezes eles podem dar dicas e guiá-lo inconscientemente. "
                      "Isto, é claro, para os espíritos 'comuns' que vagam sobre a terra."],
           ["Veneno", "Você produz um veneno relativamente forte"]]


    muito_bom = [["Luminus", "capacidade de formar projeções de luz"], ["Fix", "poder de fixar poderes a lugares ou coisas após sua realização"],
                 ["Som", "a capacidade de modificar ondas sonoras."], ["Metamorfose", "Você é capaz de mudar sua forma para a forma de uma besta mais poderosa"],
                 ["Sangue quente", "Você se torna muito mais forte durante o dia, principalmente sob o sol. Além disso, você adquiri uma grande resistência a calor."],
                 ["Sangue sombrio", "Você se torna muito mais forte durante a noite, principalmente sob o luar. Além disso, você adquiri uma grande resistência a baixas temperaturas."],
                 ["Coordenação motora divina", "Você tem perfeito controle sobre seu corpo, é capaz de fazer quase tudo que pensa com ele garantindo a você uma grande facilidade e talento "
                                               "para diversas atividades físicas como artes marcias e esportes."],
                 ["Mutante", "Você possui um ou mais membros e órgãos (exceto coração e cérebro) do seu corpo em maior número que deveria (ex: 4 braços ou 4 olhos)."],
                 ["O Enganador", "Você é capaz de transformar seu corpo no corpo de qualquer ser vivo que você ver, porém, com a sua capacidade física. Você também consegue transformar "
                                 "objetos em outros objetos sem modificar sua capacidade física e etc."],
                 ["Utensílio muito bom", "Você possui algum objeto, instrumento, utensíliso etc. Muito bom do seu mundo."],
                 ["Artesão", "Existe uma pessoa no mundo caoaz de se transformar em uma arma, e você é a pessoa escolhida pra ser a sua dupla perfeita. Só você combina com o jeito dela e é "
                             "capaz de ressonar sua alma para ativar seus poderes. (Caso outro jogador aceite ser uma arma, essa característica se torna épica)"],
                 ["Zetsu", "Parte do seu corpo é formado por uma entidade estranha. Mas ela é foda 👍"], ["Estigmazin", ""],
                 ["Politicamente (Humanamente também) incorreto", "Você tem um escravo. 🙃"],
                 ["Praga", "Você é um cara peçonhento. No sentido de veneno mesmo, você produz uma substância tóxica bem forte."]]

    epico = [["Força sobrenatural", "Zaraki."], ["Poltergeist", "capacidade de mover tudo ao seu redor com força mental"],
             ["Estigma", "você pode realizar feitiços de um único tipo poderoso de magia ao único utilizando apenas sua mana."],
             ["ahh... WIRE!", "Jesse, cabo, fios, elemento"], ["Arsenal", "a capacidade de invocar um arsenal de armas de fogo e munição de outro mundo que não existem neste."],
             ["Verminose", "Controle sobre vermes especiais"],
             ["Hipervida", "as células do seu corpo se regeneram a uma velocidade absurda além de viverem muito mais tempo que qualuqer outra, dessa forma, alguém com esse poder "
                           "raramente morrerá de velhice."], ["Familiar", "Você possui uma ou mais bestas mágicas sob o seu comando."],
             ["Filho abençoado", "Você herdou um grande poder familiar ou é um filho humanoide de uma besta poderosa"],
             ["Stylestealer", "Se alguém que você teve uma luta justa morrer, o estilo de luta desta pessoa será incorporado a você como se fossem habilidades e poderes."],
             ["Protótipo mutante", "(Metamorfose + Man eater)\nVocê possui células mutantes capazes de se multiplicar rapidamente, dando origem e externalizando um ou mais membros e "
                                   "órgãos mortais fortes, flexíveis e até afiados com um aspecto assustador. Em troca, para manter seu corpo vivo e para para produzir essas células é "
                                   "necessário comer carne humana. 'Me diga então, diga então, como fiquei assim'."],
             ["Ira de Asura", "(Mutante + Tentação do Dragão)\nQuanto mais puto mais forte e poderoso você fica."],
             ["Gigantismo", "Você fica gigante e bem mais forte."],
             ["Kamescale", "Você é capaz de transformar grande parte do seu corpo no que você tocar, como metais. Você pode também pode criar novas partes conectadas ao seu corpo feitas "
                           "do material que você tocou. Você pode voltar ao normal quando quiser, suas materializações também vão sumir."],
             ["Locustatum", "Você é capaz de trocar de lugar com qualquer coisa que você ver."],
             ["Legado Agatsuma", "(Covardia + Fuga)\nAo sofrer um acesso de Fuga, Sinapses ocorrem no cérebro do seu personagem liberando um potencial secreto e absurdo. Você alcança um "
                                 "estado de concentração e inspiração que ninguém jamais seria capaz de alcançar."],
             ["Tamashi no Rinku", "Ao ser reencarnado seu corpo e mente se tornaram abrigo de um espírito estranho com poderes misteriosos. Graças a sua conexão com esse espírito, ele é "
                                  "capaz de se materializar no mundo exterior através de você como uma arma, assim como você pode ser capaz de usar seus poderes."],
             ["Artesão", "Caso outro jogador não aceite ser sua arma, você pode roletar épico novamente."],
             ["Arma do Shinigami", "Pra você ter essa característica alguém precisa aceitar ser seu mestre ou você aceitar ser arma de alguém. Caso contrário rolete épico de novo."],
             ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."], ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."]]

    lendario = [["Besta lendária", "(Metamorfose + Familiar)\nVocê controla ou possui o poder de uma besta lendária poderosíssima."],
                ["Psycho", "(Poltergeist + Shitfinder)\nO psycho aprimora ambos poderes a um nível extraordinário, podendo agora entra na mente de seres vivos, aumentando a área de pesquisa "
                           "e com forças mentais muito mais poderosas."], ["Relíquia lendária", "Arma/Artefato exclusivo com um imenso poder"],
                ["Visão do futuro", "Um poder ocular capaz de ver o futuro próximo ou longínquo."], ["Olho da ignorância", "Poder ocular que elimina outros poderes com o olhar"],
                ["Esferas de Jeera", "Você possui um conjunto infinito de esferas negras com auras roxas capazes de assumir qualquer forma."],
                ["Linhagem vampírica", "(Sangue sombrio + Albinismo/Fraqueza ao sol)\nVocê é um vampiro. Um ser imortal que se alimenta de sangue e possui capacidades físicas e mágicas "
                                       "extraordinárias, além de seus outros segredos posses. Vampiros raramente possuem grandea traços de emoção e só podem ser mortos através da luz do sol, "
                                       "artefatos abençoados ou o corpo totalmente desintegrado."],
                ["Herdeiro sombrio", "(Sanguem sombrio + Filho Abençoado)\nVocê é descendente de algum dos principais kamis ou youkais poderosos que faziam parte do lendário Hyakki Yakou, "
                                     "podendo ser também o seu legado."],
                ["Mana ruler", "Você é um ser capaz de produzir sua própria mana, mas não só isso, sua mana é pura e em tanta quantidade que você é capaz de externar dar forma a sua mana, "
                               "podendo utilizá-la para inúmeros propósitos."], ["Olhos de Hórus", "(Stylestealer + Olhos de Águia)\nVocê icorpora em si todos os poderes, feitiços e "
                                                                                                   "capacidades que você olhar enquanto estiver olhando para eles. Todos eles serão "
                                                                                                   "melhorados em você, superando o original. 'tenho os olhos de um DEEEEEEEEEEEEEUS e eu "
                                                                                                   "posso ver, que AGORA VIRA MEEEEEEEEUUUU O SEU PODER, NÃO POSSO DEIXAR O DESTINO DOS MEUS "
                                                                                                   "FILHO NA SUA MAAAAAOOO, ADAAAAOOOO, ADAAAAOOOO, ADAAAAAAAAAOOOOOO'."],
                ["Accelerator", "Através dos vetores, você consegue mudar a direção e magnitude de tudo que toca."],
                ["Tamashi no Rinku", "Ao ser reencarnado seu corpo e mente se tornaram abrigo de um espírito estranho com poderes misteriosos. Graças a sua conexão com esse espírito, ele "
                                     "é capaz de se materializar no mundo exterior através de você como uma arma, assim como você pode ser capaz de usar seus poderes."],
                ["E-Escravo😳 👉 👈 ", "É... Seu escravo é um reencarnado também?"], ["Estigma Duplo", ""],
                ["One for All", "(Força Sobrenatural + Filho Abençoado)\nÉ, All Might, eu estou aqui!"],
                ["Deus do novo mundo", "Desce Bofe, a Caderneta do Cabrunco."], ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."],
                ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."]]

    mistico = [["Senhor das almas", ""], ["O Tirano", "(3 Lendários ou mais)\nO poder de estar acima de tudo como um verdadeiro soberano."],
               ["Dado do Destino", "Um conjunto de dados onde ao serem jogados o seu resultado pode gerar absolutamente qualquer coisa, seja ela boa ou ruim."],
               ["Controle temporal", ""], ["Filho do sol", "(Sangue quente + Filho abençoado)\nVocê foi feito a imagem, semelhança e poder do sol. De dia você é "
                                                           "invencível e onipotente. Mas não se engane, seu poder a noite ainda é colossal."],
               ["Arsenal celestial infinito", "(Arsenal + ui que delicia/Relíquia lendária/Gilgamesh)\nIs that a fucking fate reference?"],
               ["Jardim do Éden", "(Olhos de Hórus + Filho abençoado)"], ["Temor do tremor", "Você possui a habilidade de produzir e controlar vibrações. Te possibilitando vibrar tudo, "
                                                                                             "desde o próprio ar até o próprio corpo. É ainda possível criar tremores como os provocados por "
                                                                                             "placas tectônicas. (É, SEM PERDER A FÉ, MAIS FORTE QUE A MARÉ, ATÉ MORRER DE PÉ)"],
               ["One Punch Man", "(Força Sobrenatural + One For All + Defeitos na Aparência [calvo ou careca])"],
               ["Iluminação", "Você é o iluminado."], ["Imortal", "Você é imortal. Esse poder ocupa o espaço duas roletas."],
               ["Estigma Quebrado", "Estigma já virou tatuagem pra você. Você tem mais de 2 Estigmas e todo eles são extremamente quebrados."],
               ["Kamisama", "Você não reencarnou como uma divindade, mas é uma divindade que reencarnou. 'Um Deus sempre existirá enquanto alguém nele acredita.'"],
               ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."], ["Único", "Você possui um poder novo épico exclusivo seu que não está nessa lista."]]

    def __init__(self, client):
        self.client = client

    def definirPote(self):
        if self.nvl.lower() == "calamitoso":
            for i in range(self.quant):
                self.calamitoso.append([str(self.cara), ""])
        if self.nvl.lower() == "horrivel":
            for i in range(self.quant):
                self.horrivel.append([str(self.cara), ""])
        if self.nvl.lower() == "muito ruim":
            for i in range(self.quant):
                self.muito_ruim.append([str(self.cara), ""])
        if self.nvl.lower() == "ruim":
            for i in range(self.quant):
                self.ruim.append([str(self.cara), ""])
        if self.nvl.lower() == "bom":
            for i in range(self.quant):
                self.bom.append([str(self.cara), ""])
        if self.nvl.lower() == "muito bom":
            for i in range(self.quant):
                self.muito_ruim.append([str(self.cara), ""])
        if self.nvl.lower() == "epico":
            for i in range(self.quant):
                self.epico.append([str(self.cara), ""])
        if self.nvl.lower() == "lendario":
            for i in range(self.quant):
                self.lendario.append([str(self.cara), ""])
        if self.nvl.lower() == "mistico":
            for i in range(self.quant):
                self.mistico.append([str(self.cara), ""])



    def sortearNivel(self):

        #SORTEANDO O NIVEL
        return (self.niveis[random.randint(0, len(self.niveis) - 1)])

    def sortearCara(self, nvl):

        #SORTEANDO O CARAC, E SEPARANDO SUA COR
        if nvl == 3:
            retornar = self.bom[random.randint(0, len(self.bom) - 1)]
            retornar.append(0x32CD32)
            return (retornar)
        elif nvl == 4:
            retornar = self.ruim[random.randint(0, len(self.ruim) - 1)]
            retornar.append(0xCD5C5C)
            return (retornar)
        elif nvl == 5:
            retornar = self.epico[random.randint(0, len(self.epico) - 1)]
            retornar.append(0x4B0082)
            return (retornar)
        elif nvl == 7:
            retornar = self.mistico[random.randint(0, len(self.mistico) - 1)]
            retornar.append(0xFFD700)
            return (retornar)
        elif nvl == 8:
            retornar = self.horrivel[random.randint(0, len(self.horrivel) - 1)]
            retornar.append(0x8B4513)
            return (retornar)
        elif nvl == 9:
            retornar = self.muito_bom[random.randint(0, len(self.muito_bom) - 1)]
            retornar.append(0x4169E1)
            return (retornar)
        elif nvl == 10:
            retornar = self.muito_ruim[random.randint(0, len(self.muito_ruim) - 1)]
            retornar.append(0xA0522D)
            return (retornar)
        elif nvl == 11:
            retornar = self.lendario[random.randint(0, len(self.lendario) - 1)]
            retornar.append(0xFFA500)
            return (retornar)
        elif nvl == 13:
            retornar = self.calamitoso[random.randint(0, len(self.calamitoso) - 1)]
            retornar.append(0x000000)
            return (retornar)

    @commands.command()
    async def roll(self, ctx):
        return

    @commands.command()
    async def help(self, ctx):
        return

    @commands.command()
    async def change(self, ctx):
        return

    @commands.command()
    async def quant(self, ctx):
        return

    @commands.command()
    async def nivel(self, ctx):
        return

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content[0:7] == "=change":
            if message.author.id == 321636223581945856:
                channel = message.channel
                msg = message.content[8:]
                self.cara = msg
                await channel.send(f"Você deseja criar o nível **{self.cara}** na roleta! Quantas vezes devo adicioná-lo?\nDigite '=quant [Numero de vezes na roleta]'")

        if message.content[0:6] == "=quant":
            if message.author.id == 321636223581945856:
                channel = message.channel
                self.quant = message.content[7:]
                await channel.send(f"Você irá colocar a palavra **{self.cara}**, **{self.quant}** vezes no pote!\nDigite '=nivel [Nível em que **{self.cara}** estará]'")

        if message.content[0:6] == "=nivel":
            if message.author.id == 321636223581945856:
                channel = message.channel
                self.nvl = message.content[7:]
                self.definirPote()
                await channel.send(f"Você irá colocar a palavra **{self.cara}**, **{self.quant}** vezes no pote **{self.nvl}**!")

        #ENVIANDO O =ROLL
        if message.content[0:5] == "=roll":
            author = message.author
            channel = message.channel
            nivel = self.sortearNivel()

            #AJUSTANDO O NIVEL PARA SER ENVIADO NO CHAT
            if len(str(nivel)) > 10:
                nivel = nivel[:-3]

            #ENVIANDO E APAGANDO O GIF
            gif = await channel.send(
                "https://cdn.discordapp.com/attachments/942175131835457596/942496059345748109/ezgif.com-gif-maker_28.gif")
            time.sleep(2.5)
            await gif.delete()
            time.sleep(0.5)

            #ENVIANDO O NIVEL DIFERENTE DE NORMAL
            if nivel != "Normal":
                embed = discord.Embed(title=f"Roleta de {str(author)[:-5]}",
                                      description=f"Nível selecionado: **{nivel}**\n\nAgora, iremos ver qual característica você irá receber!",
                                      color=0xDCDCDC)
                await channel.send(author.mention, embed=embed)

                #ENVIANDO O GIF
                time.sleep(1)
                gif = await channel.send(
                    "https://cdn.discordapp.com/attachments/942175131835457596/942496059345748109/ezgif.com-gif-maker_28.gif")

                #APAGANDO O GIF
                time.sleep(2.5)
                await gif.delete()
                time.sleep(0.5)

                #DEFININDO O CARAC
                if nivel == "Calamitoso" or nivel == "Lendário":
                    nivel = str(nivel + "123")
                carac = self.sortearCara(len(nivel))


                #ENVIANDO O CARAC
                embed = discord.Embed(title=f"Característica do(a) {str(author)[:-5]}",
                                      description=f"A característica que você recebeu foi: **{carac[0]}:**\n\n*{carac[1]}*",
                                      color=carac[2])
                await channel.send(author.mention, embed=embed)

            #ENVIANDO O CARAC NORMAL (NO NORMAL O PLAYER DECIDE)
            elif nivel == "Normal":
                embed = discord.Embed(title=f"Roleta de {str(author)[:-5]}",
                                      description=f"Nível selecionado: **{nivel}**\n\nAgora, escolha a sua característica!\n\nVocê pode ver as opções no canal <#923416913177112626>!")
                await channel.send(author.mention, embed=embed)

        #MENSAGEM DO =HELP
        if message.content[0:5] == "=help":
            author = message.author
            channel = message.channel
            embed = discord.Embed(title=f"Olá {str(author)[:-5]}! É assim que a Maçã Madura funciona!",
                                  description=f"Digite ***=roll*** para girar a roleta, e eu irei escolher um nível de característica aleatório pra você! Os níveis são esses!\n\n"
                                              f"**Calamitoso** : {self.porcentagens[0]}% de chance\n"
                                              f"**Horrível** : {self.porcentagens[1]}% de chance\n"
                                              f"**Muito Ruim** : {self.porcentagens[2]}% de chance\n"
                                              f"**Ruim** : {self.porcentagens[3]}% de chance\n"
                                              f"**Normal** : {self.porcentagens[4]}% de chance\n"
                                              f"**Bom** : {self.porcentagens[5]}% de chance\n"
                                              f"**Muito Bom** : {self.porcentagens[6]}% de chance\n"
                                              f"**Épico** : {self.porcentagens[7]}% de chance\n"
                                              f"**Lendário** : {self.porcentagens[8]}% de chance\n"
                                              f"**Místico** : {self.porcentagens[9]}% de chance")
            await channel.send(author.mention, embed=embed)

#CONECTANDO O CLIENT
def setup(client):
    client.add_cog(sorteio(client))
    client.remove_command("help")
