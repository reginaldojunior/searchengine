Olá, tudo bem com vocês?

Então, neste post vou falar para vocês como criar seu próprio Google, claro que não vai ser nada tão performático quanto ele ou com um algoritmo de pesquisa tão robusto, mas você já vai conseguir imaginar como a gigante é feita, afinal quem nunca imaginou como o sistema deles é feito.

Para este artigo será necessário que você tenha noções em lógica de programação. A Stack que vamos utilizar será a seguinte, Python com a framework Flask e Scrapy para os WebCrawlers, NoSQL com MongoDB, HTML, CSS, JS e muito amor <3

Então vamos ao que interessa, código e mais código...

Antes de mais nada, precisamos criar o nosso algoritmo de crawler para isso utilizaremos um framework chamado scrapy. Baixe ele através do pip install para podemos utilizar ele no nosso código.

pip install scrapy

Você pode baixar tanto para toda a maquina quanto para o seu ambiente de desenvolvimento virtualenv, no meu caso instalei para toda a maquina. Com isso feito vamos criar nossa webcrawler genérica que vai pegar os dados de Title e Description dos sites.

Neste caso eu usei o seguinte comando após a instalação do scrapy

scrapy startproject generic

Assim ele criou a pasta "generic" com a estrutura básica para este projeto, assim podemos continuar com o próximo passo que é definir a spider com uma lista de url's a serem processadas, estas que serão geradas dinamicamente através do banco, teremos um form para esses cadastros que faremos mais para frente.

Fontes: 

http://pt.slideshare.net/bernardofontes/crawleando-a-web-feito-gente-grande-com-o-scrapy

http://www.gilenofilho.com.br/usando-o-scrapy-e-o-rethinkdb-para-capturar-e-armazenar-dados-imobiliarios-parte-i/
