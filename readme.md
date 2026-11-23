SISTEMAS DE TREINOS DA UEMAFIT 

Agora q vc já aprender sobre ***Prgramas orenteados a objetos(POO)***
E TAMB´ME VIU COM FUNCIOA UM ***CRUD*** (Create, read, update, delete), chegou a hora de colocar esse conhecimento em prática.
Neste projeto vc deve imaginar que é um personal trainer da acamdeia UEMAFIT e precisa desenvolver um sistema simples para gerenciar alunos e montar fichas de treino.

### OBJETIVO DO PROJETO
Criar um programa em **python** que permita ao personal trainer: 
1 - Cadastrar Alunos
2 - Visualizar alunos cadastrados 
3 - Remover alunos 
4 - Entrevistar alunos para montar uma ***Ficha de treino personalizada**

### CONTEXTO 
A cadeia UEMAFIT trabalha com três grupos principais de alunos:
- Adolescentres (até 17anos)
- Adultos (18 a 59 anos)
- Idosos (60 ou mais)
 Cada grupo deve receber um tipo de treino adequado 

### Estrutura do Sistema 
Você deve criar uma classe chamada "PersonalTrainer.
Dentro dela serão implementados as funcionalidades do sistema. 
Utilize uma lista para armazenar os alunos, onde cada aluno será representado por um diciconário com suas inforações.

### Informações do Aluno
Quando um aluno for cadastrado, o sistema deve solicitar:
- nome
- Idade
- Meta de treino (ex: Emagrecer, ganhar massa, melhorar condicionamento)
- Dias disponiveis para treinar 
- Horas disponiveis por dia 
- Se possui alguma lesão ou doença
 
 Essas informações devem ser armazenadas no sistema.

### FUNCIONALIDADES CRUD
**1- CREATE - Cadastrar aluno**
cadastrar novo aluno no sistema

**2- READ - Listar alunos**
Mostrar todos os alunos cadastrados 
exemplo de saida: 
0 - João | Adulto 
1 - Maria | Idoso

**3- UPDATE -Atualizar Aluno**
Permitir alterar informações do aluno, como: 
- idade
- meta
- dias disponiveis 
- horas por dia

**4- DELETE - Remover aluno**
Remover um aluno da lista utilizando o índice

### ENTREVISTA DO ALUNO 
crie uma função que funcione como **uma entrevista com o aluno** antes de gerar o treino. 
Perguntas q devem ser feitas: 
Qual sua meta de treino?
Quantos dias por semana vc pode treinar?
quantas horas por dia vc possiu disponíveis?
você possui alguma doença ou lesão?

### Geração da ficha de treino 
Cire um método que gere uma ficha de treino simples baseada na idade do aluno. 
Exemplo

### Menu do sistema 
Seu programadeve possuir um menu semelhante a este: 
=====UEMAFIT - SISTEMA DE TREINOS=====
1-....
2-....

