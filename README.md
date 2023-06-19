# Projeto Sistemas Distribuidos 
_Integrantes:_ 

Rebeca Cândida dos Santos | https://github.com/rsbeca/projetosd23

Vinicius Almeida Fidelis | 

O projeto foi feito com o intuito de cadastrar as tarefas, do dia-a-dia do usuário, sendo de fácil utilização. Caso alguma tarefa ultrapassar no seu prazo de validade, ela fica na cor vermelha, se o horário estiver em formato errado, ou a data o mesmo, fica em laranja, e caso estiver tudo certo, no prazo para concluir e o horário e datas no formato correto, a tarefa aparece em verde.

A interface tem a opção de editar a tarefa caso estiver algo errado, e excluir quando estiver concluída.
Foi feita com facil acesso para a utilização de todos os tipos de usuários.

Na parte superior da página tem as opções: "Inicio" que leva para a pagina inicial da aplicação, mostrando as tarefas que precisam ser realizadas, no "Sobre", explica em um texto resumo sobre as funcionalidades da página e em "Nova Tarefa", é onde fica para cadastrar a tarefa com os campos de título, conteúdo da tarefa, horário limite e a data limite da realização da tarefa, e no final com a opção de "Enviar".

Na página inicio do lado de data, em amarelo tem a opção de editar a tarefa, que levará para outra página em que você pode editar, e quando terminar clique em "Enviar", caso queira apagar a tarefa, aperte no botão vermelho ecrito "Apagar Tarefa", que deletará a tarefa.

Organização do projeto : static: contém arquivos estáticos, como exemplos, arquivos de estilos .css. templates: contém todos os templates usando a engine Jinja.

Projeto:

Para rodar o projeto siga os seguintes passos:

1 - Inicie o ambiente env dentro da aplicação.

2 - Instale os pacotes necessários: pip install -r requirements.txt

3 - Execute iniciar_banco py.

4 - Execute app.py

5 - O localhost ira abrir na porta 5000, com isto basta vizualizar.

Docker:

Caso queira rodar utilizando uma imagem no docker basta seguir os seguintes passos:

1 - Instale o docker em sua máquina local (virtual).

2 - Autenticar no docker hub na máquina local (virtual): sudo docker login .

2 - sudo docker image build -t trabalhosistema .

3 - Execute um conteiner para essa imagem. sudo docker run -p 5000:5000 -d trabalhosistema .

4 - Criar uma tag para a imagem docker de referência: sudo docker tag flask-blog-app /

5 - Publicar imagem: sudo docker push /

6 - Para usar a sua imagem, basta executar na sua máquina local (virtual): sudo docker run -p 5000:5000 -d /
