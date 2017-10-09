esociallib Python library
=====================

A esociallib é uma biblioteca para ler e gerir documentos Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial). Ja existem varias outras bibliotecas, porem na Akretion queriamos algo que fosse simples de manter para usar com o ERP open source Odoo. A mdfeelib nao tem a pretençao de solucionar toda burocracia do SPED sozinha, mas apenas a questao da geraçao dos documentos de MDF-e. Tambem criamos outras bibliotecas semelhantes para os outros documentos electronicos do SPED.

A esociallib permite de:

* Gerir os XMLs dos documentos fiscais.
* Validar os dados com as mesmas validaçoes dos XSDs ao montar os objetos, o que evita detetar os erros apenas ao transmitir o XML.
* Importar XMLs e transfoma-los em objetos Python. Usando um sistema de sub-classes, fica facil mapear esses objetos em outros objetos ou adicionar qualquer metodo customizado.

A esociallib é:

* **Simples e confiavel**. O codigo é gerido pelo generateDS a partir dos XSD's da Fazenda usando o script generate de menos de **70 linhas de codigo** apenas.
* Compativel com **Python 2 e Python 3**.
* Capaz de carregar **varias versoes dos esquemas**. Isso pode ser bem util ao receber um documento com um layout antigo.
As tecnologias XML (XSD, WSDL, SOAP...) usadas pelo site da Fazenda foram criadas inicialmente para Java e .Net. Durante um bom tempo essas tecnologias ficaram para tras no mundo do Python. Por isso varias pessoas foram criar bibliotecas manualmente com milhares de linhas e poucos testes para montar os XMLs dos documentos electronicos. Mas hoje é um absurdo usar biblitecas escritas manualmente e depender do autor inicial a cada atualizaçao dos esquemas ou quando seu programa deve migrar para Python 3. Veja o conceito do 'Truck Factor' <https://en.wikipedia.org/wiki/Bus_factor>

É debativel qual é a melhor forma de transmitir esses documentos electronicos para o site da Fazenda (talvez com essas bibliotecas que ja existem, talvez com outras bibilotecas em Java especializadas em transmitir os documentos electronicos). Porem na questao de montar os XML e poder efetuar validaçoes dos dados o mais cedo possivel (perto do momento em qual o usuario preenchou os dados), dificilmente uma biblioteca de milhares de linhas escrita manualmente fica mais confiavel do que codigo gerido a partir dos XSD da Fazenda apenas. As classes da esociallib sao geridas usando a ferramenta generateDS. A funcionalidade de sub-classes do generateDS tambem ajuda na questao dos mapeamentos entre o modelo de dados dos esquemas da fazenda e o modelo de dados do seu software (ERP por examplo). Finalmente ficou possivel fazer com Python o que o pessoal do Java ja fazia ha muito tempo com as tecnologias do tipo JAXB.

Voce pode aprender mais sobre o generateDS.py aqui: <http://www.davekuhlman.org/generateDS.html>

como instalar
=============

.. code::

  pip install -e git+https://github.com/akretion/esociallib.git#egg=esociallib

como usar
=========

.. code::
:
  # TODO documentar melhor
