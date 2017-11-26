Voxus Task

Framework Web: Django
Linguagem: Python

Li o .pdf de intrucoes dia 20/11/2017, comecei a programar efetivamente dia 21/11/2017 apos confirmar algumas informacoes
com a Fernanda Aveiro.
Para comecar estudei quais frameworks que eu conhecia que poderiam atender a maioria das atividades descritas. Apos analise decidi usar Django.Como ja passei muito das 72h limite da entrega,  pois nao consegui tempo para trabalhar muito no projeto pois trabalho full time atualmente, resolvi nao estender mais e entregar sem fazer a parte 5, que percebi que demoraria mais tempo ainda estudando e implementando o servico com a API do servico da amazon. Pelo mesmo motivo nao me preocupei em deixar o site da tarefa bonito, nao apliquei CSS nem defini estilos internos do HTML.

Parte 1: 
CRUD: 2h (final da noite depois do trabalho do dia 21/11/2017)
Essa etapa foi muito rapida de completar, pois o framework remove toda complexidade de preparar o ambiente. Uma vez que ao iniciar um projeto Django o SQLite vem como padrao, basta definir uma classe para fazer o modelo de dados da tabela e alguns comandos para migrar as definicoes para o banco de dados. O HTML deixei simples para atender os dois unicos estados que essa aplicacao web teria (logar, administrar task).

Parte 2: 
Login Autenticado com Google: 6h (final da noite depois do trabalho dias 2h no 22/11/2017, 2h no 23/11/2017 e 2h no 24/11/2017)
Uma das etapas mais frustantes, nunca havia desenvolvido algo parecido e a documentacao oficial usa termos complexos para alguem com pouca experiencia com o framework. Apesar de existir muito tutoriais online a maioria usa uma biblioteca que nao funciona mais com o autenticador do google, entao basicamente testei varias bibliotecas ate encontrar uma que funcionasse corretamente com o framework.

Parte 3: 
Tasks Mais Complexas: 5h (inicio da tarde de 25/11/2017)
Para permitir salvar multiplos anexos tive de estudar e tentar muita direcoes diferentes. Acabei alterando o modelo de dados com uma tabela nova de anexos com relacao muitos para um com a tabela de tarefas. E criei um fluxo para prencher as tabelas garantindo a relacao. Nesse mesmo momento tentei achar se o framework possibilitava colocar links na pagina para o usuario ao ver a task conseguir fazer o donwload dos anexos. Nao encontrei mas criei um link para cara anexo onde o usuario pode clicar com o direito e selecionar pegar o link e abrir o arquivo (aparentemente o browser nao permite que arquivos sejam abertos no localhost).

Parte 4: 
Tasks Completas: 30min (logo depois de terminar a parte 3 no dia 25/11/2017)
Bastou adicionar um campo booleano novo para ser essa flag na tabela das tarefas e subir as migracoes para o banco. E alterar os fomularios e HTML para apresentar esse dado.

Parte 5:
NAO FOI REALIZADA
