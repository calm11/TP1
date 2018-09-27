INFO7015 – Tópicos em Redes de Computadores – Trabalho Prático 1
Profa. Dra. Michele Nogueira
Aluna: Carolina Moraes

Reprodução dos resultados principais do artigo Jellyfish: Networking Data Centers Randomly.

Introdução
Este trabalho foi desenvolvido como um preparo para os próximos trabalhos da Disciplina de Gerência de Redes, o problema proposto foi reproduzir a figura 9 e tabela 1 do artigo Jellyfish. Esse que trata sobre uma topologia para organizar redes de data center, propõe uma topologia de grafo aleatório para switches top-of-rack. Os autores mostram que essa abordagem é mais eficiente em termos de custo e pode suportar mais servidores com a mesma quantidade de equipamentos. Além disso, as topologias Jellyfish podem manter a mesma taxa de transferência geral das redes Fat-tree devido ao curto caminho médio entre os nós.

1.	Que problema a Jellyfish estava tentando resolver? Qual era o estado da arte no momento em que o artigo foi publicado?
O artigo examina as técnicas existentes para conexão de switches top-of-rack em um datacenter e apresenta o resultado surpreendente de que os switches de conexão aleatoriamente têm muitas propriedades desejáveis em relação a uma topologia puramente estruturada. Havia uma necessidade de mercado para que os data centers aumentassem sua capacidade de forma incremental para lidar com a crescente quantidade de tráfego. O objetivo do artigo foi apresentar uma topologia de rede de data center que permite a incorporação harmoniosa de servidores adicionais para o crescimento futuro. Também é importante que essa topologia promovesse a utilização eficiente da rede. Os autores sugerem uma topologia de grafos aleatórios de grau limitado entre os switches top-of-rack (ToR) chamados Jellyfish para conseguir isso, e mostram que essa estrutura flexível permite fácil crescimento incremental enquanto é altamente eficiente. A topologia Jellyfish proposta simplifica a expansão incremental, facilitando, assim, as empresas de ampliar seus data centers à medida que a demanda aumenta. Não há necessidade de planejar a topologia do data center antecipadamente ou preocupar-se em reconectá-la completamente durante a evolução. Além disso, a rede Jellyfish tem maior largura de banda e taxa de transferência. O estado atual da arte era justamente o que os autores estavam pesquisando e desenvolveram no artigo, havia uma necessidade de mercado para que os data centers aumentem sua capacidade de forma incremental para lidar com a crescente quantidade de tráfego.

2.	Um breve resumo dos métodos e resultados do artigo original (com foco especial na Figura 9 e na Tabela 1).

Métodos: O artigo não descreve especificamente os protocolos de roteamento e transporte utilizados no experimento. Os autores usaram um simulador desenvolvido pelos autores de Multipath TCP para estudar o throughput vs. rank of flow para Jellyfish vs. Fat-tree.
Resultados: Os autores mostram que a Jellyfish supera outras topologias de rede em termos de desempenho, eles também relataram que Jellyfish geralmente tem caminhos menores entre os servidores, o que significa que esta rede aleatória é altamente conectada e eficiente. A estrutura flexível da Jellyfish também permite expansibilidade incremental suave. A idéia deles é que, quando um rack de servidores for adicionado, escolha links aleatórios na rede existente, remova-os e vincule as duas portas recém-liberadas ao novo ToR e repita conforme necessário. Os autores explicam que, como os comprimentos de caminho aumentam lentamente, a largura de banda por servidor permanece alta mesmo depois de grandes expansões. Isso mostra que a expansão é fácil e pode ser feita de forma incremental sem sacrificar a perda significativa de largura de banda para data centers maiores. No geral, os autores descobriram que a Jellyfish teve um desempenho tão bom ou melhor do que uma topologia Fat-tree tradicional em todas as suas diferentes métricas. Essas métricas incluem average path length, average throughput, fairness e number os servers supported, entre outras coisas. Ao mesmo tempo, a Jellyfish oferece muito mais facilidade de expansão, o que, argumentam os autores, a torna uma escolha viável de topologia em data centers reais.
A figura 9 mostra a distribuição do número de caminhos distintos para cada link. O eixo y mostra o número de caminhos distintos nos quais um link está ativo. O eixo x é uma classificação ordenada dos links. O gráfico mostra a distribuição usando três diferentes técnicas de seleção de caminho: 8 caminhos mais curtos, ECMP de 64 vias e ECMP de 8 vias. A figura mostra que k=shortest paths é um algoritmo de roteamento muito melhor para usar em Jellyfish do que ECMP.
A tabela 1 mostra resultados de execução de simulações de pacotes com fat-tree e Jellyfish com os protocolos TCP e MPTCP. A tabela mostra que o uso de k-shortest-paths no TCP com Jellyfish dá a mesma taxa de transferência média que a execução do ECMP em fat-tree. Este é um dado que mostra o quanto a Jellyfish alcança o mesmo desempenho de Fat-tree.

