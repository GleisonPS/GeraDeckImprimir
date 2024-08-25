# ImprimirDeckEduPro

O **ImprimirDeckEduPro** é uma ferramenta desenvolvida para facilitar a criação de materiais impressos de decks de cartas colecionáveis. Com este projeto, você pode importar arquivos de texto ou `.ydk`, baixar imagens de cartas de uma API, gerar um documento Word com as imagens no tamanho adequado, converter o documento para PDF e salvar o arquivo PDF em uma pasta específica.

## Funcionalidades

- **Importação de Arquivos**: Carregue arquivos `.txt` ou `.ydk` com a lista de cartas.
- **Baixa de Imagens**: Baixe imagens das cartas usando a API `https://images.ygoprodeck.com/images/cards/`.
- **Criação de Documento Word**: Insira as imagens em um documento Word (.docx) com tamanho padrão de 57 x 89 mm.
- **Conversão para PDF**: Converta o documento Word para PDF.
- **Salvar na Pasta Especificada**: Escolha uma pasta de destino para salvar o arquivo PDF gerado.
- **Interface Gráfica**: Utilize uma interface gráfica desenvolvida com Tkinter para interagir com o sistema.

## Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `Pillow`, `python-docx`, `pdfkit` ou `pypandoc`, `tkinter` (normalmente incluído com o Python)

## Instalação

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/imprimir-deck-edu-pro.git
   cd imprimir-deck-edu-pro
   ```

2. **Instale as Dependências**

   Crie um ambiente virtual e instale as bibliotecas necessárias:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Requisitos Adicionais**

   Dependendo do sistema operacional, você pode precisar instalar ferramentas adicionais para a conversão de documentos Word para PDF, como o `wkhtmltopdf` para `pdfkit` ou o `pandoc` para `pypandoc`.

## Uso

1. **Execute o Script**

   Execute o script principal para iniciar a interface gráfica:

   ```bash
   python main.py
   ```

2. **Carregue um Arquivo**

   Na interface gráfica, selecione um arquivo `.txt` ou `.ydk` contendo a lista de cartas.

3. **Escolha a Pasta de Destino**

   Selecione a pasta onde deseja salvar o arquivo PDF gerado.

4. **Processar e Gerar PDF**

   O sistema baixará as imagens das cartas, criará um documento Word e o converterá para PDF.

## Estrutura do Projeto

- `main.py`: Script principal que executa a interface gráfica e o processamento.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Documentação do projeto.

## Contribuição

Se você deseja contribuir para este projeto, por favor, siga as seguintes diretrizes:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature ou correção (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie a branch para o repositório (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Para quaisquer dúvidas ou suporte, entre em contato pelo Discord: toupeira21

Este README fornece uma visão geral do projeto, instruções de instalação e uso, além de orientações para contribuição e contato. Sinta-se à vontade para ajustar conforme suas necessidades e adicionar mais informações se necessário!
