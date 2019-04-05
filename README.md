# desafio-stone
Repositório contendo a resolução do Desafio para a Stone Pagamentos


# Execução de Jobs

Tarefas custosas e demoradas infelizmente muitas vezes são parte da realidade do desenvolvimento de software. Este cenário é especialmente comum em uma arquitetura de migração de dados pois é necessário fazer processamentos que tendem a ser demorados, por exemplo, selecionar dados de um banco de dados, tratá-los para um novo formato e enviá-los para uma API. Esse problema é acentuado quando tratamos grandes quantidades e dados.

Uma forma de ter maior controle nestas situações é o uso de background jobs acompanháveis. Estes jobs são bastante úteis em cenários onde temos que executar tarefas demoradas e queremos monitorar o seu andamento.

## O desafio

Desenvolver uma plataforma de execução de Jobs que roda como uma API onde é possível iniciar tarefas em background e acompanhá-las até o seu término. Além disso, deve ser possível ter acesso às informações auxiliares que são enviadas no momento da criação do mesmo.

Os jobs podem ser qualquer tarefa que demore muito, como, por exemplo: Calcular diferentes níveis da sequência de Fibonacci, calcular diferentes níveis de precisão de Pi. Deve ser fácil adicionar novos tipos de jobs para serem agendados, executados e recuperados.

## Endpoints

Seguem abaixo os endpoints mínimos necessários para entregar o desafio. Você pode adicionar novos endpoints, caso sinta necessidade.

POST
/job
Cria um novo job

GET
/job/:id
Pega informações sobre um job pelo seu id

## Critérios de aceite

- A API deve possuir testes que não consumem o recurso real, ou seja, deve ser feito mock;
- Nenhum job pode ser perdido ou deletado;
- Precisamos conseguir agendar e recuperar jobs de diferentes tipos através do mesmo endpoint;
- Precisa respeitar o padrão RestFul para APIs;
- Temos que autenticar através de token de aplicação;
- Não é permitido o uso de ORM;
- Precisamos conseguir passar metadados para o job que podem ser recuperados;
- Atenção para utilizar os status codes do HTTP corretamente de acordo com cada operação da API;

## Meio de entrega

O Código deve estar no Github ou Gitlab.