3.	Detalhe sobre sua abordagem para reproduzir a figura. Se você escolheu uma plataforma ou ferramenta específica, explique por que você fez essa escolha. Destaque as vantagens da sua abordagem, bem como quaisquer inconvenientes. 
A simulação é uma série de scripts Python, desenvolvidos em cima da ferramenta Pox. Utilizei a biblioteca matplotlib para reproduzir a Figura 9. O artigo original utiliza um simulador, já conforme orientado pela professora, nesta reprodução foi utilizado o Mininet como emulador de rede. 
Escolhi o pox após algumas pesquisas e por ser uma ferramenta desenvolvida em python.
Só com as documentações do Mininet, pox e o artigo, eu não teria conseguido reproduzir o artigo. As pesquisas feitas e os e-mails trocados com alunos da Universidade de Stanford, me ajudaram a tentar ao máximo finalizar o trabalho.

Houve algum desafio que você acertou ou suposições que você precisava fazer?
O artigo original não especificou a configuração experimental usada para gerar a Figura 9. Eles dizem apenas que usaram uma configuração de 686 servidores, mas não especificam o número de switches usados ou o número de portas disponíveis em cada switch. Portanto, só consegui gerar a figura após tentar adivinhar o parâmetro correto ao executar a simulação. Também pesquisei sobre outras reproduções do artigo para entender como identificar o parâmetro utilizado pelos autores.
4.	Qual o resultado que você conseguiu? Correspondeu ao artigo original?
Consegui reproduzir a figura 9, próxima ao que foi apresentado no artigo, já a tabela 1 não consegui reproduzi-la ao que foi apresentado no artigo, pois tive dificuldade em usar o MPTCP, testei várias formas que incorporá-lo ao código mas não obtive sucesso. Então, os resultados não correspondem exatamente ao artigo original.
5.	Você estendeu o experimento de alguma forma? (por exemplo, outra figura do artigo, uma extensão das figuras que você precisa replicar ou um novo experimento.)
Devido ao tempo de pesquisa em cima de entender o MPTCP, não tive a oportunidade de estender os experimentos, apenas gerei vários gráficos até conseguir entender a figura 9.
6.	Instruções explícitas, passo a passo, sobre como instalar e executar sua experiência. Idealmente, outro pesquisador deve ser capaz de instalar e configurar com um único comando, executar o experimento com um único comando e gerar gráficos de saída nítidos.
Toda as simulações foram feitas no Ubuntu 18.04, mas podem ser feitas por ssh em um VM Mininet
Certificar-se de ter o python instalado
Instalar Mininet
git clone https://github.com/mininet/mininet 
/util/install.sh -a
Instalar o pox
git clone https://github.com/noxrepo/pox
sudo apt-get install python-matplotlib
sudo apt-get install python-networkx
sudo apt install python-pip
sudo apt-get install termcolor
Após todos os passos:
git clone https://github.com/calm11/TP1
cd TP1/pox/ext
./figura.sh (gera figura9.png)
./gera_tabela.sh (gera a tabela no terminal)
Referências:
A. Singla, C.Hong, L. Popa and P. B. Godfrey. Jellyfish: Networking Data Centers Randomly. Proceedings of USENIX Symposium on Networked Systems Design and Implementation, 225–238, Presented as part of the 9th USENIX Symposium on Networked Systems Design and Implementation (NSDI 12), San Jose, CA, 2012, USENIX.
https://stackoverflow.com/questions/9020843/how-to-convert-a-mac-number-to-mac-string
https://multipath-tcp.org/pmwiki.php/Users/AptRepository
