import requests
import json

# Seu laudo real com quantas quebras de linha você quiser
laudo_real = """
PREÂMBULO
Em 5 de janeiro de 2026, o Diretor deste Instituto de Criminalística, Perito Criminal Robinson Pereira Valadão, designou os Peritos Criminais Alex Chaves Rocha Lima (Redator) e Everaldo Henrique Diniz (Revisor) para procederem a Exame de Registros Audiovisuais, descreverem minuciosamente o que examinarem e esclarecerem tudo que possa interessar, a fim de atender à requisição da autoridade do 2° Juizado Especial Cível e Criminal de Samambaia 2JECICRSAM/TJDFT.
1 HISTÓRICO
A Decisão com força de ofício, datada de 17 de setembro de 2025 , recebido por esta Seção de Perícias de Biometria Forense e Audiovisuais, solicitava a realização de exames periciais em registros audiovisuais. O objeto do exame era um arquivo de áudio disponibilizado por meio do sistema informatizado de Processo Judicial Eletrônico – PJe associado ao ID 219905048, descrito no item 4.1.
2 OBJETIVO PERICIAL
De acordo com o documento de solicitação, o presente exame teve por objetivo a “verificação de integridade do áudio – se houve algum tipo de edição no conteúdo”, avaliando em que grau as evidências encontradas fortalecem ou enfraquecem a hipótese de que o registro de áudio seja autêntico, em contraposição à hipótese de que seja inautêntico, mediante a verificação da presença de elementos materiais compatíveis com alterações por edição ou adulteração.
É importante destacar que, na ausência de delimitação específica de trechos alegada ou supostamente editados ou adulterados, bem como na ausência de informações sobre quais fatos, partes ou eventos teriam sido omitidos ou alterados, os quais, em regra, constituem as alegações que motivam a solicitação do exame pericial, o exame concentra-se na identificação de indícios técnicos de manipulação, tais como vestígios compatíveis com edição, bem como de descontinuidades ou alterações perceptíveis no fluxo de reprodução do áudio.
3 CADEIA DE CUSTÓDIA DO MATERIAL
A cadeia de custódia, definida pelo Art. 158-A do Código de Processo Penal, é o conjunto de todos os procedimentos utilizados para manter e documentar a história cronológica do vestígio, desde seu reconhecimento até o descarte. Conforme a Portaria 82/2014 da SENASP, esse procedimento divide-se em fase externa (da preservação e coleta até a entrada no órgão central de perícia oficial de natureza criminal) e fase interna (da entrada no órgão pericial até sua devolução com o Laudo de Perícia Criminal, ao órgão requisitante da perícia).
O material foi apresentado diretamente como anexo do processo judicial eletrônico, sem documentação complementar que permitisse rastrear sua origem, o meio de obtenção ou os procedimentos eventualmente adotados para garantir sua integridade antes da solicitação do exame pericial. Dessa forma, considerando a natureza digital do vestígio analisado e a forma como foi disponibilizado para exame, os peritos criminais não dispõem de informações referentes à fase externa da cadeia de custódia, isto é, aos procedimentos adotados desde sua identificação, coleta e preservação até sua anexação ao sistema PJe.
4 MATERIAL
4.1 Material Questionado
Tratava-se de 1 (um) arquivo de áudio disponibilizado no sistema PJe sob o número de ID 219905048 (Tabela 1).
Tabela 1 – Descrição do material
Índice	Nome do Arquivo	Duração Total
[mm:ss,sss]	Tamanho
1	documentoPJe219905048	00:28,322	65,7 KB
Doravante, o arquivo descrito na Tabela 1 foi identificado pelo índice disposto à esquerda: Arquivo 1.
4.2 Identificação Digital do Material
Com o intuito de garantir a rastreabilidade e a integridade do arquivo analisado, foi calculado o resumo de mensagem baseado na função de hash criptográfico SHA-512. A Tabela 2 apresenta o identificador único correspondente a esse arquivo, possibilitando a verificação de eventuais alterações após a elaboração deste Laudo.
Tabela 2 – Identificação digital dos arquivos examinados.
Arquivo	Resumo Criptográfico
1	b9f0dc3a37c36171bb5f877efa30a4fc764d4912dafb47803758180b45109f4698a549422b770383aa56f7e13c2476e990f8d37a08c180a091f13bad0b4dcc4c
5 EXAMES
Neste tópico foram apresentados os exames periciais executados e seus resultados, com vistas a atender ao objetivo pericial deste laudo. Para tanto, foram utilizados programas computacionais capazes de analisar arquivos computacionais de áudio em formato digital, destacando-se os softwares Adobe Audition 25.6.4.2, MediaInfo 25.04 e 010 Editor v16.0.3.
5.1 Análise Descritiva dos Materiais
A análise descritiva consiste na caracterização técnica dos arquivos submetidos a exame, com base em parâmetros formais como contêiner, formato, codec, e demais atributos considerados relevantes para a caracterização do registro audiovisual. Esta etapa é essencial para a interpretação e validação dos exames subsequentes, especialmente em casos de anormalidades ou incompatibilidades técnicas.
5.1.1 Material Questionado
O Arquivo 1 foi obtido diretamente do PJe por meio da integração com o Sistema PROCED.NET. Ao efetuar a busca pelo material associado ao ID 219905048, o sistema retornou um arquivo digital sem uma extensão válida. Inspecionando sua estrutura binária (Figura 2), verificou-se que se tratava de um arquivo em formato Opus encapsulado em Ogg. 
 
Figura 2 – Estrutura binária do Arquivo 1 com cabeçalho Ogg.
Após essa verificação, foi possível prosseguir com a extração das demais características relevantes do registro de áudio, incluídas na Tabela 3, revelando sua compatibilidade com mensagem de áudio produzida a partir de aplicativo de mensagens, como WhatsApp.
Tabela 3 – Características do arquivo de áudio questionado
Característica	Valor
Formato do Contêiner do arquivo	Ogg
Formato	Opus
Canais	1 canal
Taxa de Amostragem	16 kHz
Biblioteca Usada	WhatsApp
5.2 Verificação de Autenticidade
O exame de verificação de autenticidade em registros audiovisuais ou sonoros tem por objetivo identificar a presença de elementos indicativos de modificações que incidam sobre o conteúdo propriamente dito do registro, tais como composições, supressões, apagamentos, mascaramentos, inserções ou remanejamentos. O foco do exame recai sobre modificações capazes de alterar a representação das informações originalmente registradas, com potencial impacto sobre sua semântica no contexto de interesse.
Modificações de natureza estritamente técnica, como processos de compressão, mudança de formato, reencapsulamento ou transcodificação, embora possam ser avaliadas no âmbito da caracterização do arquivo, não são consideradas, por si sós, indicativas de alteração do conteúdo semântico do registro.
Para esse fim, os eventos e características observáveis nos registros questionados são avaliados quanto à sua consistência em relação ao processo alegado ou suposto de produção do arquivo, bem como quanto à sua relevância como elementos indicativos de adulteração, conforme a metodologia descrita no APÊNDICE A – Verificação de Autenticidade.
5.2.1 Análise Perceptual e Contextual
Nas análises perceptual e contextual, o áudio foi examinado em busca de indícios de intervenções, tais como recortes, composições, inserção de trechos ou quaisquer outras ações que, por meio de percepção auditiva, pudessem indicar inconsistências entre o registro analisado e o processo natural de sua geração.
Para isso, foram realizadas oitivas dos sinais, com avaliação perceptual dos padrões esperados de produção da fala registrada. A análise considerou aspectos articulatórios, verificando se as locuções seguem padrões naturais de articulação, como coarticulação e ajuste temporal da fala, bem como características prosódicas, incluindo a evolução da entonação, do ritmo e da intensidade. 
No contexto desta análise, foram identificados trechos que apresentam descontinuidades auditivas e padrões de produção da fala que se afastam do esperado para um registro contínuo e espontâneo. Tais trechos foram selecionados para exame mais detalhado e encontram-se sistematizados na Tabela 4.
Tabela 4 – Trechos de exame detalhado
Trecho [mm:ss.sss]	Fenômeno observado
0:05.280	Neste trecho de fala, há uma repetição “(...) o inquilino sair da... lá da 319 (...)”. Na segunda ocorrência da expressão “lá da”, verificou-se a entrada do enunciado de maneira abrupta, dando a impressão auditiva de sobreposição do som [k] com a palavra “dá”.
0:06.735	Neste trecho de fala, a ideia comunicada é “ela tá se achando dona (...)”. No entanto, verificou-se a supressão da sílaba inicial da frase, dando a impressão auditiva de “[L'tá] se achando dona (...)”. Além disso, é audível uma quebra na respiração da falante, que antecederia naturalmente o início do enunciado.
0:27.160	Logo após o final dos trechos de fala, observou-se uma alteração perceptível no padrão do ruído de fundo, com surgimento de componentes sonoros distintos daqueles presentes ao longo do restante do registro. Essa mudança ocorre de forma abrupta, sem transição gradual perceptível, o que reforça a impressão auditiva de descontinuidade no encerramento do áudio.
5.2.2 Análise Quantitativa
Nas análises quantitativas, foram avaliadas a evolução e o comportamento dos padrões temporais e espectrais do sinal de áudio, com o objetivo de identificar eventuais anormalidades ou características potencialmente associáveis a processos de edição, tais como cortes, supressões ou inserções.
As análises foram conduzidas por meio da inspeção do oscilograma e do espectrograma, permitindo a verificação da continuidade e da coerência do sinal ao longo do tempo e em diferentes faixas de frequência.
No início do Arquivo 1, observa-se a presença de aproximadamente 240 milissegundos em que as amostras de áudio apresentam valor igual a zero, seguidos do início abrupto de trecho com fala (Figura 3).
 
Figura 3 – Oscilograma e Espectrograma do Arquivo 1, com destaque para o evento em estudo.
No trecho em torno de 0:05.280, observou-se a presença de um evento transitório de alta energia e banda larga imediatamente após breve pausa (Figura 4). Tal padrão é compatível com a ocorrência de transiente acústico de curta duração, como o associado à produção de consoante plosiva, a exemplo de [k], ou a ruído impulsivo.
 
Figura 4 – Oscilograma e Espectrograma do Arquivo 1, com destaque para o evento em estudo.
No trecho em torno de 0:06.735, observou-se a presença de ruído compatível com respiração audível que não se desenvolve até um ciclo respiratório completo, sendo seguida pelo início abrupto da fala (Figura 5).
 
Figura 5 – Oscilograma e Espectrograma do Arquivo 1, com destaque para o evento em estudo.
No trecho final do arquivo, imediatamente após o término da fala, observou-se queda abrupta de energia no domínio temporal, acompanhada de alteração no padrão espectral do ruído de fundo, sem transição gradual perceptível (Figura 6).
 
Figura 6 – Oscilograma e Espectrograma do Arquivo 1, com destaque para o evento em estudo.
5.2.3 Análise de Metadados e Estrutura de Arquivos 
A análise dos metadados e da estrutura de arquivo teve como objetivo identificar indícios de não originalidade ou manipulação, seja por meio de indicações diretas ou indiretas presentes na estrutura dos arquivos e nos metadados, seja pela constatação de inconsistências entre esses registros e o processo de gravação ao qual o material audiovisual foi alegada ou supostamente submetido.
5.2.3.1 Metadados
O Arquivo 1 consistia em um arquivo de áudio codificado em Opus, encapsulado em contêiner Ogg, sem extensão de arquivo válida, contendo uma trilha de áudio com taxa de amostragem registrada de 16 kHz e compressão com perdas (Lossy), utilizando a biblioteca do WhatsApp, conforme indicado pelos metadados extraídos com o auxílio do software MediaInfo (Figura 7).
 
Figura 7 – Metadados do Arquivo 1, extraídos com o auxílio do software MediaInfo, com destaque para a indicação "Biblioteca usada: WhatsApp"
Essas características, em especial o uso do codec Opus encapsulado em Ogg e a indicação da biblioteca WhatsApp, são compatíveis com mensagens de áudio gravadas diretamente no aplicativo WhatsApp, no formato PTT (Push-to-Talk), no qual a gravação ocorre enquanto o usuário mantém pressionado o botão correspondente.
Observa-se que arquivos de áudio de origem diversa, quando encaminhados pelo WhatsApp sem terem sido originalmente gravados no aplicativo, tendem a preservar metadados associados ao formato original antes do envio. Em testes exploratórios realizados, verificou-se que arquivos encaminhados ao aplicativo mantiveram, nos metadados, referências a bibliotecas associadas aos formatos de origem, como M4A, MP3 e 3GP, ao passo que arquivos gravados diretamente no WhatsApp exibiram a biblioteca WhatsApp como origem.
Embora esse comportamento tenha se mostrado consistente nos testes realizados, não há documentação oficial conhecida que assegure tal padrão de forma conclusiva. Assim, a presença da biblioteca WhatsApp nos metadados deve ser interpretada como um forte indício de que o arquivo foi gravado diretamente no aplicativo, e não como evidência categórica de sua origem.
5.2.3.2 Estrutura de Arquivo
Dando prosseguimento à análise, foi realizada uma inspeção da estrutura binária do arquivo, com o objetivo de identificar eventuais inconsistências estruturais ou elementos característicos associados ao processo de codificação do áudio, bem como possíveis indicativos de reprocessamento ou edição (Figura 8).
 
Figura 8 – Parte da estrutura binária do cabeçalho do Arquivo 1.
A inspeção dos dados binários evidenciou uma estrutura plenamente compatível com um arquivo de áudio codificado em Opus e encapsulado em contêiner Ogg, contendo estruturas formais do codec e do contêiner compatíveis com mensagens de voz produzidas pelo aplicativo WhatsApp. A análise mais aprofundada da estrutura permitiu observar os seguintes achados: 
1.	O serial number, destacado em amarelo na Figura 8, apresentou valor nulo (0x00000000). Esta é uma característica documentada de arquivos OGG gerados pelo motor de gravação do WhatsApp no Android. Em uma gravação OGG padrão de computador, esse número seria aleatório. O valor "zero" indica uma implementação específica que não segue a geração aleatória da especificação OGG padrão, sendo uma marca registrada do app.
2.	O campo pre-skip, destacado em vermelho na Figura 8, apresentou valor correspondente a 104 amostras . Este valor específico é o padrão da biblioteca libopus quando configurada para o modo de "baixa latência" (comum em sistemas Android). Editores de áudio como Audacity ou ferramentas de conversão genéricas (FFmpeg) costumam gerar um pre-skip padrão de 312 ou 3840 samples. O valor 104 é uma assinatura forte de que o arquivo foi gerado pelo encoder nativo do WhatsApp/Android.
Essas informações apresentam elevada robustez na análise, por não serem derivadas de metadados declarativos, mas de campos estruturais do contêiner e do codec, cuja modificação demandaria reempacotamento completo do bitstream de áudio.
5.2.4 Resultados das análises
Os exames de metadados e da estrutura do arquivo evidenciaram que o Arquivo 1 apresenta características plenamente compatíveis com mensagem de voz gravada diretamente no aplicativo WhatsApp, em ambiente Android, não tendo sido identificados vestígios que indiquem processamento por softwares de edição ou recodificação externa posterior à gravação.
Destacam-se, nesse contexto, elementos estruturais do arquivo, tais como o serial number e o campo pre-skip, extraídos diretamente do contêiner Ogg e do cabeçalho Opus, os quais são coerentes com o padrão de codificação adotado pelo WhatsApp em dispositivos Android e não são passíveis de modificação sem reempacotamento completo do bitstream, o que tenderia a deixar vestígios técnicos detectáveis.
Não obstante a compatibilidade estrutural do arquivo, as análises perceptual, contextual e quantitativa identificaram fenômenos pontuais que, à primeira análise, poderiam ser interpretados como anomalias, tais como variações no padrão do ruído de fundo em momentos de pausa na fala e supressão parcial de sílabas no início de alguns enunciados.
Considerando-se a hipótese de que o arquivo tenha sido efetivamente gravado por um dispositivo Android, sustentada pelos elementos estruturais observados, tais fenômenos encontram explicação conceitual plausível nos mecanismos de processamento automático empregados pelo sistema Android para gravação de mensagens de voz. Conforme documentação oficial do desenvolvedor Android , o modo de captura de áudio VOICE_COMMUNICATION, projetado para aplicações de VoIP e mensagens de voz, pode aplicar automaticamente recursos como cancelamento de eco, controle automático de ganho, redução de ruído e detecção de atividade de voz (Voice Activity Detection – VAD), caso estes sejam recursos oferecidos pelo hardware do dispositivo e versão do sistema operacional.
Em ambientes ruidosos, a atuação combinada desses mecanismos pode resultar em variações no ruído de fundo durante pausas na fala, bem como em transições abruptas entre silêncio e fala, especialmente quando o limiar de detecção do VAD é atingido, fenômeno que pode se manifestar perceptualmente como supressão parcial de sílabas iniciais após momentos de pausa. De modo semelhante, a alteração do padrão de ruído observada ao final do registro pode ser compatível com a cessação da atividade vocal detectada pelo VAD, seguida da desativação ou reconfiguração dos mecanismos automáticos de supressão de ruído.
6 CONSIDERAÇÕES FINAIS
Neste laudo foram apresentadas as análises realizadas com base exclusivamente no arquivo de áudio disponibilizado para exame, limitadas pela ausência do dispositivo alegadamente utilizado para a gravação original.
Os fenômenos perceptuais e quantitativos identificados ao longo das análises, embora inicialmente classificados como pontos de atenção, mostram-se conceitualmente compatíveis com a atuação de processamentos automáticos de áudio implementados conforme as diretrizes e manuais de desenvolvimento de aplicativos para o sistema Android, não constituindo, isoladamente, indícios técnicos inequívocos de edição ou adulteração do conteúdo do registro.
Todavia, ressalta-se que a atribuição categórica desses fenômenos ao funcionamento específico de determinado dispositivo ou configuração de software somente seria possível mediante a análise direta do equipamento no qual, alegadamente, ocorreu a gravação primária do registro de áudio em questão. Na ausência desse elemento, as conclusões do presente exame limitam-se à avaliação da compatibilidade técnica do arquivo analisado com os processos de gravação presumidos, bem como à inexistência de vestígios materiais que sustentem a hipótese de manipulação do conteúdo por edição ou adulteração posterior.
7 CONCLUSÃO
Por fim, diante do exposto e analisado, e fundamentado nos elementos técnicos obtidos ao longo dos exames realizados, os Peritos Criminais concluem que, consideradas as limitações impostas pela ausência do dispositivo alegadamente utilizado para a gravação do áudio, bem como os graus de relevância atribuídos aos achados periciais, as evidências disponíveis fortalecem moderadamente a hipótese de que o arquivo de áudio analisado é autêntico, em contraposição à hipótese de que seja inautêntico. Este grau de suporte à hipótese corresponde ao nível +2 da escala apresentada no APÊNDICE B – Natureza das Conclusões, cuja faixa varia de –4 a +4. 
Nada mais havendo a lavrar, foi encerrado o presente Laudo de Perícia Criminal composto de 18 folhas, que relatado pelo Perito Criminal Alex Chaves Rocha Lima (que realizou os exames), lido e achado conforme pelo Perito Criminal Everaldo Henrique Diniz, segue assinado digitalmente .

"""

# Montamos o dicionário Python (ele cuida das quebras de linha pra gente)
payload = {
    "conteudo": laudo_real,
    "tipo_exame": "Verificação de Autenticidade de Registro de Áudio"
}

print("Enviando laudo para o Perito Revisor (Ollama)... Isso pode levar alguns segundos dependendo do hardware.")

# Fazemos a requisição POST para a nossa própria API
resposta = requests.post("http://localhost:8000/revisar_laudo", json=payload)

if resposta.status_code == 200:
    print("\n✅ SUCESSO! Resposta da IA:")
    # Imprime o JSON de resposta formatado e bonito
    print(json.dumps(resposta.json(), indent=4, ensure_ascii=False))
else:
    print(f"\n❌ ERRO {resposta.status_code}:")
    print(resposta.text)