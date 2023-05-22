from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from esociallib.esocial.bindings.v1_1.org.w3.pkg_2000.pkg_09.xmldsig import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00"


class TsInd13(Enum):
    """Indicativo de 13° salário.

    Validação: Se {indApuracao}(/ideEvento_perApur) = [2], preencher com [1].

    :cvar VALUE_0: Mensal
    :cvar VALUE_1: 13° salário
        ({codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em
        S-1010 = [12, 14, 16, 22, 26, 32, 92, 94, 96, 98])
    """
    VALUE_0 = 0
    VALUE_1 = 1


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


class TsTpAcConv(Enum):
    """
    Tipo do instrumento ou situação ensejadora da remuneração relativa a períodos
    de apuração anteriores.

    :cvar A: Acordo Coletivo de Trabalho
    :cvar B: Legislação federal, estadual, municipal ou distrital
    :cvar C: Convenção Coletiva de Trabalho
    :cvar D: Sentença normativa - Dissídio
    :cvar E: Conversão de licença saúde em acidente de trabalho
    :cvar F: Outras verbas de natureza salarial ou não salarial devidas
        após o desligamento
    :cvar G: Antecipação de diferenças de acordo, convenção ou dissídio
        coletivo
    :cvar H: Recolhimento mensal de FGTS anterior ao início de
        obrigatoriedade dos eventos periódicos
    :cvar I: Sentença judicial (exceto reclamatória trabalhista)
    """
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"


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


