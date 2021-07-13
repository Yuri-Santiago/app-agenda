# PROJETO AGENDA WEB

Projeto destinado ao desenvolvimento e implementação


## 1 - Especificação de Requisitos
	### 1.1 - User History, regras de negocio, restrições
Simulação de User History:
"Eu como usuário
quero poder gerenciar meus contatos
para poder ter uma maior organização e controle sobre eles"


Requisitos mínimos: 
1. Usuários devem ser identificados por id e senha. 
2. A aplicação deve permitir inserir e apagar contatos e atualizar dados de um contato.  
3. O sistema deve oferecer eficientes mecanismos de busca de dados. 
4. Deve-se poder fazer listagens de todos os contatos, por grupos de contato ou por campo (p.ex.  Nome, CEP, cidade, etc.).
5. uma interface de usuário prática e atraente

Regras de negócio:

Restrições:

Agenda de Contatos
Login, com Id e Senha do Usuário
O usuário poderá criar sua Conta do Zero e depois adicionar os contatos a partir da tela
Ao criar a conta definir nome e senha, então vai ser dado um id para ela
Terá a parte dos contatos, uma de adicionar um novo contato e uma opção de atualizar e deletar um contato que terá um botão para cada um
Iremos usar o banco de dados mysql
usuário não poderá por enquanto atualizar os dados dele mesmo
o usuário poderá agrupar os contatos a partir da barra de pesquisa, terá que definir o campo para a busca
Poderá criar grupos de contatos para guardar mais facilmente



## 2 - Telas do sistema
	2.1 - Tela de Login:
	2.2 - Tela de Sign up:
	2.3 - Tela principal:
	2.4 - Tela de criar contato:
	2.5 - Tela de criar grupo:
	2.6 - Tela de editar contato:
	2.7 - Tela de editar grupo:


## 3 - UML
       3.1  Casos de Uso - 
UC01 Acessar Conta
-  UC01.1 Criar conta
		-  UC01.1.1 dados já utilizados
-  UC01.2 Fazer login
            		-  UC01.2.1 dados inválido

                   -     UC02 Adicionar (create)
- UC02.1 Create Grupo
- UC02.2 Create Contato
		
UC03 Read (read)
	- UC03.1 Read Grupo
	- UC03.2 Read Grupos
	- UC03.3 Read Contato
	- UC03.4 Read Contatos

UC04 Atualizar/editar (update)
	- UC04.1 Update Contato
	- UC04.2 Update Grupo

UC05 Deletar (delete)
	- UC05.1 Delete Contato
	- UC05.2 Delete Grupo

UC06 Pesquisar por campo (Atributos)




 	3.2  Diagrama de Sequência 
	3.3  Diagrama de Atividade
	3.4  Diagrama de Classes
		3.4.1 Diagrama de Estado (object Account)
	3.5 Diagrama de Componentes/Pacotes
	3.6 Diagrama de Implantação

## 4 - Design Patterns
	### 4.1 - Factories
	### 4.2 - Observer

## 5 - Implementação do Sistema
## 6 - Observações Finais

Observações finais: 
• Deve-se mencionar que editor(es) UML, quais ferramentas de prototipação e quais  frameworks foram usados para elaborar projeto e código (nome, versão, link, etc.)
• O projeto deve ser entregue via projeto no github, que deve conter: 
 1. todas as respostas organizadas por questões, com diagramas e textos (use o  README para tal); 
 2. as fontes dos códigos. 
       3. Se for um projeto web e estiver hospedado em algum lugar, forneça o link. 
• O programa precisa ser mostrado funcionando. O professor pode pedir para ver as fontes,  onde coerência com os diagramas fornecidos será verificada. 
• Autores e trabalhos consultados deverão ser devidamente citados. 
• Toda cópia, seja de colegas, seja de terceiros (via Google, por exemplo) acarretará a  desconsideração do trabalho para fins de nota. Portanto, evite a tentação de pescar no Google. 
Evitar também repassar respostas próprias para os colegas, pois, neste caso,  serão penalizados quem fez e quem copiou. O professor não acredita em coincidência.
• Observar rigorosamente o dia final de entrega estipulado pelo professor.  
      • Equipes devem ter no máximo 4 membros.

