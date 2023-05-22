from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from esociallib.esocial.bindings.v1_1.org.w3.pkg_2000.pkg_09.xmldsig import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00"


class TsCondIng(Enum):
    """Condição de ingresso do trabalhador imigrante.

    Validação: Se {tmpResid}(./tmpResid) = [1], não pode ser informado [2, 5]. Se {tmpResid}(./tmpResid) = [2], não pode ser informado [1].

    :cvar VALUE_1: Refugiado
    :cvar VALUE_2: Solicitante de refúgio
    :cvar VALUE_3: Permanência no Brasil em razão de reunião familiar
    :cvar VALUE_4: Beneficiado pelo acordo entre países do Mercosul
    :cvar VALUE_5: Dependente de agente diplomático e/ou consular de
        países que mantêm acordo de reciprocidade para o exercício de
        atividade remunerada no Brasil
    :cvar VALUE_6: Beneficiado pelo Tratado de Amizade, Cooperação e
        Consulta entre a República Federativa do Brasil e a República
        Portuguesa
    :cvar VALUE_7: Outra condição
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class TsEstCivil(Enum):
    """
    :cvar VALUE_1: Solteiro
    :cvar VALUE_2: Casado
    :cvar VALUE_3: Divorciado
    :cvar VALUE_4: Separado
    :cvar VALUE_5: Viúvo
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TsGrauInstr(Enum):
    """
    Grau de instrução do trabalhador.

    :cvar VALUE_01: Analfabeto, inclusive o que, embora tenha recebido
        instrução, não se alfabetizou
    :cvar VALUE_02: Até o 5º ano incompleto do ensino fundamental
        (antiga 4ª série) ou que se tenha alfabetizado sem ter
        frequentado escola regular
    :cvar VALUE_03: 5º ano completo do ensino fundamental
    :cvar VALUE_04: Do 6º ao 9º ano do ensino fundamental incompleto
        (antiga 5ª a 8ª série)
    :cvar VALUE_05: Ensino fundamental completo
    :cvar VALUE_06: Ensino médio incompleto
    :cvar VALUE_07: Ensino médio completo
    :cvar VALUE_08: Educação superior incompleta
    :cvar VALUE_09: Educação superior completa
    :cvar VALUE_10: Pós-graduação completa
    :cvar VALUE_11: Mestrado completo
    :cvar VALUE_12: Doutorado completo
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"


class TsIndApurIr(Enum):
    """
    :cvar VALUE_0: Normal (apuração sob a folha de pagamento declarada
        no eSocial)
    :cvar VALUE_1: Situação especial de apuração de IR
    """
    VALUE_0 = 0
    VALUE_1 = 1


class TsIndApuracao(Enum):
    """
    Indicativo de período de apuração.

    :cvar VALUE_1: Mensal
    :cvar VALUE_2: Anual (13° salário)
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsIndGuia(Enum):
    """
    Indicativo do tipo de guia.

    :cvar VALUE_1: Documento de Arrecadação do eSocial - DAE
    """
    VALUE_1 = 1


class TsIndMv(Enum):
    """
    Indicador de desconto da contribuição previdenciária do trabalhador.

    :cvar VALUE_1: O declarante aplica a(s) alíquota(s) de desconto do
        segurado sobre a remuneração por ele informada (o percentual
        da(s) alíquota(s) será(ão) obtido(s) considerando a remuneração
        total do trabalhador)
    :cvar VALUE_2: O declarante aplica a(s) alíquota(s) de desconto do
        segurado sobre a diferença entre o limite máximo do salário de
        contribuição e a remuneração de outra(s) empresa(s) para as
        quais o trabalhador informou que houve o desconto
    :cvar VALUE_3: O declarante não realiza desconto do segurado, uma
        vez que houve desconto sobre o limite máximo de salário de
        contribuição em outra(s) empresa(s)
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsIndRetif(Enum):
    """
    Informe [1] para arquivo original ou [2] para arquivo de retificação.

    :cvar VALUE_1: Original
    :cvar VALUE_2: Retificação
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsIndSimples(Enum):
    """Indicador de contribuição substituída.

    Validação: O preenchimento do campo é obrigatório apenas no caso das empresas enquadradas no regime de tributação Simples Nacional, com tributação previdenciária substituída e não substituída ({classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [03]). Para os demais empregadores, não deve ser informado.

    :cvar VALUE_1: Contribuição substituída integralmente
    :cvar VALUE_2: Contribuição não substituída
    :cvar VALUE_3: Contribuição não substituída concomitante com
        contribuição substituída
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsNatAtividade(Enum):
    """Natureza da atividade.

    Validação: Se {codCateg}(../../infoContrato_codCateg) = [104], deve ser preenchido com [1]. Se {codCateg}(../../infoContrato_codCateg) = [102], deve ser preenchido com [2].

    :cvar VALUE_1: Trabalho urbano
    :cvar VALUE_2: Trabalho rural
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsProcEmi(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa
        Jurídica
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis -
        Empregador Doméstico
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_22 = 22


class TsProcEmi8(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_8: Aplicativo governamental para envio de eventos pelo
        Judiciário
    """
    VALUE_8 = 8


class TsProcEmiPf(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis -
        Empregador Doméstico
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_22 = 22


class TsProcEmiPj(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa
        Jurídica
    """
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_4 = 4


class TsProcEmiSem8(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa
        Jurídica
    :cvar VALUE_9: Aplicativo governamental - Integração com a Junta
        Comercial
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis -
        Empregador Doméstico
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_9 = 9
    VALUE_22 = 22


class TsProcEmiTodos(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa
        Jurídica
    :cvar VALUE_8: Aplicativo governamental para envio de eventos pelo
        Judiciário
    :cvar VALUE_9: Aplicativo governamental - Integração com a Junta
        Comercial
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis -
        Empregador Doméstico
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_22 = 22


class TsRacaCor(Enum):
    """
    :cvar VALUE_1: Branca
    :cvar VALUE_2: Preta
    :cvar VALUE_3: Parda
    :cvar VALUE_4: Amarela
    :cvar VALUE_5: Indígena
    :cvar VALUE_6: Não informado
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class TsSexo(Enum):
    """
    :cvar M: Masculino
    :cvar F: Feminino
    """
    M = "M"
    F = "F"


class TsSimNao(Enum):
    """
    :cvar S: Sim
    :cvar N: Não
    """
    S = "S"
    N = "N"


class TsTmpParc(Enum):
    """Preencher com o código relativo ao tipo de contrato em tempo parcial.

    Validação: O código [1] só é válido se {codCateg}(../codCateg) = [104]. Os códigos [2, 3] não são válidos se {codCateg}(../codCateg) = [104].

    :cvar VALUE_0: Não é contrato em tempo parcial
    :cvar VALUE_1: Limitado a 25 horas semanais
    :cvar VALUE_2: Limitado a 30 horas semanais
    :cvar VALUE_3: Limitado a 26 horas semanais
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsTmpResid(Enum):
    """
    :cvar VALUE_1: Prazo indeterminado
    :cvar VALUE_2: Prazo determinado
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsTpAmb(Enum):
    """
    Identificação do ambiente.

    :cvar VALUE_1: Produção
    :cvar VALUE_2: Produção restrita
    :cvar VALUE_7: Validação (uso interno)
    :cvar VALUE_8: Teste (uso interno)
    :cvar VALUE_9: Desenvolvimento (uso interno)
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class TsTpContr(Enum):
    """
    Tipo de contrato de trabalho.

    :cvar VALUE_1: Prazo indeterminado
    :cvar VALUE_2: Prazo determinado, definido em dias
    :cvar VALUE_3: Prazo determinado, vinculado à ocorrência de um fato
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsTpInsc1(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    """
    VALUE_1 = 1


class TsTpInsc12(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    :cvar VALUE_2: CPF
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsTpInsc134(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    :cvar VALUE_3: CAEPF
    :cvar VALUE_4: CNO
    """
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_4 = 4


class TsTpPlanRp(Enum):
    """
    Tipo de plano de segregação da massa.

    :cvar VALUE_0: Sem segregação da massa
    :cvar VALUE_1: Fundo em capitalização
    :cvar VALUE_2: Fundo em repartição
    :cvar VALUE_3: Mantido pelo Tesouro
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsTpProc12(Enum):
    """
    Preencher com o código correspondente ao tipo de processo.

    :cvar VALUE_1: Administrativo
    :cvar VALUE_2: Judicial
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsTpRegJor(Enum):
    """
    Regime de jornada do empregado.

    :cvar VALUE_1: Submetido a horário de trabalho (Capítulo II do
        Título II da CLT)
    :cvar VALUE_2: Atividade externa especificada no inciso I do art. 62
        da CLT
    :cvar VALUE_3: Função especificada no inciso II do art. 62 da CLT
    :cvar VALUE_4: Teletrabalho, previsto no inciso III do art. 62 da
        CLT
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TsTpRegPrev(Enum):
    """Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares
    das Forças Armadas).

    Validação: Se {codCateg}(./infoContrato_codCateg) = [104], deve ser preenchido com [1]. Se {codCateg}(./infoContrato_codCateg) = [101, 102, 103, 105, 106, 107, 108, 111], não pode ser preenchido com [2, 4].

    :cvar VALUE_1: Regime Geral de Previdência Social - RGPS
    :cvar VALUE_2: Regime Próprio de Previdência Social - RPPS
    :cvar VALUE_3: Regime de Previdência Social no exterior
    :cvar VALUE_4: Sistema de Proteção Social dos Militares das Forças
        Armadas - SPSMFA
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TsTpRegTrab(Enum):
    """
    Tipo de regime trabalhista.

    :cvar VALUE_1: CLT - Consolidação das Leis de Trabalho e legislações
        trabalhistas específicas
    :cvar VALUE_2: Estatutário/legislações específicas (servidor
        temporário, militar, agente político, etc.)
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsTpTrib(Enum):
    """
    Abrangência da decisão.

    :cvar VALUE_1: IRRF
    :cvar VALUE_2: Contribuições sociais do trabalhador
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsUf(Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MT = "MT"
    MS = "MS"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"


class TsUndSalFixo(Enum):
    """
    Unidade de pagamento da parte fixa da remuneração.

    :cvar VALUE_1: Por hora
    :cvar VALUE_2: Por dia
    :cvar VALUE_3: Por semana
    :cvar VALUE_4: Por quinzena
    :cvar VALUE_5: Por mês
    :cvar VALUE_6: Por tarefa
    :cvar VALUE_7: Não aplicável - Salário exclusivamente variável
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


@dataclass
class TAlvaraJudicial:
    """
    :ivar nrProcJud: Preencher com o número do processo judicial.
        Validação: Deve ser um número de processo judicial válido.
    """
    class Meta:
        name = "T_alvaraJudicial"

    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )


@dataclass
class TContato:
    class Meta:
        name = "T_contato"

    fonePrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        }
    )
    emailPrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 6,
            "max_length": 60,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TEnderecoExterior:
    """Endereço no exterior.

    CONDICAO_GRUPO: O (se não informado o grupo {brasil}(../brasil)); N (nos demais casos)

    :ivar paisResid: Preencher com o código do país. Validação: Deve ser
        um código válido e existente na Tabela 06.
    :ivar dscLograd:
    :ivar nrLograd:
    :ivar complemento:
    :ivar bairro:
    :ivar nmCid:
    :ivar codPostal:
    """
    class Meta:
        name = "T_endereco_exterior"

    paisResid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "pattern": r".*[^\s].*",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    nmCid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 2,
            "max_length": 50,
            "pattern": r".*[^\s].*",
        }
    )
    codPostal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 4,
            "max_length": 12,
            "pattern": r".*[^\s].*",
        }
    )


