# Experimento 2 - MVP
usando o padrão MVP foi criado uma aplicação de calculadora onde os usuários podem realizar operações básicas de adição, subtração, multiplicação e divisão.

A classe CalculatorModel contém a lógica para realizar cálculos matemáticos básicos, como adição, subtração, multiplicação e divisão.

View:
O arquivo HTML  define a interface do usuário para a calculadora, incluindo campos de entrada para números e um menu suspenso para seleção de operação.

A classe CalculatorPresenter atua como intermediário entre o modelo e a visualização.
Recebe as entradas do usuário da View, como números e operação selecionada.
Chama o método correspondente no modelo para realizar o cálculo.
Atualiza a View com o resultado do cálculo.


Flask foi utilizado para criar o servidor web e lidar com as solicitações HTTP.
E também define rotas para manipular solicitações, como a rota /calculate para realizar o cálculo.
Renderiza o template HTML com os resultados para serem exibidos ao usuário.
