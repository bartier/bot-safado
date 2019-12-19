# safadeza-generator

[![GitHub issues](https://img.shields.io/github/issues/bartier/safadeza-generator)](https://github.com/bartier/safadeza-generator/issues)
[![GitHub forks](https://img.shields.io/github/forks/bartier/safadeza-generator)](https://github.com/bartier/safadeza-generator/network)
[![GitHub stars](https://img.shields.io/github/stars/bartier/safadeza-generator)](https://github.com/bartier/safadeza-generator/stargazers)
[![GitHub license](https://img.shields.io/github/license/bartier/safadeza-generator)](https://github.com/bartier/safadeza-generator/blob/master/LICENSE)

## Objetivo
Esse projeto utiliza uma lista de verbos e uma lista de palavras para gerar atos libidinosos conforme a regra abaixo.

### `verbo no infinitivo + (objeto direto)`

## Exemplos clássicos da regra acima

- descabelar o palhaço
- afogar o ganso
- acarretar o nhenhenhem

Cada ato libidinoso gerado pelo algoritmo está sendo postado no [perfil do Bot no Twitter de tempo em tempo.](https://twitter.com/botsafado)

## Configurando o projeto

Para configurar o projeto, clone o repositório 

`git clone https://github.com/bartier/safadeza-generator.git`

No diretório do projeto, monte a imagem do docker

`docker build -t safadeza-generator .`

E execute a imagem safadeza-generator 

`docker run --rm -v /safadeza-generator/:/safadeza-generator/ safadeza-generator`

O arquivo de output será salvo em `/safadeza-generator/frases.txt`.

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
possui verbos, sendo assim, foi gerado um filtro utilizando o script [gerar_palavras_sem_verbos.py](https://github.com/bartier/safadeza-generator/blob/master/utils/gerar_palavras_sem_verbos.py) para
percorrer o arquivo e gerar um novo arquivo, o [palavras_sem_verbos.txt](https://github.com/bartier/safadeza-generator/blob/master/utils/palavras_sem_verbos.txt), que é o arquivo
utilizado.

## Como foram filtradas as palavras ofensivas?

A lista de palavras ofensivas foi obdito atráves do fórum da [Comunidade do Hardware](https://www.hardware.com.br/comunidade/lista-palavroes/1456601/).
Após algumas normalizaçoes e verbos adicionados manualmente, foi gerado o arquivo final [palavras_ofensivas.txt](https://github.com/WyrmDT/fodasebot/blob/master/utils/palavras_ofensivas.txt).
Por fim, foi utilizado o script [filtrar_palavras_ofensivas.py](https://github.com/bartier/safadeza-generator/blob/master/utils/filtrar_palavras_ofensivas.py) para
percorrer o arquivo de verbos e palavras e gerar novos arquivos filtrados: [palavras_filtradas.txt](https://github.com/bartier/safadeza-generator/blob/master/utils/palavras_filtradas.txt)
e [verbos_filtrados.txt](https://github.com/bartier/safadeza-generator/blob/master/utils/verbos_filtrados.txt).