class THorContratualTpJornada(Enum):
    """
    Tipo de jornada.

    :cvar VALUE_2: Jornada 12 x 36 (12 horas de trabalho seguidas de 36
        horas ininterruptas de descanso)
    :cvar VALUE_3: Jornada com horário diário fixo e folga variável
    :cvar VALUE_4: Jornada com horário diário fixo e folga fixa (no
        domingo)
    :cvar VALUE_5: Jornada com horário diário fixo e folga fixa (exceto
        no domingo)
    :cvar VALUE_6: Jornada com horário diário fixo e folga fixa (em
        outro dia da semana), com folga adicional periódica no domingo
    :cvar VALUE_7: Turno ininterrupto de revezamento
    :cvar VALUE_9: Demais tipos de jornada
    """
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_9 = 9


@dataclass
class TIdeBeneficio:
    """Identificação do beneficiário e do benefício.

    CHAVE_GRUPO: {cpfBenef*}, {nrBeneficio*}

    :ivar cpfBenef: Informar o CPF do beneficiário.
    :ivar nrBeneficio: Número do benefício.
    """
    class Meta:
        name = "T_ideBeneficio"

    cpfBenef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoRetornoMensal:
    """Identificação do evento de retorno.

    Evento de origem: S-1299.
    CHAVE_GRUPO: {perApur*}

    :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência
        das informações.
    """
    class Meta:
        name = "T_ideEvento_retorno_mensal"

    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )


@dataclass
class TIdeTrabSemVinculo:
    """Identificação do TSVE.

    DESCRICAO_COMPLETA:Identificação do Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE.
    CHAVE_GRUPO: {cpfTrab*}, {matricula*}, {codCateg*}

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa.
        Validação: Deve corresponder à matrícula informada pelo
        empregador no evento S-2300 do respectivo contrato. Não
        preencher no caso de TSVE sem informação de matrícula no evento
        S-2300.
    :ivar codCateg: Preencher com o código da categoria do trabalhador.
        Informar somente no caso de TSVE sem informação de matrícula no
        evento S-2300. Validação: Informação obrigatória e exclusiva se
        não houver preenchimento de {matricula}(./matricula). Se
        informado, deve ser um código válido e existente na Tabela 01.
    """
    class Meta:
        name = "T_ideTrabSemVinculo"

    cpfTrab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "pattern": r"\d{3}",
        }
    )


@dataclass
class TIdeVinculo:
    """Informações de identificação do trabalhador e do vínculo.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou,
        no caso de servidor público, a matrícula constante no Sistema de
        Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento
        S-2200 do respectivo vínculo trabalhista.
    """
    class Meta:
        name = "T_ideVinculo"

    cpfTrab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeVinculoBaixa:
    """Informações de identificação do trabalhador e do vínculo.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou,
        no caso de servidor público, a matrícula constante no Sistema de
        Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento
        S-2190 ou S-2200 do respectivo vínculo trabalhista.
    """
    class Meta:
        name = "T_ideVinculo_baixa"

    cpfTrab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeVinculoSst:
    """Informações de identificação do trabalhador e do vínculo.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}, {codCateg*}

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou,
        no caso de servidor público, a matrícula constante no Sistema de
        Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento
        S-2190, S-2200 ou S-2300 do respectivo contrato. Não preencher
        no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE
        sem informação de matrícula no evento S-2300.
    :ivar codCateg: Preencher com o código da categoria do trabalhador.
        Informar somente no caso de TSVE sem informação de matrícula no
        evento S-2300. Validação: Informação obrigatória e exclusiva se
        não houver preenchimento de {matricula}(./matricula). Se
        informado, deve ser um código válido e existente na Tabela 01.
    """
    class Meta:
        name = "T_ideVinculo_sst"

    cpfTrab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "pattern": r"\d{3}",
        }
    )


class TInfoEstagiarioNatEstagio(Enum):
    """Natureza do estágio ou da prestação de serviço civil voluntário.

    Validação: Se o código de categoria for igual a [906], deve ser preenchido com [N].

    :cvar O: Obrigatório
    :cvar N: Não obrigatório
    """
    O = "O"
    N = "N"


class TInfoEstagiarioNivEstagio(Enum):
    """Informar o nível do estágio ou da prestação de serviço civil voluntário.

    Validação: Preenchimento obrigatório se o código de categoria for igual a [901]. Se o código de categoria for igual a [906], não pode ser informado [9].

    :cvar VALUE_1: Fundamental
    :cvar VALUE_2: Médio
    :cvar VALUE_3: Formação profissional
    :cvar VALUE_4: Superior
    :cvar VALUE_8: Especial
    :cvar VALUE_9: Mãe social (Lei 7.644/1987)
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_9 = 9


@dataclass
class TInfoInterm:
    class Meta:
        name = "T_infoInterm"

    dia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "31",
            "pattern": r"\d{1,2}",
        }
    )


@dataclass
class TNascimento:
    """
    Grupo de informações do nascimento do trabalhador.

    :ivar dtNascto: Preencher com a data de nascimento.
    :ivar paisNascto: Preencher com o código do país de nascimento do
        trabalhador. Validação: Deve ser um código válido e existente na
        Tabela 06.
    :ivar paisNac:
    """
    class Meta:
        name = "T_nascimento"

    dtNascto: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    paisNascto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    paisNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )


@dataclass
class TNovaValidade:
    """Novo período de validade das informações.

    DESCRICAO_COMPLETA:Informação preenchida exclusivamente em caso de alteração do período de validade das informações, apresentando o novo período de validade.
    CONDICAO_GRUPO: OC
    """
    class Meta:
        name = "T_novaValidade"

    iniValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )


@dataclass
class TTreiCap:
    class Meta:
        name = "T_treiCap"

    codTreiCap: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{4}",
        }
    )


class InfoCeletistaIndAdmissao(Enum):
    """
    Indicativo de admissão.

    :cvar VALUE_1: Normal
    :cvar VALUE_2: Decorrente de ação fiscal
    :cvar VALUE_3: Decorrente de decisão judicial
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoCeletistaTpAdmissao(Enum):
    """Tipo de admissão do trabalhador.

    Validação: Se for igual a [5], {codCateg}(2200_vinculo_infoContrato_codCateg) deve ser igual a [104] e {procEmi}(2200_ideEvento_procEmi) deve ser igual a [2, 22].
    Se for igual a [6], {cadIni}(2200_vinculo_cadIni) deve ser igual a [N].

    :cvar VALUE_1: Admissão
    :cvar VALUE_2: Transferência de empresa do mesmo grupo econômico ou
        transferência entre órgãos do mesmo Ente Federativo
    :cvar VALUE_3: Transferência de empresa consorciada ou de consórcio
    :cvar VALUE_4: Transferência por motivo de sucessão, incorporação,
        cisão ou fusão
    :cvar VALUE_5: Transferência do empregado doméstico para outro
        representante da mesma unidade familiar
    :cvar VALUE_6: Mudança de CPF
    :cvar VALUE_7: Transferência quando a empresa sucedida é considerada
        inapta por inexistência de fato
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class InfoEstatutarioTpProv(Enum):
    """Preencher com o tipo de provimento.

    Validação: Os valores [3, 5, 6, 7, 8, 9] só são permitidos se a natureza jurídica do declarante for Administração Pública (grupo [1]).
    Se {codCateg}(2200_vinculo_infoContrato_codCateg) = [302], deve ser preenchido com [2, 5, 8, 10].

    :cvar VALUE_1: Nomeação em cargo efetivo
    :cvar VALUE_2: Nomeação exclusivamente em cargo em comissão
    :cvar VALUE_3: Incorporação, matrícula ou nomeação (militar)
    :cvar VALUE_5: Redistribuição ou Reforma Administrativa
    :cvar VALUE_6: Diplomação
    :cvar VALUE_7: Contratação por tempo determinado
    :cvar VALUE_8: Remoção (em caso de alteração do órgão declarante)
    :cvar VALUE_9: Designação
    :cvar VALUE_10: Mudança de CPF
    :cvar VALUE_11: Estabilizados - Art. 19 do ADCT
    :cvar VALUE_99: Outros não relacionados acima
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_99 = 99


