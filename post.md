Olá, tudo bem com vocês?

Então, neste post vou falar para vocês como o Google funciona, claro que não vai ser nada tão performático quanto ele ou com um algoritmo de pesquisa tão robusto, mas você já vai conseguir imaginar como a gigante é feita, afinal quem nunca imaginou como o sistema deles é feito.

Para este artigo será necessário que você tenha noções em lógica de programação. A Stack que vamos utilizar será a seguinte, Python com a framework Flask e Scrapy para os WebCrawlers, NoSQL com MongoDB, HTML, CSS, JS e muito amor <3

Então vamos ao que interessa, código e mais código...

Antes de mais nada, precisamos criar o nosso algoritmo de crawler para isso utilizaremos um framework chamado para scrapy. Baixe ele através do pip install para podemos utilizar ele no nosso código.

pip install scrapy
Você pode baixar tanto para toda a maquina quanto para o seu ambiente de desenvolvimento virtualenv, no meu caso instalei para toda a maquina. Com isso feito vamos criar nossa webcrawler genérica que vai pegar os dados de Title e Description dos sites.

Neste caso eu usei o seguinte comando após a instalação do scrapy

scrapy startproject generic
Assim ele criou a pasta "generic" com a estrutura básica para este projeto, assim podemos continuar com o próximo passo que é definir a spider com uma lista de url's a serem processadas.

https://github.com/reginaldojunior/searchengine/blob/4e9ec63d4c228621bd80e49a13bb2615cd615053/generic/spiders/generic.py

Agora vamos deixar isso dinâmico?

Para isso vamos utilizar a library pymongo (não vou usar o mongoengine), então vamos instalar ela, utilizando o seguinte comando.

pip install pymongo
Feito isso vamos fazer algumas correções no nosso arquivo de configuração "settings.py" do nosso projeto. Colocando os seguintes dados.

https://github.com/reginaldojunior/searchengine/blob/4e9ec63d4c228621bd80e49a13bb2615cd615053/generic/settings.py

Agora, vamos criar nosso classe de conexão com o mongodb, então crie vá em pipelines.py e insira o seguinte código.

https://github.com/reginaldojunior/searchengine/blob/d3a7bec2ba0cbac09b07076c470996dda72831df/generic/pipelines.py

Feito isso vamos importar a função get_sites para nosso arquivo generic.py, pois nessa collections vamos ter os sites que vão ser passados para o crawler.

https://github.com/reginaldojunior/searchengine/blob/8f8105605de2ae149e0338518e38763451a750a5/generic/pipelines.py

Nesse commit também criei a função para inserir os dados observe a função create_info

Após isso precisamos recuperar esses dados no nosso arquivo de crawler que é o generic.py, observe como ficou o novo código com os dados dinâmicos.

https://github.com/reginaldojunior/searchengine/blob/8f8105605de2ae149e0338518e38763451a750a5/generic/spiders/generic.py

Com isso já temos nossa crawler pronto para indexar os dados basta rodar ele via linha de comando na pasta do projeto rode "scrapy crawl generic" não esqueça de criar as collections no mongodb antes. Para isso você vai precisar de o mongodb instalado na sua maquina, e rodar os seguintes comandos de criação.

Criação do database

"use searchengine"

Criação das collections

"db.createCollection('sites')"
"db.createCollection('infos')"

Agora vamos começar criar nosso front simples para cadastrar os sites e fazer a pesquisa deles, para isso utilizaremos o framework chamado flask, então você pode fazer a instalação dele atráves do "pip install flask" e "pip install Flask-PyMongo". Feito a instalação criaremos nosso site, crie uma pasta chamada frontend com o seguinte conteúdo.

https://github.com/reginaldojunior/searchengine/tree/615bd2b5f44d952f43f1faceacbcf2504f183746/frontend

Ai já está a estrutura básica do frontend, agora iremos deixar ele dinâmico.

Vamos começar pelo cadastro de novos sites, no action colocaremos /newsite e method POST e então criaremos a rota no arquivo run.py, veja como ficou:

https://github.com/reginaldojunior/searchengine/commit/2acc88b6e45aac4d749ed207099e0450ff222ccc

Agora a parte da busca, no form de busca colocaremos a action /search com o action GET e então buscaremos as informações na collection por um find básico como falei, a ideia não é o super algoritmo de busca do google e sim como ele faz para fazer isso, para uma busca com resultados melhores recomendo o uso do elasticsearch. Então o nosso código de busca ficara assim:

https://github.com/reginaldojunior/searchengine/commit/03158eb831ccf3c710d80e2694dfdbf8e23cdc8a

E a view desta pagina assim:

https://github.com/reginaldojunior/searchengine/commit/9b50e116f03d954d998da583bc5c15c980257529

Como antes eu tinha esquecido de salvar a url no documento eu fiz a correção, veja como ficou

https://github.com/reginaldojunior/searchengine/commit/21943f0347bcb3aed4f12477d80b7c2885a4fbdb

Então com isso feito, temos um mini google feito, onde ele coleta as informações dos sites e faz as buscas pelo termo procurado. Todo o código está disponivel no meu github:

https://github.com/reginaldojunior/searchengine

Você também pode comentar esse post ou colaborar no repositório, fique a vontade também para tirar dúvidas, espero que tenha sido de grande ajuda esse post, e até a próxima!

Fontes: 

http://pt.slideshare.net/bernardofontes/crawleando-a-web-feito-gente-grande-com-o-scrapy

http://www.gilenofilho.com.br/usando-o-scrapy-e-o-rethinkdb-para-capturar-e-armazenar-dados-imobiliarios-parte-i/

https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/