class TsTpInsc1234(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    :cvar VALUE_2: CPF
    :cvar VALUE_3: CAEPF
    :cvar VALUE_4: CNO
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


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


class TsTpProc12(Enum):
    """
    Preencher com o código correspondente ao tipo de processo.

    :cvar VALUE_1: Administrativo
    :cvar VALUE_2: Judicial
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        }
    )
    emailPrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    nmCid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    paisNascto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    paisNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{4}",
        }
    )


class CalcTercTpCr(Enum):
    """Código de Receita - CR da contribuição descontada do trabalhador.

    :cvar VALUE_121802: Contribuição ao SEST, descontada do
        transportador autônomo
    :cvar VALUE_122102: Contribuição ao SENAT, descontada do
        transportador autônomo
    """
    VALUE_121802 = 121802
    VALUE_122102 = 122102


class DetInfoPerRefTpVrPerRef(Enum):
    """
    Tipo de valor que influi na apuração da contribuição devida.

    :cvar VALUE_11: Base de cálculo da contribuição previdenciária
        normal
    :cvar VALUE_12: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 15 anos de contribuição
    :cvar VALUE_13: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 20 anos de contribuição
    :cvar VALUE_14: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 25 anos de contribuição
    :cvar VALUE_15: Base de cálculo da contribuição previdenciária
        adicional normal - Exclusiva do empregador
    :cvar VALUE_16: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 15 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_17: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 20 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_18: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 25 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_19: Base de cálculo da contribuição previdenciária
        exclusiva do empregado
    :cvar VALUE_21: Valor total descontado do trabalhador para
        recolhimento à Previdência Social
    :cvar VALUE_22: Valor descontado do trabalhador para recolhimento ao
        SEST
    :cvar VALUE_23: Valor descontado do trabalhador para recolhimento ao
        SENAT
    :cvar VALUE_31: Valor pago ao trabalhador a título de salário-
        família
    :cvar VALUE_32: Valor pago ao trabalhador a título de salário-
        maternidade
    """
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_31 = 31
    VALUE_32 = 32


class InfoBaseCsTpValor(Enum):
    """
    Tipo de valor que influi na apuração da contribuição devida.

    :cvar VALUE_11: Base de cálculo da contribuição previdenciária
        normal
    :cvar VALUE_12: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 15 anos de contribuição
    :cvar VALUE_13: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 20 anos de contribuição
    :cvar VALUE_14: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 25 anos de contribuição
    :cvar VALUE_15: Base de cálculo da contribuição previdenciária
        adicional normal - Exclusiva do empregador
    :cvar VALUE_16: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 15 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_17: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 20 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_18: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 25 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_19: Base de cálculo da contribuição previdenciária
        exclusiva do empregado
    :cvar VALUE_21: Valor total descontado do trabalhador para
        recolhimento à Previdência Social
    :cvar VALUE_22: Valor descontado do trabalhador para recolhimento ao
        SEST
    :cvar VALUE_23: Valor descontado do trabalhador para recolhimento ao
        SENAT
    :cvar VALUE_31: Valor pago ao trabalhador a título de salário-
        família
    :cvar VALUE_32: Valor pago ao trabalhador a título de salário-
        maternidade
    :cvar VALUE_41: Base de cálculo da contribuição previdenciária
        normal - Categorias 107 e 108
    :cvar VALUE_42: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 15 anos de contribuição - Categorias 107 e 108
    :cvar VALUE_43: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 20 anos de contribuição - Categorias 107 e 108
    :cvar VALUE_44: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 25 anos de contribuição - Categorias 107 e 108
    :cvar VALUE_45: Base de cálculo da contribuição previdenciária
        adicional normal - Exclusiva do empregador - Categorias 107 e
        108
    :cvar VALUE_46: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 15 anos de contribuição - Exclusiva do empregador
        - Categorias 107 e 108
    :cvar VALUE_47: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 20 anos de contribuição - Exclusiva do empregador
        - Categorias 107 e 108
    :cvar VALUE_48: Base de cálculo da contribuição previdenciária
        adicional para o financiamento dos benefícios de aposentadoria
        especial após 25 anos de contribuição - Exclusiva do empregador
        - Categorias 107 e 108
    :cvar VALUE_49: Base de cálculo da contribuição previdenciária
        exclusiva do empregado - Categorias 107 e 108
    :cvar VALUE_81: Incidência suspensa em decorrência de decisão
        judicial - Base de cálculo - BC da Contribuição Previdenciária -
        CP normal - Categorias 107 e 108
    :cvar VALUE_82: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 15 anos de trabalho
        - Categorias 107 e 108
    :cvar VALUE_83: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 20 anos de trabalho
        - Categorias 107 e 108
    :cvar VALUE_84: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 25 anos de trabalho
        - Categorias 107 e 108
    :cvar VALUE_85: Incidência suspensa em decorrência de decisão
        judicial - BC CP normal - Exclusiva do empregador - Categorias
        107 e 108
    :cvar VALUE_86: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 15 anos de trabalho
        - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_87: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 20 anos de trabalho
        - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_88: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 25 anos de trabalho
        - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_91: Incidência suspensa em decorrência de decisão
        judicial - BC CP normal
    :cvar VALUE_92: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 15 anos de trabalho
    :cvar VALUE_93: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 20 anos de trabalho
    :cvar VALUE_94: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 25 anos de trabalho
    :cvar VALUE_95: Incidência suspensa em decorrência de decisão
        judicial - BC CP normal - Exclusiva do empregador
    :cvar VALUE_96: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 15 anos de trabalho
        - Exclusiva do empregador
    :cvar VALUE_97: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 20 anos de trabalho
        - Exclusiva do empregador
    :cvar VALUE_98: Incidência suspensa em decorrência de decisão
        judicial - BC CP aposentadoria especial aos 25 anos de trabalho
        - Exclusiva do empregador
    """
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_81 = 81
    VALUE_82 = 82
    VALUE_83 = 83
    VALUE_84 = 84
    VALUE_85 = 85
    VALUE_86 = 86
    VALUE_87 = 87
    VALUE_88 = 88
    VALUE_91 = 91
    VALUE_92 = 92
    VALUE_93 = 93
    VALUE_94 = 94
    VALUE_95 = 95
    VALUE_96 = 96
    VALUE_97 = 97
    VALUE_98 = 98


class InfoCpCalcTpCr(Enum):
    """Código de Receita - CR da contribuição descontada do trabalhador.
    Validação: Se {indApuracao}(5001_ideEvento_indApuracao) = [2], deve ser igual a [108221, 108222, 108223, 108224, 108225, 109921, 109922].

    :cvar VALUE_108201: Contribuição Previdenciária - CP descontada do
        segurado empregado/avulso
    :cvar VALUE_108202: CP descontada do segurado empregado rural curto
        prazo - Lei 11.718/2008
    :cvar VALUE_108203: CP descontada do segurado empregado doméstico
    :cvar VALUE_108204: CP descontada do segurado especial curto prazo -
        Lei 11.718/2008
    :cvar VALUE_108205: CP descontada do segurado empregado do segurado
        especial
    :cvar VALUE_108207: CP descontada do segurado empregado do MEI
    :cvar VALUE_108221: CP descontada do segurado empregado/avulso 13°
        salário
    :cvar VALUE_108222: CP descontada do segurado empregado rural curto
        prazo 13° salário - Lei 11.718/2008
    :cvar VALUE_108223: CP descontada do segurado empregado doméstico
        13° salário
    :cvar VALUE_108224: CP descontada do segurado especial curto prazo
        13° salário - Lei 11.718/2008
    :cvar VALUE_108225: CP descontada do segurado empregado do segurado
        especial 13° salário
    :cvar VALUE_109901: CP descontada do contribuinte individual,
        alíquota de 11%
    :cvar VALUE_109902: CP descontada do contribuinte individual,
        alíquota de 20%
    :cvar VALUE_109921: CP descontada do contribuinte individual,
        alíquota de 11% - 13º salário
    :cvar VALUE_109922: CP descontada do contribuinte individual,
        alíquota de 20% - 13º salário
    """
    VALUE_108201 = 108201
    VALUE_108202 = 108202
    VALUE_108203 = 108203
    VALUE_108204 = 108204
    VALUE_108205 = 108205
    VALUE_108207 = 108207
    VALUE_108221 = 108221
    VALUE_108222 = 108222
    VALUE_108223 = 108223
    VALUE_108224 = 108224
    VALUE_108225 = 108225
    VALUE_109901 = 109901
    VALUE_109902 = 109902
    VALUE_109921 = 109921
    VALUE_109922 = 109922


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}",
        }
    )
    codMunic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{7}",
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    tmpParc: Optional[TsTmpParc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    horNoturno: Optional[TsSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    dscJorn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiTodos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nivEstagio: Optional[TInfoEstagiarioNivEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    areaAtuacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrApol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtPrevTerm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    instEnsino: Optional["TInfoEstagiario.InstEnsino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    ageIntegracao: Optional["TInfoEstagiario.AgeIntegracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    supervisorEstagio: Optional["TInfoEstagiario.SupervisorEstagio"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "pattern": r"\d{14}",
            }
        )
        nmRazao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        dscLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        nrLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            }
        )
        bairro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            }
        )
        cep: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "pattern": r"\d{8}",
            }
        )
        codMunic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "pattern": r"\d{7}",
            }
        )
        uf: Optional[TsUf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    remunOutrEmpr: List["TInfoMv.RemunOutrEmpr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        }
    )
    descRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
        }
    )
    ideAdv: List["TInfoRra.IdeAdv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )
    codSusp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    dscSalVar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtAdm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class ESocial:
    """S-5001 - Informações das Contribuições Sociais por Trabalhador

    :ivar evtBasesTrab: Evento Informações das Contribuições Sociais por
        Trabalhador. CHAVE_GRUPO: {Id}
    :ivar signature:
    """
    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_01_00"

    evtBasesTrab: Optional["ESocial.EvtBasesTrab"] = field(
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
    class EvtBasesTrab:
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do trabalhador. CHAVE_GRUPO:
            {cpfTrab*}
        :ivar infoCpCalc: Cálculo da contribuição previdenciária do
            segurado DESCRICAO_COMPLETA:Cálculo da contribuição
            previdenciária do segurado, incidente sobre a remuneração do
            período de apuração e de períodos anteriores informada nos
            eventos S-1200, S-2299 e S-2399. CHAVE_GRUPO: {tpCR}
            CONDICAO_GRUPO: OC
        :ivar infoCp: Informações sobre bases e valores das
            contribuições sociais DESCRICAO_COMPLETA:Informações sobre
            bases de cálculo, descontos e deduções de contribuições
            sociais devidas à Previdência Social e a Outras Entidades e
            Fundos, referentes à remuneração do período de apuração e de
            períodos anteriores informada nos eventos S-1200, S-2299 e
            S-2399. CONDICAO_GRUPO: OC
        :ivar Id:
        """
        ideEvento: Optional[TIdeEventoRetornoTrab] = field(
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
        ideTrabalhador: Optional["ESocial.EvtBasesTrab.IdeTrabalhador"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        infoCpCalc: List["ESocial.EvtBasesTrab.InfoCpCalc"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 9,
            }
        )
        infoCp: Optional["ESocial.EvtBasesTrab.InfoCp"] = field(
            default=None,
            metadata={
                "type": "Element",
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
        class IdeTrabalhador:
            """
            :ivar cpfTrab:
            :ivar infoCompl: Informações complementares do trabalhador e
                do contrato. CONDICAO_GRUPO: OC
            :ivar procJudTrab: Processos judiciais do trabalhador
                DESCRICAO_COMPLETA:Informações sobre processos judiciais
                do trabalhador com decisão favorável quanto à não
                incidência ou alterações na incidência de contribuição
                previdenciária. CHAVE_GRUPO: {nrProcJud} CONDICAO_GRUPO:
                OC
            """
            cpfTrab: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"\d{11}",
                }
            )
            infoCompl: Optional["ESocial.EvtBasesTrab.IdeTrabalhador.InfoCompl"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            procJudTrab: List["ESocial.EvtBasesTrab.IdeTrabalhador.ProcJudTrab"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                }
            )

            @dataclass
            class InfoCompl:
                """
                :ivar sucessaoVinc: Grupo de informações da sucessão de
                    vínculo trabalhista DESCRICAO_COMPLETA:Grupo de
                    informações da sucessão de vínculo trabalhista.
                    Evento de origem: S-1200. CONDICAO_GRUPO: OC
                :ivar infoInterm: Informações relativas ao trabalho
                    intermitente DESCRICAO_COMPLETA:Informações
                    relativas ao trabalho intermitente. Evento de
                    origem: S-1200 ou S-2299. CHAVE_GRUPO: {dia}
                    CONDICAO_GRUPO: OC
                :ivar infoComplCont: Informações complementares
                    contratuais do trabalhador
                    DESCRICAO_COMPLETA:Informações complementares
                    contratuais do trabalhador. Evento de origem:
                    S-1200. CHAVE_GRUPO: {codCBO}, {natAtividade},
                    {qtdDiasTrab} CONDICAO_GRUPO: OC
                """
                sucessaoVinc: Optional[TSucessaoVinc] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                infoInterm: List["ESocial.EvtBasesTrab.IdeTrabalhador.InfoCompl.InfoInterm"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 31,
                    }
                )
                infoComplCont: List["ESocial.EvtBasesTrab.IdeTrabalhador.InfoCompl.InfoComplCont"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass
                class InfoInterm:
                    """
                    :ivar dia: Dia do mês efetivamente trabalhado pelo
                        empregado com contrato de trabalho intermitente.
                    """
                    dia: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": "0",
                            "max_inclusive": "31",
                            "pattern": r"\d{1,2}",
                        }
                    )

                @dataclass
                class InfoComplCont:
                    """
                    :ivar codCBO: Classificação Brasileira de Ocupações
                        - CBO.
                    :ivar natAtividade: Natureza da atividade.
                    :ivar qtdDiasTrab: Informação prestada
                        exclusivamente pelo segurado especial em caso de
                        contratação de contribuinte individual,
                        indicando a quantidade de dias trabalhados pelo
                        mesmo.
                    """
                    codCBO: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{6}",
                        }
                    )
                    natAtividade: Optional[TsNatAtividade] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    qtdDiasTrab: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": "0",
                            "max_inclusive": "31",
                            "pattern": r"\d{1,2}",
                        }
                    )

            @dataclass
            class ProcJudTrab:
                """
                :ivar nrProcJud: Informar o número do processo judicial.
                    Origem: campo {nrProcJud} de S-1200, S-2299 ou
                    S-2399, se {tpTrib} no evento de origem for igual a
                    [2].
                :ivar codSusp: Código do indicativo da suspensão,
                    atribuído pelo empregador em S-1070. Origem: campo
                    {codSusp} de S-1200, S-2299 ou S-2399, se {tpTrib}
                    no evento de origem for igual a [2].
                """
                nrProcJud: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "length": 20,
                    }
                )
                codSusp: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{1,14}",
                    }
                )

        @dataclass
        class InfoCpCalc:
            """
            :ivar tpCR:
            :ivar vrCpSeg: Valor da contribuição do segurado, devida à
                Previdência Social, calculada segundo as regras da
                legislação em vigor, por CR. Validação: 1. Se {indMV} do
                S-1200/S-2299/S-2399 = [3], {vrCpSeg}(./vrCpSeg) = [0];
                portanto, não há CR. 2. Se {indMV} do
                S-1200/S-2299/S-2399 = [1, 2], efetuar o somatório das
                ocorrências do campo {vlrRemunOE} e o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19], resultando em [TotalRemun]. Este
                procedimento visa a identificação da(s) alíquota(s)
                aplicável(eis): 2.1. Se {indMV} do S-1200/S-2299/S-2399
                = [1], aplicar a(s) alíquota(s) conforme a categoria do
                segurado sobre a remuneração paga pelo declarante
                (somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19]), observado o limite máximo do
                salário de contribuição. 2.2. Se {indMV} do
                S-1200/S-2299/S-2399 = [2]: a) Se [TotalRemun]
                ultrapassar o limite máximo do salário de contribuição,
                aplicar a(s) alíquota(s) conforme a categoria do
                segurado sobre a diferença entre o referido limite
                máximo e o somatório das ocorrências do campo
                {vlrRemunOE}. Para os períodos de apuração iguais ou
                posteriores a 03/2020, observar a(s) faixa(s) de
                remuneração já tributada(s) em outra(s) empresa(s) nas
                categorias empregado/avulso/agente público. b) Se
                [TotalRemun] for inferior ao limite máximo do salário de
                contribuição: b1) Para as categorias
                empregado/avulso/agente público: somar {vlrRemunOE}
                destas mesmas categorias com o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19] e aplicar a(s) alíquota(s). Para
                os períodos de apuração iguais ou posteriores a 03/2020,
                observar a(s) faixa(s) de remuneração já tributada(s) em
                outra(s) empresa(s) nas categorias
                empregado/avulso/agente público. b2) Para categoria
                contribuinte individual: aplicar a alíquota sobre a
                remuneração paga pelo declarante (somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19]). 3. Se não for informado o grupo
                {infoMV} do S-1200/S-2299/S-2399: a) Se o trabalhador
                presta serviço para a empresa declarante em apenas uma
                categoria
                ({codCateg}(5001_infoCp_ideEstabLot_infoCategIncid_codCateg)),
                efetuar o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19] e aplicar a(s) alíquota(s)
                conforme a categoria. b) Se o trabalhador presta serviço
                para a empresa declarante em mais de uma categoria
                ({codCateg}(5001_infoCp_ideEstabLot_infoCategIncid_codCateg)):
                I. Efetuar o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19] para todas as categorias de
                segurado empregado/avulso/agente público e aplicar a(s)
                alíquota(s) correta(s) conforme faixa salarial,
                observado o limite máximo do salário de contribuição.
                II. Caso o somatório do item I não tenha atingido o
                limite máximo do salário de contribuição, efetuar o
                somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [11, 12, 13, 14, 19] para todas as categorias
                diferentes de segurado empregado e aplicar a alíquota
                correta conforme a categoria, observado o limite máximo
                do salário de contribuição. OBS.: a) No caso de
                {indApuracao}(5001_ideEvento_indApuracao) = [1], o
                cálculo deve ser efetuado separadamente para
                {infoBaseCS/ind13}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_ind13)
                = [0] e
                {infoBaseCS/ind13}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_ind13)
                = [1]. A soma de ambos os cálculos deve corresponder ao
                valor de {vrCpSeg}(./vrCpSeg). b) Aplica-se a alíquota
                de 20% para o cálculo da contribuição previdenciária a
                ser descontada de remuneração de trabalhador pertencente
                às categorias [731, 734], quando o empregador for
                cooperativa de trabalho
                ({indCoop}(1000_infoEmpregador_inclusao_infoCadastro_indCoop)
                em S-1000 = [1]), ou pertencente ao grupo "Contribuinte
                Individual", quando o Empregador tiver
                {classTrib}(5001_infoCp_classTrib) = [04, 70, 80]). Caso
                o trabalhador receba remuneração da empresa em outra
                categoria do grupo "Contribuinte Individual", primeiro
                deve ser aplicado o desconto sobre essa categoria (7XX)
                e depois sobre a remuneração das categorias [731, 734],
                observado o limite máximo do salário de contribuição. c)
                {vrCpSeg}(./vrCpSeg) deve ser igual a
                {vrDescSeg}(./vrDescSeg) nas seguintes situações: c1) Se
                houver informações em {infoPerAnt} na composição de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor);
                c2) Se houver informação de {procJudTrab} com {tpTrib} =
                [2] nos eventos que contenham informações de remuneração
                (S-1200, S-2299 e S-2399); c3) Se houver processo do
                empregador informado em S-1010, contestando incidência
                de contribuição previdenciária em rubricas utilizadas na
                composição da remuneração do trabalhador; c4) Se, no
                período de apuração mensal, houver remuneração referente
                a 13º salário
                ({codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                em S-1010 = [12, 14, 16, 22, 26, 32, 92, 94, 96, 98]).
                Nesse caso, o campo {vrCpSeg}(./vrCpSeg) será igual ao
                valor calculado sobre a remuneração mensal acrescido do
                desconto sobre a remuneração relativa a 13° salário
                informado pelo empregador; c5) Se {procEmi} do evento
                S-1200/S-2299/S-2399 for igual a [2, 4, 22]; c6) Para as
                categorias do grupo "Contribuinte Individual" (7XX), se
                o campo
                {dtTrans11096}(1000_infoEmpregador_inclusao_infoCadastro_dtTrans11096)
                em S-1000 for informado. d) No caso de trabalhador
                categoria = [102], utilizar somente a alíquota de 8%,
                observado o limite máximo do salário de contribuição. e)
                No caso de empregador com
                {classTrib}(5001_infoCp_classTrib) = [21, 22], exceto se
                {ideEstabLot/tpInsc}(5001_infoCp_ideEstabLot_tpInsc) =
                [4], ou com {classTrib}(5001_infoCp_classTrib) = [60],
                não calcular para a categoria do grupo "Contribuinte
                Individual" (7XX). O valor deve ser zerado. f) Não
                calcular quando a categoria do trabalhador for [741]
                (MEI). O valor deve ser zerado. g) Não calcular quando a
                lotação tributária for [91]. O valor deve ser zerado.
            :ivar vrDescSeg: Valor efetivamente descontado do segurado,
                correspondente a
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                = [21] do correspondente {infoCpCalc/tpCR}(./tpCR).
            """
            tpCR: Optional[InfoCpCalcTpCr] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            vrCpSeg: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": Decimal("0"),
                    "max_inclusive": Decimal("999999999999.99"),
                    "total_digits": 14,
                    "fraction_digits": 2,
                }
            )
            vrDescSeg: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": Decimal("0"),
                    "max_inclusive": Decimal("999999999999.99"),
                    "total_digits": 14,
                    "fraction_digits": 2,
                }
            )

        @dataclass
        class InfoCp:
            """
            :ivar classTrib:
            :ivar ideEstabLot: Identificação do estabelecimento ou obra
                e da lotação tributária DESCRICAO_COMPLETA:Identificação
                do estabelecimento ou obra de construção civil e da
                lotação tributária. CHAVE_GRUPO: {tpInsc}, {nrInsc},
                {codLotacao}
            """
            classTrib: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"\d{2}",
                }
            )
            ideEstabLot: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class IdeEstabLot:
                """
                :ivar tpInsc: Preencher com o código correspondente ao
                    tipo de inscrição, conforme Tabela 05. Evento de
                    origem: S-1200, S-2299 ou S-2399.
                :ivar nrInsc: Informar o número de inscrição do
                    contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstabLot/tpInsc}(./tpInsc).
                    Evento de origem: S-1200, S-2299 ou S-2399.
                :ivar codLotacao: Informar o código atribuído pelo
                    empregador para a lotação tributária. Evento de
                    origem: S-1200, S-2299 ou S-2399.
                :ivar infoCategIncid: Informações relativas à matrícula
                    e categoria do trabalhador e tipos de incidências.
                    CHAVE_GRUPO: {matricula}, {codCateg}, {indSimples}
                """
                tpInsc: Optional[TsTpInsc1234] = field(
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
                        "pattern": r"\d{11}|\d{12}|\d{14}",
                    }
                )
                codLotacao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )
                infoCategIncid: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 10,
                    }
                )

                @dataclass
                class InfoCategIncid:
                    """
                    :ivar matricula: Matrícula atribuída ao trabalhador
                        pela empresa ou, no caso de servidor público, a
                        matrícula constante no Sistema de Administração
                        de Recursos Humanos do órgão. Evento de origem:
                        S-1200, S-2299 ou S-2399.
                    :ivar codCateg: Preencher com o código da categoria
                        do trabalhador, conforme Tabela 01. Validação:
                        Se o evento de origem for S-1200, retornar o
                        código de categoria informado nesse evento. Se o
                        evento de origem for S-2299 ou S-2399, retornar
                        o código de categoria existente no Registro de
                        Eventos Trabalhistas - RET.
                    :ivar indSimples: Indicador de contribuição
                        substituída. Evento de origem: S-1200, S-2299 ou
                        S-2399.
                    :ivar infoBaseCS: Informações sobre bases de
                        cálculo, descontos e deduções de CS
                        DESCRICAO_COMPLETA:Informações sobre bases de
                        cálculo, descontos e deduções de contribuições
                        sociais devidas à Previdência Social e a Outras
                        Entidades e Fundos. Evento de origem: S-1200,
                        S-2299 ou S-2399. CHAVE_GRUPO: {ind13},
                        {tpValor} CONDICAO_GRUPO: N (se
                        {classTrib}(5001_infoCp_classTrib) = [10] e
                        {codCateg}(../codCateg) = [202]); O (nos demais
                        casos)
                    :ivar calcTerc: Cálculo das contribuições sociais
                        devidas a Outras Entidades e Fundos.
                        CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC (se
                        {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc)
                        = [1]); N (nos demais casos)
                    :ivar infoPerRef: Informações de remuneração por
                        período de referência. CONDICAO_GRUPO: OC
                        CHAVE_GRUPO: {perRef}
                    """
                    matricula: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 30,
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
                    indSimples: Optional[TsIndSimples] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoBaseCS: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoBaseCs"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        }
                    )
                    calcTerc: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.CalcTerc"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 2,
                        }
                    )
                    infoPerRef: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoPerRef"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class InfoBaseCs:
                        """
                        :ivar ind13:
                        :ivar tpValor:
                        :ivar valor: Valor da base de cálculo, dedução
                            ou desconto da contribuição social devida à
                            Previdência Social ou a Outras Entidades e
                            Fundos, conforme definido no campo
                            {tpValor}(./tpValor). Validação: Deve ser
                            maior que 0 (zero). Deve corresponder ao
                            somatório dos valores informados no campo
                            {vrRubr} em S-1200 e S-2299 (grupos
                            {infoPerApur} e {infoPerAnt}), e também em
                            S-2399, obedecendo ao que segue: a) Somar os
                            valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                            em S-1010 seja igual a [1, 3] e subtrair os
                            valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                            em S-1010 seja igual a [2, 4], observando a
                            tabela de relacionamento abaixo:
                            {tpValor}(./tpValor) = [11]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado);
                            {tpValor}(./tpValor) = [12]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e {grauExp} em
                            S-1200/S-2299 = [2]; {tpValor}(./tpValor) =
                            [13]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e {grauExp} em
                            S-1200/S-2299 = [3]; {tpValor}(./tpValor) =
                            [14]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e {grauExp} em
                            S-1200/S-2299 = [4]; {tpValor}(./tpValor) =
                            [15]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado);
                            {tpValor}(./tpValor) = [16]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e {grauExp} em
                            S-1200/S-2299 = [2]; {tpValor}(./tpValor) =
                            [17]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e {grauExp} em
                            S-1200/S-2299 = [3]; {tpValor}(./tpValor) =
                            [18]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e {grauExp} em
                            S-1200/S-2299 = [4]; {tpValor}(./tpValor) =
                            [19],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [15, 16, 21, 22];
                            {tpValor}(./tpValor) = [31],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [51]; {tpValor}(./tpValor) =
                            [32],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [21, 22] ou
                            ({natRubr}(1010_infoRubrica_inclusao_dadosRubrica_natRubr)
                            em S-1010 = [4050, 4051] com
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [9X]); {tpValor}(./tpValor) =
                            [41]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado),
                            observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [42]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e {grauExp} em
                            S-1200/S-2299 = [2], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [43]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e {grauExp} em
                            S-1200/S-2299 = [3], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [44]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [11, 12] e {grauExp} em
                            S-1200/S-2299 = [4], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [45]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado),
                            observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [46]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e {grauExp} em
                            S-1200/S-2299 = [2], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [47]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e {grauExp} em
                            S-1200/S-2299 = [3], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [48]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [13, 14] e {grauExp} em
                            S-1200/S-2299 = [4], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [49],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [15, 16, 21, 22], observado o
                            limite para {codCateg}(../codCateg) = [107,
                            108]; {tpValor}(./tpValor) = [81]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado),
                            observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [82]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e {grauExp} em
                            S-1200/S-2299 = [2], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [83]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e {grauExp} em
                            S-1200/S-2299 = [3], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [84]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e {grauExp} em
                            S-1200/S-2299 = [4], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [85]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado),
                            observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [86]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e {grauExp} em
                            S-1200/S-2299 = [2], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [87]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e {grauExp} em
                            S-1200/S-2299 = [3], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [88]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e {grauExp} em
                            S-1200/S-2299 = [4], observado o limite para
                            {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [91]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado);
                            {tpValor}(./tpValor) = [92]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e {grauExp} em
                            S-1200/S-2299 = [2]; {tpValor}(./tpValor) =
                            [93]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e {grauExp} em
                            S-1200/S-2299 = [3]; {tpValor}(./tpValor) =
                            [94]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [91, 92] e {grauExp} em
                            S-1200/S-2299 = [4]; {tpValor}(./tpValor) =
                            [95]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e ({grauExp} em
                            S-1200/S-2299 = [1] ou não informado);
                            {tpValor}(./tpValor) = [96]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e {grauExp} em
                            S-1200/S-2299 = [2]; {tpValor}(./tpValor) =
                            [97]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e {grauExp} em
                            S-1200/S-2299 = [3]; {tpValor}(./tpValor) =
                            [98]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [95, 96] e {grauExp} em
                            S-1200/S-2299 = [4]. b) Somar os valores das
                            rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                            em S-1010 seja igual a [2, 4] e subtrair os
                            valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                            em S-1010 seja igual a [1, 3], observando a
                            tabela de relacionamento abaixo:
                            {tpValor}(./tpValor) = [21],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [31, 32]; {tpValor}(./tpValor) =
                            [22],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [34]; {tpValor}(./tpValor) =
                            [23],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            em S-1010 = [35]. * Caso
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            da rubrica em S-1010 seja igual a [91, 92,
                            93, 94] e
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                            do respectivo processo em S-1070 seja
                            diferente de [90] (decisão definitiva), o
                            valor também deve ser computado na
                            composição das bases do {tpValor}(./tpValor)
                            = [11, 12, 13, 14, 41, 42, 43, 44]. Se
                            {codCateg}(../codCateg) = [107, 108], caso
                            {tpValor}(./tpValor) = [11] seja maior que o
                            limite do salário-base para essas
                            categorias, então {tpValor}(./tpValor) =
                            [81] é igual a {tpValor}=[41] –
                            ({tpValor}=[11] – {tpValor}=[91]). Se
                            {tpValor}(./tpValor) = [81] resultar
                            negativo, informar 0 (zero). O mesmo se
                            aplica para {tpValor}(./tpValor) = [82, 83,
                            84]. ** Caso
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                            da rubrica em S-1010 seja igual a [95, 96,
                            97, 98] e
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                            do respectivo processo em S-1070 seja
                            diferente de [90] (decisão definitiva), o
                            valor também deve ser computado na
                            composição das bases do {tpValor}(./tpValor)
                            = [15, 16, 17, 18, 45, 46, 47, 48]. Se
                            {codCateg}(../codCateg) = [107, 108], caso
                            {tpValor}(./tpValor) = [15] seja maior que o
                            limite do salário-base para essas
                            categorias, então {tpValor}(./tpValor) =
                            [85] é igual a {tpValor}=[45] –
                            ({tpValor}=[15] – {tpValor}=[95]). Se
                            {tpValor}(./tpValor) = [85] resultar
                            negativo, informar 0 (zero). O mesmo se
                            aplica para {tpValor}(./tpValor) = [86, 87,
                            88]. *** Caso
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                            do respectivo processo em S-1070 seja igual
                            a [90] (decisão definitiva), o valor não
                            deve ser computado.
                        """
                        ind13: Optional[TsInd13] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        tpValor: Optional[InfoBaseCsTpValor] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        valor: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": Decimal("0"),
                                "max_inclusive": Decimal("999999999999.99"),
                                "total_digits": 14,
                                "fraction_digits": 2,
                            }
                        )

                    @dataclass
                    class CalcTerc:
                        """
                        :ivar tpCR:
                        :ivar vrCsSegTerc: Valor da contribuição social
                            devida a Outras Entidades ou Fundos,
                            calculada segundo a legislação em vigor, por
                            CR. Validação: {calcTerc/tpCR}(./tpCR) =
                            [121802] - Somatório de
                            {valor}(../infoBaseCS_valor) quando
                            {tpValor}(../infoBaseCS_tpValor) = [11, 12,
                            13, 14], multiplicado pela alíquota de 1,5%,
                            se {codCateg}(../codCateg) = [711, 712, 734]
                            (transportador autônomo) e
                            {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc)
                            = [1]; {calcTerc/tpCR}(./tpCR) = [122102] -
                            Somatório de {valor}(../infoBaseCS_valor)
                            quando {tpValor}(../infoBaseCS_tpValor) =
                            [11, 12, 13, 14], multiplicado pela alíquota
                            de 1,0%, se {codCateg}(../codCateg) = [711,
                            712, 734] (transportador autônomo) e
                            {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc)
                            = [1]. OBS.: No período de 04/2020 a
                            06/2020, as alíquotas devem ser 0,75% para o
                            SEST e 0,5% para o SENAT.
                        :ivar vrDescTerc: Valor efetivamente descontado
                            do segurado, correspondente a
                            {tpValor}(../infoBaseCS_tpValor) = [22, 23],
                            do correspondente {calcTerc/tpCR}(./tpCR).
                        """
                        tpCR: Optional[CalcTercTpCr] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        vrCsSegTerc: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": Decimal("0"),
                                "max_inclusive": Decimal("999999999999.99"),
                                "total_digits": 14,
                                "fraction_digits": 2,
                            }
                        )
                        vrDescTerc: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": Decimal("0"),
                                "max_inclusive": Decimal("999999999999.99"),
                                "total_digits": 14,
                                "fraction_digits": 2,
                            }
                        )

                    @dataclass
                    class InfoPerRef:
                        """
                        :ivar perRef: Informar o período ao qual se
                            refere a remuneração. Origem:
                            {perApur}(5001_ideEvento_perApur) ou campo
                            {perRef} de S-1200/S-2299.
                        :ivar ideADC: Instrumento ou situação ensejadora
                            da remuneração em períodos anteriores
                            DESCRICAO_COMPLETA:Identificação do
                            instrumento ou situação ensejadora da
                            remuneração relativa a períodos de apuração
                            anteriores. Evento de origem: S-1200 ou
                            S-2299 (exceto {remunSuc}(./remunSuc), cujo
                            evento de origem somente é S-1200).
                            CHAVE_GRUPO: {dtAcConv}, {tpAcConv}
                            CONDICAO_GRUPO: OC
                        :ivar detInfoPerRef: Detalhamento das
                            informações de remuneração por período de
                            referência DESCRICAO_COMPLETA:Detalhamento
                            das informações de remuneração por período
                            de referência. Deve ser preenchido com
                            informações de {infoPerApur} e {infoPerAnt}
                            do S-1200 e S-2299, e de {dmDev} do S-2399,
                            quando houver. CHAVE_GRUPO: {ind13},
                            {tpVrPerRef}
                        """
                        perRef: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 4,
                                "max_length": 7,
                                "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
                            }
                        )
                        ideADC: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoPerRef.IdeAdc"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                            }
                        )
                        detInfoPerRef: List["ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoPerRef.DetInfoPerRef"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 99,
                            }
                        )

                        @dataclass
                        class IdeAdc:
                            """
                            :ivar dtAcConv: Data da assinatura do
                                acordo, convenção coletiva, sentença
                                normativa ou da conversão da licença
                                saúde em acidente de trabalho.
                            :ivar tpAcConv:
                            :ivar dsc:
                            :ivar remunSuc: Indicar se a remuneração é
                                relativa a verbas de natureza salarial
                                ou não salarial devidas pela empresa
                                sucessora a empregados desligados ainda
                                na sucedida.
                            """
                            dtAcConv: Optional[XmlDate] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                }
                            )
                            tpAcConv: Optional[TsTpAcConv] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            dsc: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_length": 1,
                                    "max_length": 255,
                                    "pattern": r"[^\s]{1}[\S\s]*",
                                }
                            )
                            remunSuc: Optional[TsSimNao] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                }
                            )

                        @dataclass
                        class DetInfoPerRef:
                            """
                            :ivar ind13:
                            :ivar tpVrPerRef:
                            :ivar vrPerRef: Valor da base de cálculo,
                                dedução ou desconto da contribuição
                                social, conforme definido no campo
                                {tpVrPerRef}(./tpVrPerRef). Validação:
                                Deve ser maior que 0 (zero). Deve
                                corresponder ao somatório dos valores
                                informados no campo {vrRubr} em S-1200 e
                                S-2299 (grupos {infoPerApur} e
                                {infoPerAnt}), e também em S-2399,
                                obedecendo ao que segue: a) Somar os
                                valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                                em S-1010 seja igual a [1, 3] e subtrair
                                os valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                                em S-1010 seja igual a [2, 4],
                                observando a tabela de relacionamento
                                abaixo: {tpVrPerRef}(./tpVrPerRef) =
                                [11]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [11, 12] e ({grauExp} em
                                S-1200/S-2299 = [1] ou não informado);
                                {tpVrPerRef}(./tpVrPerRef) = [12]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [11, 12] e {grauExp} em
                                S-1200/S-2299 = [2];
                                {tpVrPerRef}(./tpVrPerRef) = [13]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [11, 12] e {grauExp} em
                                S-1200/S-2299 = [3];
                                {tpVrPerRef}(./tpVrPerRef) = [14]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [11, 12] e {grauExp} em
                                S-1200/S-2299 = [4];
                                {tpVrPerRef}(./tpVrPerRef) = [15]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [13, 14] e ({grauExp} em
                                S-1200/S-2299 = [1] ou não informado);
                                {tpVrPerRef}(./tpVrPerRef) = [16]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [13, 14] e {grauExp} em
                                S-1200/S-2299 = [2];
                                {tpVrPerRef}(./tpVrPerRef) = [17]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [13, 14] e {grauExp} em
                                S-1200/S-2299 = [3];
                                {tpVrPerRef}(./tpVrPerRef) = [18]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [13, 14] e {grauExp} em
                                S-1200/S-2299 = [4];
                                {tpVrPerRef}(./tpVrPerRef) = [19],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [15, 16, 21, 22];
                                {tpVrPerRef}(./tpVrPerRef) = [31],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [51];
                                {tpVrPerRef}(./tpVrPerRef) = [32],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [21, 22] ou
                                ({natRubr}(1010_infoRubrica_inclusao_dadosRubrica_natRubr)
                                em S-1010 = [4050, 4051] com
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [9X]). b) Somar os valores
                                das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                                em S-1010 seja igual a [2, 4] e subtrair
                                os valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                                em S-1010 seja igual a [1, 3],
                                observando a tabela de relacionamento
                                abaixo: {tpVrPerRef}(./tpVrPerRef) =
                                [21],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [31, 32];
                                {tpVrPerRef}(./tpVrPerRef) = [22],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [34];
                                {tpVrPerRef}(./tpVrPerRef) = [23],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                em S-1010 = [35]. * Caso
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                da rubrica em S-1010 seja igual a [91,
                                92, 93, 94] e
                                {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                                do respectivo processo em S-1070 seja
                                diferente de [90] (decisão definitiva),
                                o valor deve ser computado na composição
                                das bases do {tpVrPerRef}(./tpVrPerRef)
                                = [11, 12, 13, 14]. ** Caso
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP)
                                da rubrica em S-1010 seja igual a [95,
                                96, 97, 98] e
                                {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                                do respectivo processo em S-1070 seja
                                diferente de [90] (decisão definitiva),
                                o valor deve ser computado na composição
                                das bases do {tpVrPerRef}(./tpVrPerRef)
                                = [15, 16, 17, 18]. *** Caso
                                {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                                do respectivo processo em S-1070 seja
                                igual a [90] (decisão definitiva), o
                                valor não deve ser computado.
                            """
                            ind13: Optional[TsInd13] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            tpVrPerRef: Optional[DetInfoPerRefTpVrPerRef] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            vrPerRef: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
