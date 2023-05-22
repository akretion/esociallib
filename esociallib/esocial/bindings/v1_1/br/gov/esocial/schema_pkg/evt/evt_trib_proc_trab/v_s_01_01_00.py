from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from esociallib.esocial.bindings.v1_1.org.w3.pkg_2000.pkg_09.xmldsig import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00"


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        }
    )
    emailPrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    nmCid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    paisNascto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    paisNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{4}",
        }
    )


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}",
        }
    )
    codMunic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{7}",
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    tmpParc: Optional[TsTmpParc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    horNoturno: Optional[TsSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    dscJorn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiTodos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nivEstagio: Optional[TInfoEstagiarioNivEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    areaAtuacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrApol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtPrevTerm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    instEnsino: Optional["TInfoEstagiario.InstEnsino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    ageIntegracao: Optional["TInfoEstagiario.AgeIntegracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    supervisorEstagio: Optional["TInfoEstagiario.SupervisorEstagio"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "pattern": r"\d{14}",
            }
        )
        nmRazao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        dscLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        nrLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            }
        )
        bairro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            }
        )
        cep: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "pattern": r"\d{8}",
            }
        )
        codMunic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "pattern": r"\d{7}",
            }
        )
        uf: Optional[TsUf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    remunOutrEmpr: List["TInfoMv.RemunOutrEmpr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        }
    )
    descRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
        }
    )
    ideAdv: List["TInfoRra.IdeAdv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )
    codSusp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    dscSalVar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtAdm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class ESocial:
    """S-5501 - Informações Consolidadas de Tributos Decorrentes de Processo Trabalhista

    :ivar evtTribProcTrab: Evento Informações Consolidadas de Tributos
        Decorrentes de Processo Trabalhista. CHAVE_GRUPO: {Id}
    :ivar signature:
    """
    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_01_00"

    evtTribProcTrab: Optional["ESocial.EvtTribProcTrab"] = field(
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
    class EvtTribProcTrab:
        """
        :ivar ideEvento: Informações de identificação do evento.
        :ivar ideEmpregador: Informações de identificação do empregador
            ou do contribuinte que prestou a informação. CHAVE_GRUPO:
            {tpInsc*}, {nrInsc*}
        :ivar ideProc: Identificação do processo. CHAVE_GRUPO:
            {nrProcTrab*}, {perApur*}
        :ivar Id:
        """
        ideEvento: Optional["ESocial.EvtTribProcTrab.IdeEvento"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        ideEmpregador: Optional["ESocial.EvtTribProcTrab.IdeEmpregador"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        ideProc: Optional["ESocial.EvtTribProcTrab.IdeProc"] = field(
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
        class IdeEvento:
            """
            :ivar nrRecArqBase: Preencher com o número do recibo do
                arquivo que deu origem ao presente arquivo de retorno.
                Validação: Deve ser um recibo de entrega válido,
                correspondente ao arquivo que deu origem ao presente
                arquivo de retorno (S-2501 ou S-3500).
            """
            nrRecArqBase: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "length": 23,
                    "pattern": r"[1]{1}\.\d{1}\.\d{19}",
                }
            )

        @dataclass
        class IdeEmpregador:
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo
                de inscrição do empregador ou contribuinte que prestou a
                informação, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do empregador
                ou contribuinte que prestou a informação, de acordo com
                o tipo de inscrição indicado no campo
                {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em
                S-1000.
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
                    "pattern": r"\d{8}|\d{11}|\d{14}",
                }
            )

        @dataclass
        class IdeProc:
            """
            :ivar nrProcTrab: Número do processo trabalhista, da ata ou
                número de identificação da conciliação. Validação: a) Se
                o evento de origem for S-2501, retornar o campo
                {nrProcTrab}(2501_ideProc_nrProcTrab) desse evento; b)
                Se o evento de origem for S-3500, retornar o campo
                {nrProcTrab}(2501_ideProc_nrProcTrab) do evento S-2501
                objeto da exclusão.
            :ivar perApur: Mês/ano em que é devida a obrigação de pagar
                a parcela prevista no acordo/sentença. Validação: a) Se
                o evento de origem for S-2501, retornar o campo
                {perApurPgto}(2501_ideProc_perApurPgto) desse evento; b)
                Se o evento de origem for S-3500, retornar o campo
                {perApurPgto}(2501_ideProc_perApurPgto) do evento S-2501
                objeto da exclusão.
            :ivar infoTributos: Identificação do período e da base de
                cálculo dos tributos referentes ao processo trabalhista.
                CHAVE_GRUPO: {perRef}
            :ivar infoCRIRRF: Informações de IRRF referentes ao processo
                trabalhista. DESCRICAO_COMPLETA:Informações de Imposto
                de Renda Retido na Fonte, consolidadas por Código de
                Receita - CR. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
            """
            nrProcTrab: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"\d{15}|\d{20}",
                }
            )
            perApur: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "length": 7,
                    "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
                }
            )
            infoTributos: List["ESocial.EvtTribProcTrab.IdeProc.InfoTributos"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 999,
                }
            )
            infoCRIRRF: List["ESocial.EvtTribProcTrab.IdeProc.InfoCrirrf"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                }
            )

            @dataclass
            class InfoTributos:
                """
                :ivar perRef: Informar o mês/ano (formato AAAA-MM) de
                    referência das informações. Validação: a) Se o
                    evento de origem for S-2501, retornar o campo
                    {perRef}(2501_ideTrab_calcTrib_perRef) desse evento;
                    b) Se o evento de origem for S-3500, retornar o
                    campo {perRef}(2501_ideTrab_calcTrib_perRef) do
                    evento S-2501 objeto da exclusão.
                :ivar infoCRContrib: Informações das contribuições
                    sociais referentes ao processo trabalhista.
                    DESCRICAO_COMPLETA:Informações das contribuições
                    sociais devidas à Previdência Social e Outras
                    Entidades e Fundos, consolidadas por
                    {perRef}(../perRef) e por Código de Receita - CR.
                    CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
                """
                perRef: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "length": 7,
                        "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
                    }
                )
                infoCRContrib: List["ESocial.EvtTribProcTrab.IdeProc.InfoTributos.InfoCrcontrib"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )

                @dataclass
                class InfoCrcontrib:
                    """
                    :ivar tpCR:
                    :ivar vrCR: Valor correspondente ao Código de
                        Receita - CR. Validação: Deve ser apurado de
                        acordo com a legislação em vigor na competência.
                        Deve ser maior que 0 (zero).
                    """
                    tpCR: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{6}",
                        }
                    )
                    vrCR: Optional[Decimal] = field(
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
            class InfoCrirrf:
                """
                :ivar tpCR:
                :ivar vrCR: Valor correspondente ao Código de Receita -
                    CR. Validação: Deve ser apurado de acordo com a
                    legislação em vigor na competência. Deve ser maior
                    que 0 (zero).
                """
                tpCR: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{6}",
                    }
                )
                vrCR: Optional[Decimal] = field(
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
