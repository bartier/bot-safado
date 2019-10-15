# safadeza-generator

## Objetivo
Esse projeto utiliza uma lista de verbos e uma lista de palavras para gerar atos libidinosos conforme a regra abaixo.

[![Resumo](https://user-images.githubusercontent.com/18057391/66723183-828f3980-edec-11e9-92dd-9c4a5215f2d8.png)](https://twitter.com/RamsesErebro/status/1104507809029328898)

Cada ato libidinoso gerado pelo algoritmo está sendo postado no [perfil do Bot no Twitter a cada 20 minutos](https://twitter.com/BotSafadeza). 

## Contribuindo

Sinta-se à vontade para enviar problemas/sugerir melhorias/tirar dúvidas na aba 'issues' do GitHub nesse repositório. Caso tenha
interesse em enviar uma Pull Request para adicionar uma feature ou corrigir algum bug, por gentileza, envie o máximo possível
de contexto para que sua Pull Request tenha mais chance de ser aceita.

Lembre-se de manter sua Pull Request focada em um objetivo, mantendo as boas práticas.

**Por favor, pergunte primeiro pela aba Issues** antes de iniciar uma alteração significante no projeto, caso contrário, você corre o risco de perder muito tempo em um trabalho
que pode não ser aceito caso não esteja dentre o esperado.

## Como foi gerado a lista de verbos?

Foi utilizado um crawler para obter uma listagem do site [Conjugacao](http://conjugacao.com.br/). Caso tenha mais interesse, acesse o
repositório no GitHub do [projeto com a implementação do crawler](https://github.com/bartier/conjugacaoScraper). 
Foi utilizado o framework [Scrapy](http://scrapy.org/) como base.

## Como foi gerado a lista de palavras?

A lista de palavras (que não são verbos, é claro) foi obtida através do repositório do [fodasebot](https://github.com/WyrmDT/fodasebot),
o qual possui o arquivo [palavras.txt](https://github.com/WyrmDT/fodasebot/blob/master/palavras.txt). No entanto essa listagem
possui verbos, sendo assim, foi gerado um filtro utilizando o script [utils.py](https://github.com/bartier/safadeza-generator/blob/master/utils.py) para
percorrer o arquivo e gerar um novo arquivo, o [palavras_sem_verbos.txt](https://github.com/bartier/safadeza-generator/blob/master/palavras_sem_verbos.txt), que é o arquivo
utilizado.