class SucessaoVincTpInsc(Enum):
    """Preencher com o código correspondente ao tipo de inscrição, conforme Tabela
    05.

    Validação: Somente é possível informar [5] se {dtTransf}(./dtTransf) for igual ou anterior a [1999-06-30].
    Somente é possível informar [6] se {dtTransf}(./dtTransf) for igual ou anterior a [2011-12-31].

    :cvar VALUE_1: CNPJ
    :cvar VALUE_2: CPF
    :cvar VALUE_5: CGC
    :cvar VALUE_6: CEI
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_5 = 5
    VALUE_6 = 6


class TrabTemporarioHipLeg(Enum):
    """
    Hipótese legal para contratação de trabalhador temporário.

    :cvar VALUE_1: Necessidade de substituição transitória de pessoal
        permanente
    :cvar VALUE_2: Demanda complementar de serviços
    """
    VALUE_1 = 1
    VALUE_2 = 2


class VinculoCadIni(Enum):
    """
    Indicar se o evento se refere a cadastramento inicial de vínculo (o ingresso do
    trabalhador no empregador declarante, por admissão ou transferência, é anterior
    à data de início da obrigatoriedade de envio de seus eventos não periódicos) ou
    se refere a admissão (o ingresso do trabalhador no empregador declarante é
    igual ou posterior à data de início de obrigatoriedade de envio de seus eventos
    não periódicos).

    :cvar S: Sim (Cadastramento Inicial)
    :cvar N: Não (Admissão)
    """
    S = "S"
    N = "N"


@dataclass
class TAprend:
    """
    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do estabelecimento para
        o qual a contratação de aprendiz foi efetivada, de acordo com o
        tipo de inscrição indicado no campo {aprend/tpInsc}(./tpInsc).
        Validação: Deve ser um identificador válido e: a) Se
        {aprend/tpInsc}(./tpInsc) = [1], deve ser informado com 14
        (catorze) algarismos. Se o empregador for pessoa jurídica, a
        raiz do CNPJ informado deve ser diferente de
        {ideEmpregador/nrInsc}(/ideEmpregador_nrInsc). b) Se
        {aprend/tpInsc}(./tpInsc) = [2], deve ser diferente do CPF do
        empregado. Se o empregador for pessoa física, também deve ser
        diferente do CPF do empregador.
    """
    class Meta:
        name = "T_aprend"

    tpInsc: Optional[TsTpInsc12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )


@dataclass
class TEnderecoBrasil:
    """Endereço no Brasil.

    CONDICAO_GRUPO: O (se não informado o grupo {exterior}(../exterior)); N (nos demais casos)

    :ivar tpLograd:
    :ivar dscLograd:
    :ivar nrLograd:
    :ivar complemento:
    :ivar bairro:
    :ivar cep:
    :ivar codMunic:
    :ivar uf: Preencher com a sigla da Unidade da Federação - UF.
    """
    class Meta:
        name = "T_endereco_brasil"

    tpLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "pattern": r".*[^\s].*",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}",
        }
    )
    codMunic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{7}",
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class THorContratual:
    """
    :ivar qtdHrsSem:
    :ivar tpJornada:
    :ivar tmpParc:
    :ivar horNoturno: Indicar se a jornada semanal possui horário
        noturno (no todo ou em parte). Validação: Informação obrigatória
        se {codCateg}(../codCateg) for diferente de [111].
    :ivar dscJorn: Descrição da jornada semanal contratual, contendo os
        dias da semana e os respectivos horários contratuais (entrada,
        saída e intervalos).
    """
    class Meta:
        name = "T_horContratual"

    qtdHrsSem: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    tpJornada: Optional[THorContratualTpJornada] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    tmpParc: Optional[TsTmpParc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    horNoturno: Optional[TsSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    dscJorn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 999,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )


@dataclass
class TIdeEmpregador:
    """Informações de identificação do empregador.

    CHAVE_GRUPO: {tpInsc*}, {nrInsc*}

    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do contribuinte de
        acordo com o tipo de inscrição indicado no campo
        {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em S-1000.
    """
    class Meta:
        name = "T_ideEmpregador"

    tpInsc: Optional[TsTpInsc12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}|\d{11}|\d{14}",
        }
    )


@dataclass
class TIdeEmpregadorCnpj:
    """Informações de identificação do empregador.

    CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
    """
    class Meta:
        name = "T_ideEmpregador_cnpj"

    tpInsc: Optional[TsTpInsc1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}|\d{14}",
        }
    )


@dataclass
class TIdeEmpregadorExclusao:
    """Informações de identificação do empregador.

    CHAVE_GRUPO: {tpInsc}, {nrInsc}

    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do contribuinte de
        acordo com o tipo de inscrição indicado no campo
        {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em S-1000.
    """
    class Meta:
        name = "T_ideEmpregador_exclusao"

    tpInsc: Optional[TsTpInsc12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}|\d{11}|\d{14}",
        }
    )


@dataclass
class TIdeEventoEvtTab:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_evtTab"

    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoEvtTabInicial:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_evtTab_inicial"

    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoExclusao:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_exclusao"

    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiTodos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoExclusaoProcTrab:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_exclusao_proc_trab"

    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoFolha:
    """Informações de identificação do evento.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}, {indGuia*}
    """
    class Meta:
        name = "T_ideEvento_folha"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoFolhaMensal:
    """Informações de identificação do evento.

    CHAVE_GRUPO: {perApur*}, {indGuia*}
    """
    class Meta:
        name = "T_ideEvento_folha_mensal"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoFolhaMensalPf:
    """Informações de identificação do evento.

    CHAVE_GRUPO: {perApur*}, {indGuia*}
    """
    class Meta:
        name = "T_ideEvento_folha_mensal_PF"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoFolhaOpp:
    """Informações de identificação do evento.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}
    """
    class Meta:
        name = "T_ideEvento_folha_opp"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoFolhaSemRetificacao:
    """Informações de identificação do evento.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}, {indGuia*}
    """
    class Meta:
        name = "T_ideEvento_folha_sem_retificacao"

    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoRetornoContrib:
    """Identificação do evento de retorno.

    Evento de origem: S-1299.
    CHAVE_GRUPO: {indApuracao*}, {perApur*}

    :ivar indApuracao:
    :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência
        das informações, se {indApuracao}(./indApuracao) for igual a
        [1], ou apenas o ano (formato AAAA), se
        {indApuracao}(./indApuracao) for igual a [2].
    """
    class Meta:
        name = "T_ideEvento_retorno_contrib"

    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )


@dataclass
class TIdeEventoRetornoTrab:
    """Identificação do evento de retorno.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}

    :ivar nrRecArqBase: Preencher com o número do recibo do arquivo que
        deu origem ao presente arquivo de retorno ao empregador.
        Validação: Deve ser um recibo de entrega válido, correspondente
        ao arquivo que deu origem ao presente arquivo de retorno
        (S-1200, S-2299, S-2399 ou S-3000).
    :ivar indApuracao:
    :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência
        das informações, se {indApuracao}(./indApuracao) for igual a
        [1], ou apenas o ano (formato AAAA), se
        {indApuracao}(./indApuracao) for igual a [2].
    """
    class Meta:
        name = "T_ideEvento_retorno_trab"

    nrRecArqBase: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )


@dataclass
class TIdeEventoTrab:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_trab"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoTrabPj:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_trab_PJ"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoTrabAdmissao:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_trab_admissao"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoTrabIndGuia:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_trab_indGuia"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TIdeEventoTrabJud:
    """
    Informações de identificação do evento.
    """
    class Meta:
        name = "T_ideEvento_trab_jud"

    indRetif: Optional[TsIndRetif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass
class TInfoEstagiario:
    """
    :ivar natEstagio:
    :ivar nivEstagio:
    :ivar areaAtuacao: Área de atuação do estagiário ou, no caso de
        prestação de serviço civil voluntário, jornada semanal do
        desempenho de atividades em formato decimal.
    :ivar nrApol: Número da apólice de seguro.
    :ivar dtPrevTerm: Data prevista para o término do estágio ou da
        prestação de serviço civil voluntário. Validação: Deve ser uma
        data posterior à data de início do estágio ou da prestação de
        serviço civil voluntário.
    :ivar instEnsino: Instituição de ensino ou entidade de
        formação/qualificação.
    :ivar ageIntegracao: Agente de integração. CONDICAO_GRUPO: OC (se o
        código de categoria for igual a [901]); N (nos demais casos)
    :ivar supervisorEstagio: Supervisor do estágio. CONDICAO_GRUPO: OC
        (se o código de categoria for igual a [901]); N (nos demais
        casos)
    """
    class Meta:
        name = "T_infoEstagiario"

    natEstagio: Optional[TInfoEstagiarioNatEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nivEstagio: Optional[TInfoEstagiarioNivEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    areaAtuacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrApol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtPrevTerm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    instEnsino: Optional["TInfoEstagiario.InstEnsino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    ageIntegracao: Optional["TInfoEstagiario.AgeIntegracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    supervisorEstagio: Optional["TInfoEstagiario.SupervisorEstagio"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )

    @dataclass
    class InstEnsino:
        """
        :ivar cnpjInstEnsino: Preencher com o CNPJ da instituição de
            ensino, no caso de estágio, ou da entidade de
            formação/qualificação, no caso de prestação de serviço civil
            voluntário. Deve ser preenchido apenas se a
            instituição/entidade for brasileira. Validação: Se
            informado, deve ser um CNPJ válido, com 14 (catorze)
            algarismos.
        :ivar nmRazao: Informar a razão social. Validação: Preenchimento
            obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar dscLograd: Descrição do logradouro. Validação:
            Preenchimento obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar nrLograd: Número do logradouro. Se não houver número a ser
            informado, preencher com "S/N". Validação: Preenchimento
            obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar bairro: Nome do bairro/distrito. Validação: Preenchimento
            obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar cep: Código de Endereçamento Postal - CEP. Validação: Não
            informar se o campo {cnpjInstEnsino}(./cnpjInstEnsino)
            estiver preenchido. Se informado, deve ser preenchido apenas
            com números, com 8 (oito) posições.
        :ivar codMunic: Preencher com o código do município, conforme
            tabela do IBGE. Validação: Não informar se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) estiver preenchido. Se
            informado, deve ser um código válido e existente na tabela
            do IBGE.
        :ivar uf: Preencher com a sigla da Unidade da Federação - UF.
            Validação: Não informar se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) estiver preenchido.
        """
        cnpjInstEnsino: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "pattern": r"\d{14}",
            }
        )
        nmRazao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        dscLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        nrLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            }
        )
        bairro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            }
        )
        cep: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "pattern": r"\d{8}",
            }
        )
        codMunic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "pattern": r"\d{7}",
            }
        )
        uf: Optional[TsUf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            }
        )

    @dataclass
    class AgeIntegracao:
        """
        :ivar cnpjAgntInteg: CNPJ do agente de integração. Validação:
            Deve ser um CNPJ válido, com 14 (catorze) algarismos.
        """
        cnpjAgntInteg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{14}",
            }
        )

    @dataclass
    class SupervisorEstagio:
        """
        :ivar cpfSupervisor: CPF do responsável pela supervisão do
            estagiário. Validação: Deve ser um CPF válido.
        """
        cpfSupervisor: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}",
            }
        )


@dataclass
class TInfoMv:
    """Informação de múltiplos vínculos DESCRICAO_COMPLETA:Grupo preenchido
    exclusivamente em caso de trabalhador que possua outros vínculos/atividades nos
    quais já tenha ocorrido desconto de contribuição previdenciária.

    CONDICAO_GRUPO: OC

    :ivar indMV:
    :ivar remunOutrEmpr: Remuneração recebida pelo trabalhador em outras
        empresas ou atividades DESCRICAO_COMPLETA:Informações relativas
        ao trabalhador que possui vínculo empregatício com outra(s)
        empresa(s) e/ou que exerce outras atividades como contribuinte
        individual, detalhando as empresas que efetuaram (ou efetuarão)
        desconto da contribuição. CHAVE_GRUPO: {tpInsc}, {nrInsc},
        {codCateg}
    """
    class Meta:
        name = "T_infoMV"

    indMV: Optional[TsIndMv] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    remunOutrEmpr: List["TInfoMv.RemunOutrEmpr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )

    @dataclass
    class RemunOutrEmpr:
        """
        :ivar tpInsc:
        :ivar nrInsc: Informar o número de inscrição do contribuinte de
            acordo com o tipo de inscrição indicado no campo
            {remunOutrEmpr/tpInsc}(./tpInsc). Validação: a) Se
            {remunOutrEmpr/tpInsc}(./tpInsc) = [1], deve ser um CNPJ
            válido, diferente do CNPJ base indicado no evento de
            Informações do Empregador (S-1000) e dos estabelecimentos
            informados através do evento S-1005. b) Se
            {remunOutrEmpr/tpInsc}(./tpInsc) = [2], deve ser um CPF
            válido e diferente do CPF do trabalhador e ainda, caso o
            empregador seja pessoa física, diferente do CPF do
            empregador.
        :ivar codCateg:
        :ivar vlrRemunOE:
        """
        tpInsc: Optional[TsTpInsc12] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "min_exclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )


@dataclass
class TInfoRra:
    """Informações complementares de RRA.

    DESCRICAO_COMPLETA:Informações complementares relativas a Rendimentos Recebidos Acumuladamente - RRA.
    CONDICAO_GRUPO: O (se {indRRA}(../indRRA) = [S]); N (nos demais casos)

    :ivar tpProcRRA:
    :ivar nrProcRRA: Informar o número do processo/requerimento
        administrativo/judicial. Validação: Informação obrigatória se
        {tpProcRRA}(./tpProcRRA) = [2] e opcional se
        {tpProcRRA}(./tpProcRRA) = [1]. Deve ser número de processo
        válido e: a) Se {tpProcRRA}(./tpProcRRA) = [1], deve possuir 17
        (dezessete) ou 21 (vinte e um) algarismos; b) Se
        {tpProcRRA}(./tpProcRRA) = [2], deve possuir 20 (vinte)
        algarismos.
    :ivar descRRA:
    :ivar qtdMesesRRA:
    :ivar despProcJud:
    :ivar ideAdv: Identificação dos advogados. CHAVE_GRUPO: {tpInsc},
        {nrInsc} CONDICAO_GRUPO: OC
    """
    class Meta:
        name = "T_infoRRA"

    tpProcRRA: Optional[TsTpProc12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        }
    )
    descRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "pattern": r".*[^\s].*",
        }
    )
    qtdMesesRRA: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999.9"),
            "total_digits": 4,
            "fraction_digits": 1,
        }
    )
    despProcJud: Optional["TInfoRra.DespProcJud"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
        }
    )
    ideAdv: List["TInfoRra.IdeAdv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "max_occurs": 99,
        }
    )

    @dataclass
    class DespProcJud:
        """Despesas com processo judicial DESCRICAO_COMPLETA:Detalhamento das despesas
        com processo judicial.

        CONDICAO_GRUPO: OC

        :ivar vlrDespCustas: Preencher com o valor das despesas com
            custas judiciais.
        :ivar vlrDespAdvogados: Preencher com o valor total das despesas
            com advogado(s).
        """
        vlrDespCustas: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )
        vlrDespAdvogados: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )

    @dataclass
    class IdeAdv:
        """
        :ivar tpInsc: Preencher com o código correspondente ao tipo de
            inscrição, conforme Tabela 05.
        :ivar nrInsc: Informar o número de inscrição do advogado.
            Validação: Deve ser um número de inscrição válido, de acordo
            com o tipo de inscrição indicado no campo
            {ideAdv/tpInsc}(./tpInsc), considerando as particularidades
            aplicadas à informação de CNPJ de órgão público em S-1000.
            Se {ideAdv/tpInsc}(./tpInsc) = [1], deve possuir 14
            (catorze) algarismos e, no caso de declarante pessoa
            jurídica, ser diferente do CNPJ base do empregador (exceto
            se {ideEmpregador/nrInsc}(/ideEmpregador_nrInsc) tiver 14
            (catorze) algarismos). Se {ideAdv/tpInsc}(./tpInsc) = [2],
            deve possuir 11 (onze) algarismos e, no caso de declarante
            pessoa física, ser diferente do CPF do empregador.
        :ivar vlrAdv: Valor da despesa com o advogado, se houver.
        """
        tpInsc: Optional[TsTpInsc12] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )


@dataclass
class TInfoSimples:
    """Informação relativa a empresas do Simples DESCRICAO_COMPLETA:Informação
    relativa a empresas enquadradas no regime de tributação Simples Nacional.

    CONDICAO_GRUPO: O (se {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [03]); N (nos demais casos)

    :ivar indSimples: Indicador de contribuição substituída.
    """
    class Meta:
        name = "T_infoSimples"

    indSimples: Optional[TsIndSimples] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class TItensRemunRpps:
    """
    Itens da remuneração do trabalhador DESCRICAO_COMPLETA:Rubricas que compõem a
    remuneração do trabalhador.

    :ivar codRubr: Informar o código atribuído pelo empregador que
        identifica a rubrica em sua folha de pagamento.
    :ivar ideTabRubr:
    :ivar qtdRubr: Informar a quantidade de referência para apuração (em
        horas, cotas, meses, etc.). Validação: Deve ser maior que 0
        (zero).
    :ivar fatorRubr: Informar o fator, percentual, etc. da rubrica,
        quando necessário. Validação: Deve ser maior que 0 (zero).
    :ivar vrRubr:
    :ivar indApurIR: Indicativo de tipo de apuração de IR.
    """
    class Meta:
        name = "T_itensRemun_rpps"

    codRubr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    ideTabRubr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_length": 1,
            "max_length": 8,
            "pattern": r".*[^\s].*",
        }
    )
    qtdRubr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999.99"),
            "total_digits": 12,
            "fraction_digits": 2,
        }
    )
    fatorRubr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    vrRubr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    indApurIR: Optional[TsIndApurIr] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class TLocalTrabGeral:
    """
    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do contribuinte de
        acordo com o tipo de inscrição indicado no campo
        {localTrabGeral/tpInsc}(./tpInsc). Validação: Deve ser um número
        de inscrição válido e existente na Tabela de Estabelecimentos
        (S-1005), bem como compatível com
        {localTrabGeral/tpInsc}(./tpInsc).
    :ivar descComp:
    """
    class Meta:
        name = "T_localTrabGeral"

    tpInsc: Optional[TsTpInsc134] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 80,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )


@dataclass
class TProcJudTrab:
    """Informações sobre a existência de processos judiciais do trabalhador
    DESCRICAO_COMPLETA:Informações sobre a existência de processos judiciais do
    trabalhador com decisão favorável quanto à não incidência de contribuições
    sociais e/ou Imposto de Renda.

    CHAVE_GRUPO: {tpTrib}, {nrProcJud}, {codSusp}
    CONDICAO_GRUPO: OC
    """
    class Meta:
        name = "T_procJudTrab"

    tpTrib: Optional[TsTpTrib] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )
    codSusp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{1,14}",
        }
    )


@dataclass
class TRemuneracao:
    """
    :ivar vrSalFx:
    :ivar undSalFixo:
    :ivar dscSalVar: Descrição do salário por tarefa ou variável e como
        este é calculado. Ex.: Comissões pagas no percentual de 10%
        sobre as vendas. Validação: Preenchimento obrigatório se
        {undSalFixo}(./undSalFixo) for igual a [6, 7].
    """
    class Meta:
        name = "T_remuneracao"

    vrSalFx: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    undSalFixo: Optional[TsUndSalFixo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    dscSalVar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 999,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )


@dataclass
class TSucessaoVinc:
    """
    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do empregador anterior,
        de acordo com o tipo de inscrição indicado no campo
        {sucessaoVinc/tpInsc}(./tpInsc).
    :ivar matricAnt: Matrícula do trabalhador no empregador anterior.
    :ivar dtAdm: Preencher com a data de admissão do trabalhador. No
        caso de transferência do empregado, deve ser preenchida a data
        inicial do vínculo no primeiro empregador (data de início do
        vínculo).
    """
    class Meta:
        name = "T_sucessaoVinc"

    tpInsc: Optional[TsTpInsc12] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtAdm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class ESocial:
    """S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador

    :ivar evtAdmissao: Evento Cadastramento Inicial do Vínculo e
        Admissão/Ingresso de Trabalhador. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ADMISSAO_POSTERIOR_INICIO_ATIVIDADES
        REGRA:REGRA_ADMISSAO_VALIDA_DT_ADM
        REGRA:REGRA_ADMISSAO_VALIDA_DURACAO_CONTRATO
        REGRA:REGRA_BLOQUEIA_USO_CPF_EMPREGADOR
        REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB
        REGRA:REGRA_COMPATIB_CATEG_EVENTO
        REGRA:REGRA_EMPREGADO_DOMESTICO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EVETRAB_VALIDA_OPCAO_FGTS
        REGRA:REGRA_EXCLUSAO_ADMISSAO_TSVE_INICIO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_DOMESTICO
        REGRA:REGRA_EXTEMP_REINTEGRACAO
        REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB
        REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_MUDANCA_CPF
        REGRA:REGRA_REGISTRO_PRELIMINAR
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_MATRICULA
        REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar signature:
    """
    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_01_00"

    evtAdmissao: Optional["ESocial.EvtAdmissao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )

    @dataclass
    class EvtAdmissao:
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar trabalhador: Informações pessoais do trabalhador.
            CHAVE_GRUPO: {cpfTrab*}
        :ivar vinculo: Informações do vínculo. DESCRICAO_COMPLETA:Grupo
            de informações do vínculo. CHAVE_GRUPO: {matricula*}
        :ivar Id:
        """
        ideEvento: Optional[TIdeEventoTrabAdmissao] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        ideEmpregador: Optional[TIdeEmpregador] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        trabalhador: Optional["ESocial.EvtAdmissao.Trabalhador"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        vinculo: Optional["ESocial.EvtAdmissao.Vinculo"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "length": 36,
                "pattern": r"ID\d{34}",
            }
        )

        @dataclass
        class Trabalhador:
            """
            :ivar cpfTrab:
            :ivar nmTrab:
            :ivar sexo:
            :ivar racaCor:
            :ivar estCiv:
            :ivar grauInstr:
            :ivar nmSoc:
            :ivar nascimento:
            :ivar endereco: Endereço do trabalhador
                DESCRICAO_COMPLETA:Grupo de informações do endereço do
                trabalhador. CONDICAO_GRUPO: O (se grupo
                {desligamento}(2200_vinculo_desligamento) não estiver
                preenchido); F (nos demais casos)
            :ivar trabImig: Informações do trabalhador imigrante.
                CONDICAO_GRUPO: N (se
                {paisNac}(2200_trabalhador_nascimento_paisNac) = [105]);
                OC (se {paisNac}(2200_trabalhador_nascimento_paisNac)
                for diferente de [105]) e se grupo
                {desligamento}(2200_vinculo_desligamento) não estiver
                preenchido); F (nos demais casos)
            :ivar infoDeficiencia: Pessoa com deficiência.
                CONDICAO_GRUPO: OC (se grupo
                {desligamento}(2200_vinculo_desligamento) não estiver
                preenchido); F (nos demais casos)
            :ivar dependente: Informações dos dependentes. CHAVE_GRUPO:
                {tpDep}, {nmDep}, {dtNascto} CONDICAO_GRUPO: OC
            :ivar contato: Informações de contato. CONDICAO_GRUPO: OC
                (se grupo {desligamento}(2200_vinculo_desligamento) não
                estiver preenchido); F (nos demais casos)
            """
            cpfTrab: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"\d{11}",
                }
            )
            nmTrab: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 2,
                    "max_length": 70,
                    "pattern": r".*[^\s].*",
                }
            )
            sexo: Optional[TsSexo] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            racaCor: Optional[TsRacaCor] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            estCiv: Optional[TsEstCivil] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            grauInstr: Optional[TsGrauInstr] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            nmSoc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 2,
                    "max_length": 70,
                    "pattern": r".*[^\s].*",
                }
            )
            nascimento: Optional[TNascimento] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            endereco: Optional["ESocial.EvtAdmissao.Trabalhador.Endereco"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            trabImig: Optional["ESocial.EvtAdmissao.Trabalhador.TrabImig"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            infoDeficiencia: Optional["ESocial.EvtAdmissao.Trabalhador.InfoDeficiencia"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            dependente: List["ESocial.EvtAdmissao.Trabalhador.Dependente"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                }
            )
            contato: Optional[TContato] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )

            @dataclass
            class Endereco:
                """
                :ivar brasil: Endereço no Brasil. CONDICAO_GRUPO: O (se
                    não informados os grupos
                    {exterior}(2200_trabalhador_endereco_exterior) e
                    {desligamento}(2200_vinculo_desligamento)); N (se
                    grupo {exterior}(2200_trabalhador_endereco_exterior)
                    estiver preenchido); F (nos demais casos)
                :ivar exterior: Endereço no exterior. CONDICAO_GRUPO: O
                    (se não informados os grupos
                    {brasil}(2200_trabalhador_endereco_brasil) e
                    {desligamento}(2200_vinculo_desligamento)); N (se
                    grupo {brasil}(2200_trabalhador_endereco_brasil)
                    estiver preenchido); F (nos demais casos)
                """
                brasil: Optional[TEnderecoBrasil] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                exterior: Optional[TEnderecoExterior] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass
            class TrabImig:
                """
                :ivar tmpResid: Tempo de residência do trabalhador
                    imigrante. Validação: Preenchimento obrigatório se
                    ({dtAdm}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm)
                    ou
                    {dtExercicio}(2200_vinculo_infoRegimeTrab_infoEstatutario_dtExercicio))
                    &gt;= [2021-07-19].
                :ivar condIng:
                """
                tmpResid: Optional[TsTmpResid] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                condIng: Optional[TsCondIng] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

            @dataclass
            class InfoDeficiencia:
                """
                :ivar defFisica:
                :ivar defVisual:
                :ivar defAuditiva:
                :ivar defMental:
                :ivar defIntelectual:
                :ivar reabReadap:
                :ivar infoCota: Informar se o trabalhador deve ser
                    contabilizado no preenchimento de cota de pessoas
                    com deficiência habilitadas ou de beneficiários
                    reabilitados. Validação: Preenchimento obrigatório e
                    exclusivo se {tpRegTrab}(2200_vinculo_tpRegTrab) =
                    [1]. Somente pode ser informado [S] se pelo menos um
                    dos campos a seguir estiver preenchido com [S]:
                    {defFisica}(./defFisica), {defVisual}(./defVisual),
                    {defAuditiva}(./defAuditiva),
                    {defMental}(./defMental),
                    {defIntelectual}(./defIntelectual) e
                    {reabReadap}(./reabReadap). Esta validação não deve
                    ser realizada quando se tratar de evento enviado em
                    versão do leiaute anterior a S-1.0.
                :ivar observacao:
                """
                defFisica: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                defVisual: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                defAuditiva: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                defMental: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                defIntelectual: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                reabReadap: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                infoCota: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                observacao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 255,
                        "pattern": r"[^\s]{1}[\S\s]*",
                    }
                )

            @dataclass
            class Dependente:
                """
                :ivar tpDep:
                :ivar nmDep:
                :ivar dtNascto:
                :ivar cpfDep:
                :ivar sexoDep: Sexo do dependente. Validação:
                    Preenchimento obrigatório se
                    {tpRegPrev}(2200_vinculo_tpRegPrev) = [2] e
                    {cadIni}(2200_vinculo_cadIni) = [N]. Não informar se
                    {tpRegPrev}(2200_vinculo_tpRegPrev) for diferente de
                    [2].
                :ivar depIRRF:
                :ivar depSF:
                :ivar incTrab:
                """
                tpDep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{2}",
                    }
                )
                nmDep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 2,
                        "max_length": 70,
                        "pattern": r".*[^\s].*",
                    }
                )
                dtNascto: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": XmlDate(1890, 1, 1),
                    }
                )
                cpfDep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{11}",
                    }
                )
                sexoDep: Optional[TsSexo] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                depIRRF: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                depSF: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                incTrab: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class Vinculo:
            """
            :ivar matricula: Matrícula atribuída ao trabalhador pela
                empresa ou, no caso de servidor público, a matrícula
                constante no Sistema de Administração de Recursos
                Humanos do órgão. Validação: O valor informado não pode
                conter a expressão 'eSocial' nas 7 (sete) primeiras
                posições. REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar tpRegTrab: Tipo de regime trabalhista. Validação: Se
                {codCateg}(2200_vinculo_infoContrato_codCateg) = [104],
                deve ser preenchido com [1].
            :ivar tpRegPrev:
            :ivar cadIni:
            :ivar infoRegimeTrab: Informações do regime trabalhista.
            :ivar infoContrato: Informações do contrato de trabalho.
            :ivar sucessaoVinc: Grupo de informações da sucessão de
                vínculo trabalhista/estatutário. CONDICAO_GRUPO: O (se
                {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                = [2, 3, 4, 7] ou
                {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                = [5, 8]); N (nos demais casos)
            :ivar transfDom: Informações do empregado doméstico
                transferido de outro representante da mesma unidade
                familiar. CONDICAO_GRUPO: O (se
                {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                for igual [5]); N (nos demais casos)
            :ivar mudancaCPF: Informações de mudança de CPF do
                trabalhador. CONDICAO_GRUPO: O (se
                {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                = [6] ou
                {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                = [10]); N (nos demais casos)
            :ivar afastamento: Informações de afastamento do trabalhador
                DESCRICAO_COMPLETA:Informações de afastamento do
                trabalhador. Preenchimento exclusivo em caso de
                trabalhador que permaneça afastado na data de início da
                obrigatoriedade dos eventos não periódicos para o
                empregador no eSocial ou na data de transferência ou
                alteração de CPF do empregado. CONDICAO_GRUPO: N (se
                grupo {desligamento}(2200_vinculo_desligamento) estiver
                preenchido); OC (nos demais casos)
            :ivar desligamento: Informação do desligamento do
                trabalhador DESCRICAO_COMPLETA:Informação do
                desligamento do trabalhador. Grupo preenchido
                exclusivamente caso seja necessário enviar cadastramento
                inicial referente a trabalhador que já tenha sido
                desligado da empresa antes do início dos eventos não
                periódicos para o empregador no eSocial (por exemplo,
                envio para pagamento de diferenças salariais -
                acordo/dissídio/convenção coletiva - em meses
                posteriores ao desligamento e sob vigência dos eventos
                periódicos para o empregador no eSocial) ou no caso de
                desligamento em data anterior à transferência do
                empregado. CONDICAO_GRUPO: N (se (grupo
                {afastamento}(2200_vinculo_afastamento) ou
                {cessao}(2200_vinculo_cessao) estiver preenchido) ou (se
                {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                = [6] ou
                {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                = [10])); OC (nos demais casos)
            :ivar cessao: Informação de cessão/exercício em outro órgão
                do trabalhador DESCRICAO_COMPLETA:Informação de
                cessão/exercício em outro órgão do trabalhador.
                Preenchimento exclusivo em caso de trabalhador que
                permaneça cedido/em exercício em outro órgão na data de
                início da obrigatoriedade dos eventos não periódicos
                para o empregador/ente público no eSocial ou na data de
                transferência ou alteração de CPF do empregado.
                CONDICAO_GRUPO: N (se grupo
                {desligamento}(2200_vinculo_desligamento) estiver
                preenchido); OC (nos demais casos)
            """
            matricula: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 30,
                    "pattern": r".*[^\s].*",
                }
            )
            tpRegTrab: Optional[TsTpRegTrab] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            tpRegPrev: Optional[TsTpRegPrev] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            cadIni: Optional[VinculoCadIni] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            infoRegimeTrab: Optional["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            infoContrato: Optional["ESocial.EvtAdmissao.Vinculo.InfoContrato"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            sucessaoVinc: Optional["ESocial.EvtAdmissao.Vinculo.SucessaoVinc"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            transfDom: Optional["ESocial.EvtAdmissao.Vinculo.TransfDom"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            mudancaCPF: Optional["ESocial.EvtAdmissao.Vinculo.MudancaCpf"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            afastamento: Optional["ESocial.EvtAdmissao.Vinculo.Afastamento"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            desligamento: Optional["ESocial.EvtAdmissao.Vinculo.Desligamento"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            cessao: Optional["ESocial.EvtAdmissao.Vinculo.Cessao"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )

            @dataclass
            class InfoRegimeTrab:
                """
                :ivar infoCeletista: Informações de trabalhador
                    celetista. CONDICAO_GRUPO: O (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [1]); N (nos
                    demais casos)
                :ivar infoEstatutario: Informações de trabalhador
                    estatutário. CONDICAO_GRUPO: O (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [2]); N (nos
                    demais casos)
                """
                infoCeletista: Optional["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                infoEstatutario: Optional["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoEstatutario"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass
                class InfoCeletista:
                    """
                    :ivar dtAdm: Preencher com a data de admissão do
                        trabalhador. No caso de transferência do
                        empregado ou de mudança de CPF, preencher com a
                        data inicial do vínculo no primeiro empregador
                        (data de início do vínculo). Validação: Devem
                        ser observadas as seguintes regras: a) Deve ser
                        posterior à data de nascimento do trabalhador;
                        b) Se {cadIni}(2200_vinculo_cadIni) = [S], deve
                        ser anterior à data de início da obrigatoriedade
                        dos eventos não periódicos para o empregador no
                        eSocial; c) Se {cadIni}(2200_vinculo_cadIni) =
                        [N] e
                        {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                        = [1], deve ser igual ou posterior à data de
                        início da obrigatoriedade dos eventos não
                        periódicos para o empregador no eSocial.
                    :ivar tpAdmissao:
                    :ivar indAdmissao:
                    :ivar nrProcTrab: Número que identifica o processo
                        trabalhista, quando a admissão se der por
                        decisão judicial. Validação: Informação
                        obrigatória e exclusiva se
                        {indAdmissao}(./indAdmissao) = [3]. Se
                        preenchido, deve ser um processo judicial
                        válido, com 20 (vinte) algarismos.
                    :ivar tpRegJor:
                    :ivar natAtividade:
                    :ivar dtBase:
                    :ivar cnpjSindCategProf:
                    :ivar FGTS: Informações do FGTS
                        DESCRICAO_COMPLETA:Informações do Fundo de
                        Garantia do Tempo de Serviço - FGTS.
                        CONDICAO_GRUPO: N (se
                        {tpAdmissao}(../tpAdmissao) = [6] OU (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg)
                        for diferente de [104] e {dtAdm}(../dtAdm) &gt;=
                        [1988-10-05]) OU (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) =
                        [104] e {dtAdm}(../dtAdm) &gt;= [2015-10-01]));
                        O (nos demais casos)
                    :ivar trabTemporario: Dados sobre trabalho
                        temporário DESCRICAO_COMPLETA:Dados sobre
                        trabalho temporário. Preenchimento obrigatório
                        no caso de contratação de trabalhador
                        temporário. CONDICAO_GRUPO: N (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg)
                        for diferente de [106]); O (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) =
                        [106] e se grupo
                        {desligamento}(2200_vinculo_desligamento) não
                        estiver preenchido); F (nos demais casos)
                    :ivar aprend: Informações relacionadas ao aprendiz
                        DESCRICAO_COMPLETA:Informações para
                        identificação do empregador contratante de
                        aprendiz. Preenchimento obrigatório no caso de
                        contratação de aprendiz por entidade educativa
                        sem fins lucrativos que tenha por objetivo a
                        assistência ao adolescente e à educação
                        profissional (art. 430, inciso II, CLT) ou por
                        entidade de prática desportiva filiada ao
                        Sistema Nacional do Desporto ou a Sistema de
                        Desporto de Estado, do Distrito Federal ou de
                        Município (art. 430, inciso III, CLT).
                        CONDICAO_GRUPO: N (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg)
                        for diferente de [103]); OC (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) =
                        [103] e se grupo
                        {desligamento}(2200_vinculo_desligamento) não
                        estiver preenchido); F (nos demais casos)
                    """
                    dtAdm: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    tpAdmissao: Optional[InfoCeletistaTpAdmissao] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    indAdmissao: Optional[InfoCeletistaIndAdmissao] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    nrProcTrab: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "length": 20,
                        }
                    )
                    tpRegJor: Optional[TsTpRegJor] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    natAtividade: Optional[TsNatAtividade] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    dtBase: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": "1",
                            "max_inclusive": "12",
                            "pattern": r"\d{1,2}",
                        }
                    )
                    cnpjSindCategProf: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{14}",
                        }
                    )
                    FGTS: Optional["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.Fgts"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    trabTemporario: Optional["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    aprend: Optional[TAprend] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class Fgts:
                        dtOpcFGTS: Optional[XmlDate] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )

                    @dataclass
                    class TrabTemporario:
                        """
                        :ivar hipLeg:
                        :ivar justContr: Descrição do fato determinado
                            que, no caso concreto, justifica a hipótese
                            legal para a contratação de trabalho
                            temporário. O prazo de contratação do
                            trabalho temporário deve ser compatível com
                            o motivo justificador alegado.
                        :ivar ideEstabVinc: Identificação do
                            estabelecimento do tomador ao qual o
                            trabalhador temporário está vinculado
                        :ivar ideTrabSubstituido: Identificação do(s)
                            trabalhador(es) substituído(s). CHAVE_GRUPO:
                            {cpfTrabSubst} CONDICAO_GRUPO: O (se
                            {hipLeg}(2200_vinculo_infoRegimeTrab_infoCeletista_trabTemporario_hipLeg)
                            = [1]); N (nos demais casos)
                        """
                        hipLeg: Optional[TrabTemporarioHipLeg] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        justContr: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 999,
                                "pattern": r"[^\s]{1}[\S\s]*",
                            }
                        )
                        ideEstabVinc: Optional["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario.IdeEstabVinc"] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        ideTrabSubstituido: List["ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario.IdeTrabSubstituido"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 9,
                            }
                        )

                        @dataclass
                        class IdeEstabVinc:
                            """
                            :ivar tpInsc:
                            :ivar nrInsc: Informar o número de inscrição
                                do contratante de serviços, de acordo
                                com o tipo de inscrição informado em
                                {ideEstabVinc/tpInsc}(./tpInsc).
                                Validação: Se
                                {ideEstabVinc/tpInsc}(./tpInsc) for
                                igual a [1], deve ser um CNPJ válido,
                                com 14 (catorze) algarismos. Se
                                {ideEstabVinc/tpInsc}(./tpInsc) for
                                igual a [2], deve ser um CPF válido.
                            """
                            tpInsc: Optional[TsTpInsc12] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            nrInsc: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "pattern": r"\d{11}|\d{14}",
                                }
                            )

                        @dataclass
                        class IdeTrabSubstituido:
                            """
                            :ivar cpfTrabSubst: CPF do trabalhador
                                substituído. Validação: Deve ser um CPF
                                válido.
                            """
                            cpfTrabSubst: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "pattern": r"\d{11}",
                                }
                            )

                @dataclass
                class InfoEstatutario:
                    """
                    :ivar tpProv:
                    :ivar dtExercicio: Data da entrada em exercício pelo
                        servidor. Validação: Devem ser observadas as
                        seguintes regras: a) Deve ser posterior à data
                        de nascimento do trabalhador; b) Se
                        {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                        anterior à data de início da obrigatoriedade dos
                        eventos não periódicos para o empregador/ente
                        público no eSocial; c) Se
                        {cadIni}(2200_vinculo_cadIni) = [N] e
                        {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                        for diferente de [5, 8, 10], deve ser igual ou
                        posterior à data de início da obrigatoriedade
                        dos eventos não periódicos para o
                        empregador/ente público no eSocial.
                    :ivar tpPlanRP: Tipo de plano de segregação da
                        massa. Validação: Preenchimento obrigatório e
                        exclusivo se {tpRegPrev}(2200_vinculo_tpRegPrev)
                        = [2].
                    :ivar indTetoRGPS: Informar se o servidor está
                        sujeito ao teto do RGPS pela instituição do
                        regime de previdência complementar. Validação:
                        Preenchimento obrigatório e exclusivo se
                        {tpRegPrev}(2200_vinculo_tpRegPrev) = [2].
                    :ivar indAbonoPerm: Indicar se o servidor recebe
                        abono permanência. Validação: Preenchimento
                        obrigatório e exclusivo se
                        {tpRegPrev}(2200_vinculo_tpRegPrev) = [2].
                    :ivar dtIniAbono: Informar a data de inicio do abono
                        permanência. Validação: Preenchimento
                        obrigatório se {indAbonoPerm}(./indAbonoPerm) =
                        [S] e {cadIni}(2200_vinculo_cadIni) = [N]. Não
                        informar se {indAbonoPerm}(./indAbonoPerm) =
                        [N]. Se preenchida, devem ser observadas as
                        seguintes regras: a) Deve ser igual ou posterior
                        à data de exercício do servidor; b) Se
                        {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                        anterior à data de início da obrigatoriedade dos
                        eventos não periódicos para o ente público; c)
                        Se {cadIni}(2200_vinculo_cadIni) = [N], deve ser
                        igual ou anterior à data da transferência ou
                        alteração do CPF do servidor
                        ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf)
                        ou
                        {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)).
                        Não informar se
                        {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                        for diferente de [5, 8, 10].
                    """
                    tpProv: Optional[InfoEstatutarioTpProv] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    dtExercicio: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    tpPlanRP: Optional[TsTpPlanRp] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    indTetoRGPS: Optional[TsSimNao] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    indAbonoPerm: Optional[TsSimNao] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtIniAbono: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

            @dataclass
            class InfoContrato:
                """
                :ivar nmCargo: Informar o nome do cargo. Validação: O
                    preenchimento é obrigatório, exceto se for relativo
                    a servidor nomeado em cargo em comissão
                    ({tpRegTrab}(2200_vinculo_tpRegTrab) = [2] e
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                    = [2]).
                :ivar CBOCargo:
                :ivar dtIngrCargo: Data de ingresso do servidor no
                    cargo. Validação: Não preencher se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [1] ou se
                    {CBOCargo}(./CBOCargo) não for informado. Se
                    preenchida, devem ser observadas as seguintes
                    regras: a) Deve ser igual ou posterior à data de
                    exercício do servidor; b) Se
                    {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                    anterior à data de início da obrigatoriedade dos
                    eventos não periódicos para o ente público; c) Se
                    {cadIni}(2200_vinculo_cadIni) = [N], deve ser igual
                    ou anterior à data da transferência ou alteração do
                    CPF do servidor
                    ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf)
                    ou {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)).
                    Não informar se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                    for diferente de [5, 8, 10].
                :ivar nmFuncao: Informar o nome da função de
                    confiança/cargo em comissão. Validação:
                    Preenchimento obrigatório se for relativo a servidor
                    nomeado em cargo em comissão
                    ({tpRegTrab}(2200_vinculo_tpRegTrab) = [2] e
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                    = [2]).
                :ivar CBOFuncao:
                :ivar acumCargo: Informar se o cargo, emprego ou função
                    pública é acumulável. Validação: Preenchimento
                    obrigatório se {cadIni}(2200_vinculo_cadIni) = [N] e
                    se a natureza jurídica do declarante for igual a
                    1XX-X, 201-1 ou 203-8.
                :ivar codCateg:
                :ivar remuneracao: Informações da remuneração e
                    periodicidade de pagamento. CONDICAO_GRUPO: N (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [2]); O (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [1] e se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                :ivar duracao: Duração do contrato de trabalho.
                    CONDICAO_GRUPO: N (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [2]); O (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [1] e se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                :ivar localTrabalho: Informações do local de trabalho.
                    CONDICAO_GRUPO: O (se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                :ivar horContratual: Informações do horário contratual
                    do trabalhador. CONDICAO_GRUPO: O (se
                    {tpRegJor}(2200_vinculo_infoRegimeTrab_infoCeletista_tpRegJor)
                    = [1] e se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); OC (se
                    {tpRegJor}(2200_vinculo_infoRegimeTrab_infoCeletista_tpRegJor)
                    for diferente de [1] e se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                :ivar alvaraJudicial: Dados do alvará judicial
                    DESCRICAO_COMPLETA:Informações do alvará judicial em
                    caso de contratação de menores de 14 anos, em
                    qualquer categoria, e de maiores de 14 e menores de
                    16, em categoria diferente de "Aprendiz".
                    CONDICAO_GRUPO: OC (se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                :ivar observacoes: Observações do contrato de trabalho.
                    CONDICAO_GRUPO: OC (se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                :ivar treiCap: Treinamentos, capacitações, exercícios
                    simulados e outras anotações
                    DESCRICAO_COMPLETA:Treinamentos, capacitações,
                    exercícios simulados, autorizações ou outras
                    anotações que devam ser anotadas no registro de
                    empregados e/ou na CTPS, por determinação de Norma
                    Regulamentadora - NR. CHAVE_GRUPO: {codTreiCap}
                    CONDICAO_GRUPO: OC (se grupo
                    {desligamento}(2200_vinculo_desligamento) não
                    estiver preenchido); F (nos demais casos)
                """
                nmCargo: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 100,
                        "pattern": r"[^\s]{1}[\S\s]*",
                    }
                )
                CBOCargo: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{6}",
                    }
                )
                dtIngrCargo: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                nmFuncao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 100,
                        "pattern": r"[^\s]{1}[\S\s]*",
                    }
                )
                CBOFuncao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{6}",
                    }
                )
                acumCargo: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                codCateg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{3}",
                    }
                )
                remuneracao: Optional[TRemuneracao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                duracao: Optional["ESocial.EvtAdmissao.Vinculo.InfoContrato.Duracao"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                localTrabalho: Optional["ESocial.EvtAdmissao.Vinculo.InfoContrato.LocalTrabalho"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                horContratual: Optional[THorContratual] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                alvaraJudicial: Optional[TAlvaraJudicial] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                observacoes: List["ESocial.EvtAdmissao.Vinculo.InfoContrato.Observacoes"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )
                treiCap: List[TTreiCap] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )

                @dataclass
                class Duracao:
                    """
                    :ivar tpContr:
                    :ivar dtTerm:
                    :ivar clauAssec: Indicar se o contrato por prazo
                        determinado contém cláusula assecuratória do
                        direito recíproco de rescisão antes da data de
                        seu término. Validação: O preenchimento é
                        obrigatório se {tpContr}(./tpContr) = [2, 3].
                        Não preencher se {tpContr}(./tpContr) = [1].
                    :ivar objDet:
                    """
                    tpContr: Optional[TsTpContr] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    dtTerm: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    clauAssec: Optional[TsSimNao] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    objDet: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 255,
                            "pattern": r"[^\s]{1}[\S\s]*",
                        }
                    )

                @dataclass
                class LocalTrabalho:
                    """
                    :ivar localTrabGeral: Estabelecimento onde o
                        trabalhador exercerá suas atividades
                        DESCRICAO_COMPLETA:Estabelecimento (CNPJ, CNO,
                        CAEPF) onde o trabalhador (exceto doméstico)
                        exercerá suas atividades. Caso o trabalhador
                        exerça suas atividades em instalações de
                        terceiros, este campo deve ser preenchido com o
                        estabelecimento do próprio empregador ao qual o
                        trabalhador esteja vinculado. CONDICAO_GRUPO: N
                        (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) =
                        [104]); O (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg)
                        for diferente de [104] e se grupo
                        {desligamento}(2200_vinculo_desligamento) não
                        estiver preenchido); F (nos demais casos)
                    :ivar localTempDom: Endereço de trabalho do
                        trabalhador doméstico e trabalhador temporário
                        DESCRICAO_COMPLETA:Grupo preenchido
                        exclusivamente em caso de trabalhador doméstico
                        e trabalhador temporário, indicando o endereço
                        onde o trabalhador exerce suas atividades.
                        CONDICAO_GRUPO: N (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg)
                        for diferente de [104, 106]); O (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) =
                        [104, 106] e se grupo
                        {desligamento}(2200_vinculo_desligamento) não
                        estiver preenchido); F (nos demais casos)
                    """
                    localTrabGeral: Optional[TLocalTrabGeral] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    localTempDom: Optional[TEnderecoBrasil] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass
                class Observacoes:
                    """
                    :ivar observacao: Observação relacionada ao contrato
                        de trabalho.
                    """
                    observacao: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 255,
                            "pattern": r"[^\s]{1}[\S\s]*",
                        }
                    )

            @dataclass
            class SucessaoVinc:
                """
                :ivar tpInsc:
                :ivar nrInsc:
                :ivar matricAnt: Matrícula do trabalhador no empregador
                    anterior. Validação: O preenchimento é obrigatório
                    se {cadIni}(2200_vinculo_cadIni) = [N].
                :ivar dtTransf: Preencher com a data da transferência do
                    empregado para o empregador declarante. Validação:
                    Devem ser observadas as seguintes regras: a) Deve
                    ser posterior à data de admissão do trabalhador; b)
                    Se {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                    anterior à data de início da obrigatoriedade dos
                    eventos não periódicos para o empregador; c) Se
                    {cadIni}(2200_vinculo_cadIni) = [N], deve ser igual
                    ou posterior à data de início da obrigatoriedade dos
                    eventos não periódicos para o empregador.
                :ivar observacao:
                """
                tpInsc: Optional[SucessaoVincTpInsc] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                nrInsc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{8,14}",
                    }
                )
                matricAnt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )
                dtTransf: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                observacao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 255,
                        "pattern": r"[^\s]{1}[\S\s]*",
                    }
                )

            @dataclass
            class TransfDom:
                """
                :ivar cpfSubstituido: Preencher com o número do CPF do
                    representante anterior da unidade familiar.
                    Validação: Deve ser um CPF válido e diferente do CPF
                    do declarante e do empregado.
                :ivar matricAnt: Matrícula do trabalhador no
                    representante anterior da unidade familiar.
                :ivar dtTransf: Data da transferência do vínculo ao novo
                    representante da unidade familiar.
                """
                cpfSubstituido: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{11}",
                    }
                )
                matricAnt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )
                dtTransf: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

            @dataclass
            class MudancaCpf:
                """
                :ivar cpfAnt: Preencher com o número do CPF antigo do
                    trabalhador.
                :ivar matricAnt: Preencher com a matrícula anterior do
                    trabalhador.
                :ivar dtAltCPF: Data de alteração do CPF.
                :ivar observacao:
                """
                cpfAnt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{11}",
                    }
                )
                matricAnt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )
                dtAltCPF: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                observacao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 255,
                        "pattern": r"[^\s]{1}[\S\s]*",
                    }
                )

            @dataclass
            class Afastamento:
                """
                :ivar dtIniAfast: Data de início do afastamento.
                    Validação: Devem ser observadas as seguintes regras:
                    a) Deve ser igual ou posterior à data de
                    admissão/exercício do trabalhador; b) Se
                    {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                    anterior à data de início da obrigatoriedade dos
                    eventos não periódicos para o empregador; c) Se
                    {cadIni}(2200_vinculo_cadIni) = [N], deve ser
                    anterior à data da transferência ou alteração do CPF
                    do empregado
                    ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf),
                    {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf)
                    ou {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)).
                    Não informar se
                    {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                    = [1] ou se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                    for diferente de [5, 8, 10].
                :ivar codMotAfast:
                """
                dtIniAfast: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                codMotAfast: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{2}",
                    }
                )

            @dataclass
            class Desligamento:
                """
                :ivar dtDeslig: Preencher com a data de desligamento do
                    vínculo (último dia trabalhado). Validação: Devem
                    ser observadas as seguintes regras: a) Deve ser
                    igual ou posterior à data de admissão/exercício do
                    trabalhador; b) Se {cadIni}(2200_vinculo_cadIni) =
                    [S], deve ser anterior à data de início da
                    obrigatoriedade dos eventos não periódicos para o
                    empregador; c) Se {cadIni}(2200_vinculo_cadIni) =
                    [N], deve ser anterior à data da transferência do
                    empregado
                    ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf)
                    ou
                    {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf)).
                    Não informar se
                    {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                    = [1] ou se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                    for diferente de [5, 8].
                """
                dtDeslig: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

            @dataclass
            class Cessao:
                """
                :ivar dtIniCessao: Data de início da cessão/exercício em
                    outro órgão. Validação: Devem ser observadas as
                    seguintes regras: a) Deve ser igual ou posterior à
                    data de admissão/exercício do trabalhador; b) Se
                    {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                    anterior à data de início da obrigatoriedade dos
                    eventos não periódicos para o ente público e a
                    natureza jurídica do declarante deve ser
                    Administração Pública (grupo [1]); c) Se
                    {cadIni}(2200_vinculo_cadIni) = [N], deve ser
                    anterior à data da transferência ou alteração do CPF
                    do empregado
                    ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf)
                    ou {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)) e
                    igual ou posterior a [2021-07-19]. Não informar se
                    {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao)
                    = [1] ou se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv)
                    for diferente de [5, 8, 10].
                """
                dtIniCessao: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
