from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from esociallib.esocial.bindings.v1_1.org.w3.pkg_2000.pkg_09.xmldsig import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00"


class TsGrauExp(Enum):
    """
    Preencher com o código que representa o grau de exposição a agentes nocivos,
    conforme Tabela 02.

    :cvar VALUE_1: Não ensejador de aposentadoria especial
    :cvar VALUE_2: Ensejador de aposentadoria especial - FAE15_12% (15
        anos de contribuição e alíquota de 12%)
    :cvar VALUE_3: Ensejador de aposentadoria especial - FAE20_09% (20
        anos de contribuição e alíquota de 9%)
    :cvar VALUE_4: Ensejador de aposentadoria especial - FAE25_06% (25
        anos de contribuição e alíquota de 6%)
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


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


class TsTpProc12(Enum):
    """
    Preencher com o código correspondente ao tipo de processo.

    :cvar VALUE_1: Administrativo
    :cvar VALUE_2: Judicial
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsTpRegPrev123(Enum):
    """
    Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares das
    Forças Armadas).

    :cvar VALUE_1: Regime Geral de Previdência Social - RGPS
    :cvar VALUE_2: Regime Próprio de Previdência Social - RPPS
    :cvar VALUE_3: Regime de Previdência Social no exterior
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        }
    )
    emailPrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    nmCid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    paisNascto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    paisNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{4}",
        }
    )


class InfoCcpTpCcp(Enum):
    """
    Indicar o âmbito de celebração do acordo.

    :cvar VALUE_1: CCP no âmbito de empresa
    :cvar VALUE_2: CCP no âmbito de sindicato
    :cvar VALUE_3: NINTER
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoContrTpContr(Enum):
    """
    Tipo de contrato a que se refere o processo judicial ou a demanda submetida à
    CCP ou ao NINTER.

    :cvar VALUE_1: Trabalhador com vínculo formalizado, sem alteração
        nas datas de admissão e de desligamento
    :cvar VALUE_2: Trabalhador com vínculo formalizado, com alteração na
        data de admissão
    :cvar VALUE_3: Trabalhador com vínculo formalizado, com inclusão ou
        alteração de data de desligamento
    :cvar VALUE_4: Trabalhador com vínculo formalizado, com alteração
        nas datas de admissão e de desligamento
    :cvar VALUE_5: Empregado com reconhecimento de vínculo
    :cvar VALUE_6: Trabalhador sem vínculo de emprego/estatutário
        (TSVE), sem reconhecimento de vínculo empregatício
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class InfoProcessoOrigem(Enum):
    """
    Informar a origem do processo/demanda.

    :cvar VALUE_1: Processo judicial
    :cvar VALUE_2: Demanda submetida à CCP ou ao NINTER
    """
    VALUE_1 = 1
    VALUE_2 = 2


class InfoTermMtvDesligTsv(Enum):
    """Motivo do término do diretor não empregado, com FGTS.

    Validação: Informação obrigatória e exclusiva se {infoContr/codCateg}(2500_ideTrab_infoContr_codCateg) = [721].

    :cvar VALUE_01: Exoneração do diretor não empregado sem justa causa,
        por deliberação da assembleia, dos sócios cotistas ou da
        autoridade competente
    :cvar VALUE_02: Término de mandato do diretor não empregado que não
        tenha sido reconduzido ao cargo
    :cvar VALUE_03: Exoneração a pedido de diretor não empregado
    :cvar VALUE_04: Exoneração do diretor não empregado por culpa
        recíproca ou força maior
    :cvar VALUE_05: Morte do diretor não empregado
    :cvar VALUE_06: Exoneração do diretor não empregado por falência,
        encerramento ou supressão de parte da empresa
    :cvar VALUE_99: Outros
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_99 = "99"


class InfoVlrRepercProc(Enum):
    """
    Repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER.

    :cvar VALUE_1: Decisão com pagamento de verbas de natureza
        remuneratória
    :cvar VALUE_2: Decisão sem pagamento de verbas de natureza
        remuneratória
    """
    VALUE_1 = 1
    VALUE_2 = 2


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}",
        }
    )
    codMunic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{7}",
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    tmpParc: Optional[TsTmpParc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    horNoturno: Optional[TsSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    dscJorn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiTodos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nivEstagio: Optional[TInfoEstagiarioNivEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    areaAtuacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrApol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtPrevTerm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    instEnsino: Optional["TInfoEstagiario.InstEnsino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    ageIntegracao: Optional["TInfoEstagiario.AgeIntegracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    supervisorEstagio: Optional["TInfoEstagiario.SupervisorEstagio"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "pattern": r"\d{14}",
            }
        )
        nmRazao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        dscLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        nrLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            }
        )
        bairro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            }
        )
        cep: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "pattern": r"\d{8}",
            }
        )
        codMunic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "pattern": r"\d{7}",
            }
        )
        uf: Optional[TsUf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    remunOutrEmpr: List["TInfoMv.RemunOutrEmpr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        }
    )
    descRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
        }
    )
    ideAdv: List["TInfoRra.IdeAdv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )
    codSusp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    dscSalVar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtAdm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class ESocial:
    """S-2500 - Processo Trabalhista

    :ivar evtProcTrab: Evento Processo Trabalhista. CHAVE_GRUPO: {Id}
        REGRA:REGRA_BASES_PROC_TRAB
        REGRA:REGRA_BLOQUEIA_USO_CPF_EMPREGADOR
        REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_MUDANCA_CATEG_NAT_ATIV
        REGRA:REGRA_UNICIDADE_CONTRATUAL REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_MATRICULA REGRA:REGRA_VALIDA_PROC_TRAB
        REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar signature:
    """
    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00"

    evtProcTrab: Optional["ESocial.EvtProcTrab"] = field(
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
    class EvtProcTrab:
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador
            ou do contribuinte que está prestando a informação.
            CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar infoProcesso: Informações do processo judicial ou de
            demanda submetida à CCP ou ao NINTER. CHAVE_GRUPO:
            {nrProcTrab*} DESCRICAO_COMPLETA: Informações do processo
            judicial ou de demanda submetida à Comissão de Conciliação
            Prévia (CCP) ou ao Núcleo Intersindical de Conciliação
            Trabalhista (NINTER).
        :ivar ideTrab: Informações do trabalhador. CHAVE_GRUPO:
            {cpfTrab*}
        :ivar Id:
        """
        ideEvento: Optional[TIdeEventoTrab] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        ideEmpregador: Optional["ESocial.EvtProcTrab.IdeEmpregador"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        infoProcesso: Optional["ESocial.EvtProcTrab.InfoProcesso"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        ideTrab: Optional["ESocial.EvtProcTrab.IdeTrab"] = field(
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
        class IdeEmpregador:
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo
                de inscrição do empregador ou contribuinte que está
                prestando a informação, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do empregador
                ou contribuinte que está prestando a informação, de
                acordo com o tipo de inscrição indicado no campo
                {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em
                S-1000.
            :ivar ideResp: Identificação do contribuinte, caso tenha
                havido imposição de responsabilidade indireta.
                DESCRICAO_COMPLETA: Informações de identificação do
                contribuinte (responsável direto), caso tenha havido
                imposição de responsabilidade indireta. CONDICAO_GRUPO:
                OC
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
            ideResp: Optional["ESocial.EvtProcTrab.IdeEmpregador.IdeResp"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )

            @dataclass
            class IdeResp:
                """
                :ivar tpInsc:
                :ivar nrInsc: Informar o número de inscrição do
                    contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideResp/tpInsc}(./tpInsc).
                    Validação: Deve ser um identificador válido e: a) Se
                    {ideResp/tpInsc}(./tpInsc) = [1], deve ser informado
                    com 14 (catorze) algarismos. Se o empregador for
                    pessoa jurídica, a raiz do CNPJ informado deve ser
                    diferente de {ideEmpregador/nrInsc}(../nrInsc),
                    exceto se {ideEmpregador/nrInsc}(../nrInsc) tiver 14
                    (catorze) algarismos. b) Se
                    {ideResp/tpInsc}(./tpInsc) = [2], deve ser diferente
                    do CPF do trabalhador. Se o empregador for pessoa
                    física, também deve ser diferente do CPF do
                    empregador.
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
        class InfoProcesso:
            """
            :ivar origem:
            :ivar nrProcTrab: Número do processo trabalhista, da ata ou
                número de identificação da conciliação. Validação: Se
                {origem}(./origem) = [1], deve ser um processo judicial
                válido, com 20 (vinte) algarismos. Se {origem}(./origem)
                = [2], deve possuir 15 (quinze) algarismos.
            :ivar obsProcTrab: Observações relacionadas ao processo
                judicial ou à demanda submetida à CCP ou ao NINTER.
            :ivar dadosCompl: Informações complementares do processo ou
                da demanda.
            """
            origem: Optional[InfoProcessoOrigem] = field(
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
                    "required": True,
                    "pattern": r"\d{15}|\d{20}",
                }
            )
            obsProcTrab: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 999,
                    "pattern": r"[^\s]{1}[\S\s]*",
                }
            )
            dadosCompl: Optional["ESocial.EvtProcTrab.InfoProcesso.DadosCompl"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class DadosCompl:
                """
                :ivar infoProcJud: Informações complementares do
                    processo judicial. CONDICAO_GRUPO: O (se
                    {origem}(2500_infoProcesso_origem) = [1]); N (nos
                    demais casos)
                :ivar infoCCP: Informações complementares da demanda
                    submetida à CCP ou ao NINTER. CONDICAO_GRUPO: O (se
                    {origem}(2500_infoProcesso_origem) = [2]); N (nos
                    demais casos)
                """
                infoProcJud: Optional["ESocial.EvtProcTrab.InfoProcesso.DadosCompl.InfoProcJud"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                infoCCP: Optional["ESocial.EvtProcTrab.InfoProcesso.DadosCompl.InfoCcp"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass
                class InfoProcJud:
                    """
                    :ivar dtSent: Informar a data do(a): a) Trânsito em
                        julgado da decisão líquida proferida no processo
                        trabalhista; b) Homologação de acordo judicial;
                        ou c) Trânsito em julgado da decisão
                        homologatória dos cálculos de liquidação da
                        sentença. Validação: Deve ser igual ou anterior
                        à data atual.
                    :ivar ufVara: Preencher com a sigla da Unidade da
                        Federação onde está localizada a Vara em que o
                        processo tramitou.
                    :ivar codMunic:
                    :ivar idVara:
                    """
                    dtSent: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    ufVara: Optional[TsUf] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    codMunic: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{7}",
                        }
                    )
                    idVara: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{1,4}",
                        }
                    )

                @dataclass
                class InfoCcp:
                    """
                    :ivar dtCCP: Data da celebração do acordo celebrado
                        perante CCP ou Ninter. Validação: Deve ser igual
                        ou anterior à data atual.
                    :ivar tpCCP:
                    :ivar cnpjCCP: Identificar o CNPJ do sindicato
                        representativo do trabalhador, no âmbito da CCP
                        ou NINTER. Validação: O preenchimento é
                        obrigatório e exclusivo se {tpCCP}(./tpCCP) for
                        igual a [2] ou [3]. Deve ser um número de CNPJ
                        válido.
                    """
                    dtCCP: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    tpCCP: Optional[InfoCcpTpCcp] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    cnpjCCP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{14}",
                        }
                    )

        @dataclass
        class IdeTrab:
            """
            :ivar cpfTrab:
            :ivar nmTrab: Informar o nome do trabalhador. Validação:
                Preenchimento obrigatório se não existir contrato com
                {indContr}(2500_ideTrab_infoContr_indContr) = [S].
            :ivar dtNascto: Preencher com a data de nascimento.
                Validação: Preenchimento obrigatório se não existir
                contrato com {indContr}(2500_ideTrab_infoContr_indContr)
                = [S]. Deve ser maior ou igual que 01/01/1890 e menor ou
                igual à data atual.
            :ivar dependente: Informações dos dependentes. CHAVE_GRUPO:
                {cpfDep} CONDICAO_GRUPO: OC (se existir contrato com
                {indContr}(2500_ideTrab_infoContr_indContr) = [N]); N
                (nos demais casos)
            :ivar infoContr: Informações do contrato de trabalho.
                CHAVE_GRUPO: {matricula}, {codCateg}, {dtInicio}
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
                    "min_length": 2,
                    "max_length": 70,
                    "pattern": r".*[^\s].*",
                }
            )
            dtNascto: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": XmlDate(1890, 1, 1),
                }
            )
            dependente: List["ESocial.EvtProcTrab.IdeTrab.Dependente"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                }
            )
            infoContr: List["ESocial.EvtProcTrab.IdeTrab.InfoContr"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                }
            )

            @dataclass
            class Dependente:
                """
                :ivar cpfDep: Número de inscrição no CPF. Validação:
                    Deve ser um número de CPF válido e diferente do CPF
                    do trabalhador. Em arquivo de empregador Pessoa
                    Física, também deve ser diferente do CPF informado
                    em
                    {ideEmpregador/nrInsc}(2500_ideEmpregador_nrInsc).
                :ivar tpDep:
                :ivar descDep: Informar a descrição da dependência.
                    Validação: Informação obrigatória e exclusiva se
                    {tpDep}(./tpDep) = [99].
                """
                cpfDep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{11}",
                    }
                )
                tpDep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{2}",
                    }
                )
                descDep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )

            @dataclass
            class InfoContr:
                """
                :ivar tpContr:
                :ivar indContr: Indicativo se o contrato possui
                    informação no evento S-2190, S-2200 ou S-2300 no
                    declarante. Validação: Deve ser igual a [N] se o
                    grupo {ideResp}(2500_ideEmpregador_ideResp) for
                    informado.
                :ivar dtAdmOrig: Preencher com a data de admissão
                    original do vínculo (data de admissão antes da
                    alteração). Validação: Preenchimento obrigatório e
                    exclusivo se {infoContr/tpContr}(./tpContr) = [2, 4]
                    e se {indContr}(./indContr) = [N]. Deve ser
                    posterior à data de nascimento do trabalhador.
                :ivar indReint: Indicativo de reintegração do empregado.
                    Validação: Preenchimento obrigatório e exclusivo se
                    {infoContr/tpContr}(./tpContr) for diferente de [6]
                    e {indContr}(./indContr) = [S]. Caso seja informado
                    [S], deve existir evento de reintegração (S-2298)
                    para a matrícula abaixo informada, com o número de
                    processo nesse evento igual a
                    {nrProcTrab}(2500_infoProcesso_nrProcTrab).
                :ivar indCateg: Indicativo se houve reconhecimento de
                    categoria do trabalhador diferente da informada (no
                    eSocial ou na GFIP) pelo declarante.
                :ivar indNatAtiv: Indicativo se houve reconhecimento de
                    natureza da atividade diferente da cadastrada pelo
                    declarante.
                :ivar indMotDeslig: Indicativo se houve reconhecimento
                    de motivo de desligamento diferente do informado
                    pelo declarante.
                :ivar indUnic: Indicativo se houve reconhecimento de
                    unicidade contratual (declaração da continuidade do
                    contrato de trabalho, considerando como único dois
                    ou mais vínculos sucessivos informados no eSocial).
                    Validação: Deve ser igual a [N] se o grupo
                    {ideResp}(2500_ideEmpregador_ideResp) for informado.
                :ivar matricula: Matrícula atribuída ao trabalhador pela
                    empresa ou, no caso de servidor público, a matrícula
                    constante no Sistema de Administração de Recursos
                    Humanos do órgão. Se {indContr}(./indContr) = [N],
                    deve ser criada uma matrícula para o trabalhador. Se
                    {indContr}(./indContr) = [S], deve corresponder à
                    matrícula informada pelo empregador no evento
                    S-2190, S-2200 ou S-2300 do respectivo contrato. O
                    campo não deve ser informado somente no caso de TSVE
                    cadastrado em versão do leiaute anterior a S-1.0. Se
                    {indUnic}(./indUnic) = [S], deve ser preenchida a
                    matrícula que incorporará as demais (informadas no
                    grupo
                    {unicContr}(2500_ideTrab_infoContr_unicContr)).
                    Validação: Se {indContr}(./indContr) = [N], deve ser
                    aplicada a regra de validação abaixo. Além disso, o
                    valor informado neste campo não pode conter a
                    expressão 'eSocial' nas 7 (sete) primeiras posições.
                    Se {indContr}(./indContr) = [S], deve corresponder a
                    uma matrícula existente no Registro de Eventos
                    Trabalhistas - RET para o respectivo trabalhador.
                    REGRA:REGRA_CARACTERE_ESPECIAL
                :ivar codCateg: Preencher com o código da categoria do
                    trabalhador. Validação: Informação obrigatória e
                    exclusiva se {indContr}(./indContr) = [N] ou se o
                    campo {matricula}(./matricula) não estiver
                    preenchido. Deve ser um código válido e existente na
                    Tabela 01 e obedecer ao que segue: a) Se o campo
                    {matricula}(./matricula) não estiver preenchido,
                    deve ser igual ao código de categoria informado no
                    evento S-2300; b) Se {indContr}(./indContr) = [N] e
                    {infoContr/tpContr}(./tpContr) for diferente de [6],
                    deve ser um código de categoria compatível com o
                    evento S-2200 (conforme regra de validação abaixo);
                    c) Se {indContr}(./indContr) = [N] e
                    {infoContr/tpContr}(./tpContr) = [6], deve ser um
                    código de categoria compatível com o evento S-2300
                    (conforme regra de validação abaixo).
                    REGRA:REGRA_COMPATIB_CATEG_EVENTO
                :ivar dtInicio: Data de início de TSVE, que pode ser: a)
                    Para o cooperado, a data de ingresso na cooperativa;
                    b) Para o diretor não empregado, a data de posse no
                    cargo; c) Para o dirigente sindical, a data de
                    início do mandato no sindicato; d) Para o
                    estagiário, a data de início do estágio; e) Para o
                    trabalhador avulso, a data de ingresso no Órgão
                    Gestor de Mão de Obra - OGMO ou no sindicato; f)
                    Para o servidor público exercente de cargo eletivo,
                    a data de início do mandato; g) Para os demais
                    trabalhadores, a data de início das atividades.
                    Validação: Informação obrigatória e exclusiva se
                    ({infoContr/tpContr}(./tpContr) = [6] e
                    {indContr}(./indContr) = [N]) ou se o campo
                    {matricula}(./matricula) não estiver preenchido.
                    Deve ser posterior à data de nascimento do
                    trabalhador. Se o campo {matricula}(./matricula) não
                    estiver preenchido, deve ser igual à data de início
                    informada no evento S-2300.
                :ivar infoCompl: Informações complementares do contrato
                    de trabalho. CONDICAO_GRUPO: O (se
                    {indContr}(../indContr) = [N]); N (nos demais casos)
                :ivar mudCategAtiv: Informação do novo código de
                    categoria e/ou da nova natureza da atividade.
                    DESCRICAO_COMPLETA:Informação do novo código de
                    categoria e/ou da nova natureza da atividade, no
                    caso de reconhecimento judicial nesse sentido.
                    CHAVE_GRUPO: {dtMudCategAtiv} CONDICAO_GRUPO: OC (se
                    {indCateg}(../indCateg) = [S] ou se
                    {indNatAtiv}(../indNatAtiv) = [S]); N (nos demais
                    casos)
                :ivar unicContr: Informações dos vínculos/contratos
                    incorporados. DESCRICAO_COMPLETA:Informações dos
                    vínculos/contratos incorporados, no caso de
                    reconhecimento de unicidade contratual. CHAVE_GRUPO:
                    {matUnic}, {codCateg}, {dtInicio} CONDICAO_GRUPO: O
                    (se {indUnic}(2500_ideTrab_infoContr_indUnic) =
                    [S]); N (nos demais casos)
                :ivar ideEstab: Identificação do estabelecimento.
                    DESCRICAO_COMPLETA:Identificação do estabelecimento
                    responsável pelo pagamento ao trabalhador dos
                    valores informados neste evento.
                """
                tpContr: Optional[InfoContrTpContr] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                indContr: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                dtAdmOrig: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                indReint: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                indCateg: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                indNatAtiv: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                indMotDeslig: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                indUnic: Optional[TsSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                matricula: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )
                codCateg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{3}",
                    }
                )
                dtInicio: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                infoCompl: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                mudCategAtiv: List["ESocial.EvtProcTrab.IdeTrab.InfoContr.MudCategAtiv"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )
                unicContr: List["ESocial.EvtProcTrab.IdeTrab.InfoContr.UnicContr"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )
                ideEstab: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass
                class InfoCompl:
                    """
                    :ivar codCBO: Classificação Brasileira de Ocupações
                        - CBO. Validação: Preenchimento obrigatório se
                        {infoContr/codCateg}(../codCateg) for diferente
                        de [901, 903, 904]). Se informado, deve ser um
                        código válido e existente na tabela de CBO, com
                        6 (seis) posições.
                    :ivar natAtividade: Natureza da atividade.
                        Validação: Preenchimento obrigatório se
                        {infoContr/codCateg}(../codCateg) for relativo a
                        "Empregado", "Agente Público", "Avulso" ou igual
                        a [401, 731, 734, 738]. Não deve ser preenchido
                        se {infoContr/codCateg}(../codCateg) = [721,
                        722, 771, 901]. Se
                        {infoContr/codCateg}(../codCateg) = [104], deve
                        ser preenchido com [1]. Se
                        {infoContr/codCateg}(../codCateg) = [102], deve
                        ser preenchido com [2].
                    :ivar remuneracao: Informações da remuneração e
                        periodicidade de pagamento. CHAVE_GRUPO:
                        {dtRemun} CONDICAO_GRUPO: N (se
                        ({infoContr/tpContr}(../../tpContr) for
                        diferente de [6] e
                        {tpRegTrab}(../infoVinc_tpRegTrab) = [2]); O (se
                        ({infoContr/tpContr}(../../tpContr) for
                        diferente de [6] e
                        {tpRegTrab}(../infoVinc_tpRegTrab) = [1]) ou se
                        {infoContr/codCateg}(../../codCateg) = [721,
                        722, 771]); OC (nos demais casos)
                    :ivar infoVinc: Informações sobre o vínculo
                        trabalhista. CONDICAO_GRUPO: O (se
                        {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr)
                        for diferente de [6]); N (nos demais casos)
                    :ivar infoTerm: Informações de término de TSVE.
                        CONDICAO_GRUPO: OC (se
                        {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr)
                        = [6]; N (nos demais casos)
                    """
                    codCBO: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{6}",
                        }
                    )
                    natAtividade: Optional[TsNatAtividade] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    remuneracao: List["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.Remuneracao"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        }
                    )
                    infoVinc: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoTerm: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoTerm"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class Remuneracao:
                        """
                        :ivar dtRemun: Data a partir da qual as
                            informações de remuneração e periodicidade
                            de pagamento estão vigentes. Validação: Deve
                            ser igual ou posterior à data de admissão
                            (ou de início) e igual ou anterior à data de
                            desligamento (ou de término), se informada.
                        :ivar vrSalFx: Salário base do trabalhador,
                            correspondente à parte fixa da remuneração
                            em {dtRemun}(./dtRemun). Validação: Se
                            {undSalFixo}(./undSalFixo) for igual a [7],
                            preencher com 0 (zero).
                        :ivar undSalFixo:
                        :ivar dscSalVar: Descrição do salário por tarefa
                            ou variável e como este é calculado. Ex.:
                            Comissões pagas no percentual de 10% sobre
                            as vendas. Validação: Preenchimento
                            obrigatório se {undSalFixo}(./undSalFixo)
                            for igual a [6, 7].
                        """
                        dtRemun: Optional[XmlDate] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        vrSalFx: Optional[Decimal] = field(
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
                        undSalFixo: Optional[TsUndSalFixo] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        dscSalVar: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 999,
                                "pattern": r"[^\s]{1}[\S\s]*",
                            }
                        )

                    @dataclass
                    class InfoVinc:
                        """
                        :ivar tpRegTrab: Tipo de regime trabalhista.
                            Validação: Se
                            {infoContr/codCateg}(../../codCateg) =
                            [104], deve ser preenchido com [1].
                        :ivar tpRegPrev: Tipo de regime previdenciário.
                            Validação: Se
                            {infoContr/codCateg}(../../codCateg) =
                            [104], deve ser preenchido com [1]. Se
                            {infoContr/codCateg}(../../codCateg) = [101,
                            102, 103, 105, 106, 107, 108, 111], não pode
                            ser preenchido com [2].
                        :ivar dtAdm: Preencher com a data de admissão do
                            trabalhador. Validação: Deve ser posterior à
                            data de nascimento do trabalhador.
                        :ivar tmpParc: Preencher com o código relativo
                            ao tipo de contrato em tempo parcial.
                            Informar este campo apenas no caso de
                            empregado submetido a horário de trabalho
                            (Capítulo II do Título II da CLT).
                            Validação: Informação obrigatória e
                            exclusiva se {tpRegTrab}(./tpRegTrab) = [1].
                            O código [1] só é válido se
                            {infoContr/codCateg}(../../codCateg) =
                            [104]. Os códigos [2, 3] não são válidos se
                            {infoContr/codCateg}(../../codCateg) =
                            [104].
                        :ivar duracao: Duração do contrato de trabalho.
                            CONDICAO_GRUPO: O (se
                            {tpRegTrab}(../tpRegTrab) = [1]); N (nos
                            demais casos)
                        :ivar observacoes: Observações do contrato de
                            trabalho. CONDICAO_GRUPO: OC
                        :ivar sucessaoVinc: Grupo de informações da
                            sucessão de vínculo trabalhista/estatutário.
                            CONDICAO_GRUPO: OC
                        :ivar infoDeslig: Informações do desligamento.
                            CONDICAO_GRUPO: O
                        """
                        tpRegTrab: Optional[TsTpRegTrab] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        tpRegPrev: Optional[TsTpRegPrev123] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        dtAdm: Optional[XmlDate] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        tmpParc: Optional[TsTmpParc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            }
                        )
                        duracao: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.Duracao"] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            }
                        )
                        observacoes: List["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.Observacoes"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 99,
                            }
                        )
                        sucessaoVinc: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.SucessaoVinc"] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            }
                        )
                        infoDeslig: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.InfoDeslig"] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )

                        @dataclass
                        class Duracao:
                            """
                            :ivar tpContr:
                            :ivar dtTerm: Data do término do contrato
                                por prazo determinado. Validação: O
                                preenchimento é obrigatório se
                                {duracao/tpContr}(./tpContr) = [2]. Não
                                informar se {duracao/tpContr}(./tpContr)
                                = [1]. Se preenchido, deve ser igual ou
                                posterior à data de admissão (no caso de
                                transferência, igual ou posterior a
                                {sucessaoVinc/dtTransf}(../sucessaoVinc_dtTransf)).
                            :ivar clauAssec: Indicar se o contrato por
                                prazo determinado contém cláusula
                                assecuratória do direito recíproco de
                                rescisão antes da data de seu término.
                                Validação: O preenchimento é obrigatório
                                se {duracao/tpContr}(./tpContr) = [2,
                                3]. Não preencher se
                                {duracao/tpContr}(./tpContr) = [1].
                            :ivar objDet: Indicação do objeto
                                determinante da contratação por prazo
                                determinado (obra, serviço, safra,
                                etc.). Validação: O preenchimento é
                                obrigatório e exclusivo se
                                {duracao/tpContr}(./tpContr) = [3].
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
                        class Observacoes:
                            """
                            :ivar observacao: Observação relacionada ao
                                contrato de trabalho.
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
                            :ivar matricAnt: Matrícula do trabalhador no
                                empregador anterior.
                            :ivar dtTransf: Preencher com a data da
                                transferência do empregado para o
                                empregador declarante. Validação: Deve
                                ser posterior à data de admissão do
                                trabalhador.
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

                        @dataclass
                        class InfoDeslig:
                            """
                            :ivar dtDeslig: Preencher com a data de
                                desligamento do vínculo (último dia
                                trabalhado). Validação: Deve ser igual
                                ou posterior a {dtAdm}(../dtAdm) e não
                                superior à data atual (data do envio do
                                evento) acrescida de 10 dias corridos.
                            :ivar mtvDeslig:
                            :ivar dtProjFimAPI: Data projetada para o
                                término do aviso prévio indenizado.
                                Validação: Se informada, deve ser igual
                                ou posterior a {dtDeslig}(./dtDeslig).
                            """
                            dtDeslig: Optional[XmlDate] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            mtvDeslig: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "pattern": r"\d{2}",
                                }
                            )
                            dtProjFimAPI: Optional[XmlDate] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                }
                            )

                    @dataclass
                    class InfoTerm:
                        """
                        :ivar dtTerm: Data do término. Validação: Deve
                            ser igual ou posterior a
                            {dtInicio}(../../dtInicio) e igual ou
                            anterior à data atual acrescida de 10 (dez)
                            dias.
                        :ivar mtvDesligTSV:
                        """
                        dtTerm: Optional[XmlDate] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        mtvDesligTSV: Optional[InfoTermMtvDesligTsv] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            }
                        )

                @dataclass
                class MudCategAtiv:
                    """
                    :ivar codCateg: Preencher com o código da categoria
                        do trabalhador. Validação: Deve ser um código
                        válido e existente na Tabela 01.
                    :ivar natAtividade: Natureza da atividade.
                        Validação: Não informar se
                        {mudCategAtiv/codCateg}(./codCateg) = [721, 722,
                        771, 901]. Se
                        {mudCategAtiv/codCateg}(./codCateg) = [104], não
                        pode ser preenchido com [2]. Se
                        {mudCategAtiv/codCateg}(./codCateg) = [102], não
                        pode ser preenchido com [1].
                    :ivar dtMudCategAtiv: Data a partir da qual foi
                        reconhecida a nova categoria e/ou a nova
                        natureza da atividade. Validação: Deve ser igual
                        ou posterior à data de admissão (ou de início) e
                        igual ou anterior à data de desligamento, se
                        informada.
                    """
                    codCateg: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{3}",
                        }
                    )
                    natAtividade: Optional[TsNatAtividade] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtMudCategAtiv: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )

                @dataclass
                class UnicContr:
                    """
                    :ivar matUnic: Informar a matrícula incorporada
                        (matrícula cujo vínculo/contrato passou a
                        integrar período de unicidade contratual
                        reconhecido judicialmente). O campo não deve ser
                        informado somente no caso de TSVE cadastrado em
                        versão do leiaute anterior a S-1.0. Validação:
                        Deve corresponder a uma matrícula existente no
                        RET para o respectivo trabalhador e diferente do
                        vínculo/contrato informado em
                        {infoContr}(2500_ideTrab_infoContr).
                    :ivar codCateg: Preencher com o código da categoria
                        do trabalhador (código de categoria cujo
                        contrato passou a integrar período de unicidade
                        contratual reconhecido judicialmente).
                        Validação: Informação obrigatória e exclusiva se
                        o campo {matUnic}(./matUnic) não estiver
                        preenchido. Deve ser igual a um código de
                        categoria de contrato cadastrado no evento
                        S-2300 e diferente do contrato informado em
                        {infoContr}(2500_ideTrab_infoContr).
                    :ivar dtInicio: Data de início de TSVE (data de
                        início cujo contrato passou a integrar período
                        de unicidade contratual reconhecido
                        judicialmente). Validação: Informação
                        obrigatória e exclusiva se o campo
                        {matUnic}(./matUnic) não estiver preenchido.
                        Deve ser igual a uma data de início de contrato
                        cadastrado no evento S-2300 e diferente do
                        contrato informado em
                        {infoContr}(2500_ideTrab_infoContr).
                    """
                    matUnic: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 30,
                            "pattern": r".*[^\s].*",
                        }
                    )
                    codCateg: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{3}",
                        }
                    )
                    dtInicio: Optional[XmlDate] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass
                class IdeEstab:
                    """
                    :ivar tpInsc: Preencher com o código correspondente
                        ao tipo de inscrição do estabelecimento, de
                        acordo com as opções da Tabela 05. No caso de
                        empregador doméstico, informar [3] (CAEPF).
                        Validação: Se
                        {ideEmpregador/tpInsc}(2500_ideEmpregador_tpInsc)
                        = [1], deve ser igual a [1, 4]. Se
                        {ideEmpregador/tpInsc}(2500_ideEmpregador_tpInsc)
                        = [2], deve ser igual a [3, 4].
                    :ivar nrInsc: Informar o número de inscrição do
                        estabelecimento do contribuinte de acordo com o
                        tipo de inscrição indicado no campo acima. No
                        caso de empregador doméstico, informar os 9
                        (nove) primeiros dígitos do CPF do empregador,
                        seguidos de 5 (cinco) dígitos 0 (zero). Por
                        exemplo, se o CPF do empregador doméstico for
                        111111111-99, informar 11111111100000.
                        Validação: A inscrição informada deve ser
                        compatível com {ideEstab/tpInsc}(./tpInsc) e o
                        número deve constar na base da RFB e pertencer a
                        {ideEmpregador/nrInsc}(2500_ideEmpregador_nrInsc).
                        Se o processo for referente a empregado
                        doméstico, a inscrição informada deve ser igual
                        aos 9 (nove) primeiros dígitos do CPF do
                        empregador, seguidos de 5 (cinco) dígitos 0
                        (zero).
                    :ivar infoVlr: Informações dos períodos e valores.
                        DESCRICAO_COMPLETA:Informações dos períodos e
                        valores decorrentes de processo trabalhista e
                        ainda não declarados no eSocial.
                    """
                    tpInsc: Optional[TsTpInsc134] = field(
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
                            "pattern": r"\d{12}|\d{14}",
                        }
                    )
                    infoVlr: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )

                    @dataclass
                    class InfoVlr:
                        """
                        :ivar compIni: Competência inicial a que se
                            refere o processo ou conciliação, no formato
                            AAAA-MM. Validação: Devem ser obedecidas as
                            seguintes regras: a) Se
                            {infoContr/tpContr}(../../tpContr) = [1, 3],
                            deve ser igual ou posterior ao mês/ano da
                            data de admissão; b) Se
                            {infoContr/tpContr}(../../tpContr) = [2, 4,
                            5], deve ser igual ao mês/ano da data de
                            admissão; c) Se
                            {infoContr/tpContr}(../../tpContr) = [6],
                            deve ser igual ou posterior ao mês/ano da
                            data de início do TSVE.
                        :ivar compFim: Competência final a que se refere
                            o processo ou conciliação, no formato AAAA-
                            MM. Validação: Deve ser igual ou posterior a
                            {compIni}(./compIni), igual ou anterior ao
                            mês/ano de
                            {dtSent}(2500_infoProcesso_dadosCompl_infoProcJud_dtSent)
                            ou
                            {dtCCP}(2500_infoProcesso_dadosCompl_infoCCP_dtCCP)
                            e: a) Se {infoContr/tpContr}(../../tpContr)
                            = [1, 2], deve ser igual ou anterior ao
                            mês/ano da data de desligamento, se
                            informada; b) Se
                            {infoContr/tpContr}(../../tpContr) = [3, 4,
                            5], deve ser igual ao mês/ano da data de
                            desligamento, se informada; c) Se
                            {infoContr/tpContr}(../../tpContr) = [6],
                            deve ser igual ou anterior ao mês/ano da
                            data de término do TSVE, se informada.
                        :ivar repercProc:
                        :ivar vrRemun: Valor total das verbas
                            remuneratórias a serem pagas ao trabalhador.
                            Validação: Se {repercProc}(./repercProc) =
                            [1], deve ser maior que 0 (zero). Se
                            {repercProc}(./repercProc) = [2], deve ser
                            igual a 0 (zero).
                        :ivar vrAPI: Valor do aviso prévio indenizado
                            pago ao empregado. Validação: Deve ser maior
                            ou igual a 0 (zero).
                        :ivar vr13API: Valor da projeção do aviso prévio
                            indenizado sobre o 13º salário. Validação:
                            Deve ser maior ou igual a 0 (zero).
                        :ivar vrInden: Valor total das demais verbas
                            indenizatórias a serem pagas ao trabalhador.
                            Validação: Deve ser maior ou igual a 0
                            (zero).
                        :ivar vrBaseIndenFGTS: Valor da base de cálculo
                            para recolhimento da indenização
                            compensatória (multa rescisória) do FGTS,
                            para geração de guia. Preencher este campo
                            somente quando o valor da indenização
                            compensatória (multa rescisória) do FGTS for
                            objeto de transação. Validação: Deve ser
                            maior ou igual a 0 (zero).
                        :ivar pagDiretoResc: A indenização compensatória
                            (multa rescisória) do FGTS transacionada foi
                            paga diretamente ao trabalhador mediante
                            decisão/autorização judicial? Validação:
                            Informação obrigatória e exclusiva se
                            {vrBaseIndenFGTS}(./vrBaseIndenFGTS) estiver
                            preenchido.
                        :ivar idePeriodo: Identificação do período ao
                            qual se referem as bases de cálculo.
                            CHAVE_GRUPO: {perRef} CONDICAO_GRUPO: O (se
                            {repercProc}(../repercProc) = [1]); OC (nos
                            demais casos)
                        """
                        compIni: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "length": 7,
                                "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
                            }
                        )
                        compFim: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "length": 7,
                                "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
                            }
                        )
                        repercProc: Optional[InfoVlrRepercProc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        vrRemun: Optional[Decimal] = field(
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
                        vrAPI: Optional[Decimal] = field(
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
                        vr13API: Optional[Decimal] = field(
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
                        vrInden: Optional[Decimal] = field(
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
                        vrBaseIndenFGTS: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": Decimal("0"),
                                "max_inclusive": Decimal("999999999999.99"),
                                "total_digits": 14,
                                "fraction_digits": 2,
                            }
                        )
                        pagDiretoResc: Optional[TsSimNao] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            }
                        )
                        idePeriodo: List["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 360,
                            }
                        )

                        @dataclass
                        class IdePeriodo:
                            """
                            :ivar perRef: Informar o mês/ano (formato
                                AAAA-MM) de referência das informações.
                                Validação: Deve ser um período
                                compreendido entre {compIni}(../compIni)
                                e {compFim}(../compFim), informado no
                                formato AAAA-MM.
                            :ivar baseCalculo: Bases de cálculo de
                                contribuição previdenciária e FGTS.
                                DESCRICAO_COMPLETA:Bases de cálculo de
                                contribuição previdenciária e FGTS
                                decorrentes de processo trabalhista e
                                ainda não declaradas.
                            :ivar infoFGTS: Informações referentes a
                                bases de cálculo de FGTS para geração de
                                guia. DESCRICAO_COMPLETA:Informações
                                referentes a bases de cálculo de FGTS
                                para geração de guia para competências
                                anteriores ao início do FGTS Digital.
                                Informar apenas bases que ainda não
                                foram recolhidas via SEFIP/Conectividade
                                Social. CONDICAO_GRUPO: OC
                            :ivar baseMudCateg: Bases de cálculo já
                                declaradas em GFIP, no caso de
                                reconhecimento de mudança de código de
                                categoria. DESCRICAO_COMPLETA:Bases de
                                cálculo de contribuição previdenciária
                                já declaradas anteriormente em GFIP ou
                                no evento S-1200 (exclusivamente para
                                remuneração de trabalhador sem cadastro
                                no S-2300), no caso de reconhecimento de
                                mudança de código de categoria.
                                CONDICAO_GRUPO: OC (se
                                {indCateg}(2500_ideTrab_infoContr_indCateg)
                                = [S]); N (nos demais casos)
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
                            baseCalculo: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.BaseCalculo"] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                }
                            )
                            infoFGTS: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.InfoFgts"] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                }
                            )
                            baseMudCateg: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.BaseMudCateg"] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                }
                            )

                            @dataclass
                            class BaseCalculo:
                                """
                                :ivar vrBcCpMensal: Valor da base de
                                    cálculo da contribuição
                                    previdenciária sobre a remuneração
                                    mensal do trabalhador. Validação:
                                    Deve ser maior ou igual a 0 (zero).
                                :ivar vrBcCp13: Valor da base de cálculo
                                    da contribuição previdenciária sobre
                                    a remuneração do trabalhador
                                    referente ao 13º salário. Validação:
                                    Deve ser maior ou igual a 0 (zero).
                                :ivar vrBcFgts: Valor da base de cálculo
                                    do FGTS sobre a remuneração do
                                    trabalhador (sem 13° salário).
                                    Validação: Deve ser maior ou igual a
                                    0 (zero).
                                :ivar vrBcFgts13: Valor da base de
                                    cálculo do FGTS sobre a remuneração
                                    do trabalhador sobre o 13º salário.
                                    Validação: Deve ser maior ou igual a
                                    0 (zero).
                                :ivar infoAgNocivo: Grau de exposição a
                                    agentes nocivos
                                    DESCRICAO_COMPLETA:Grupo referente
                                    ao detalhamento do grau de exposição
                                    do trabalhador aos agentes nocivos
                                    que ensejam a cobrança da
                                    contribuição adicional para
                                    financiamento dos benefícios de
                                    aposentadoria especial.
                                    CONDICAO_GRUPO: O (se o código de
                                    categoria for igual a [1XX, 2XX,
                                    3XX, 731, 734, 738] ou se o código
                                    de categoria for igual a [4XX] com
                                    {categOrig} em S-2300 = [1XX, 2XX,
                                    3XX, 731, 734, 738]); N (nos demais
                                    casos)
                                """
                                vrBcCpMensal: Optional[Decimal] = field(
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
                                vrBcCp13: Optional[Decimal] = field(
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
                                vrBcFgts: Optional[Decimal] = field(
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
                                vrBcFgts13: Optional[Decimal] = field(
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
                                infoAgNocivo: Optional["ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.BaseCalculo.InfoAgNocivo"] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    }
                                )

                                @dataclass
                                class InfoAgNocivo:
                                    grauExp: Optional[TsGrauExp] = field(
                                        default=None,
                                        metadata={
                                            "type": "Element",
                                            "required": True,
                                        }
                                    )

                            @dataclass
                            class InfoFgts:
                                """
                                :ivar vrBcFgtsGuia: Valor da base de
                                    cálculo do FGTS sobre a remuneração
                                    do trabalhador (sem 13° salário).
                                    Validação: Deve ser maior ou igual a
                                    0 (zero).
                                :ivar vrBcFgts13Guia: Valor da base de
                                    cálculo do FGTS sobre a remuneração
                                    do trabalhador sobre o 13º salário.
                                    Validação: Deve ser maior ou igual a
                                    0 (zero).
                                :ivar pagDireto: O FGTS transacionado
                                    referente a {perRef}(../perRef) foi
                                    pago diretamente ao trabalhador
                                    mediante decisão/autorização
                                    judicial?
                                """
                                vrBcFgtsGuia: Optional[Decimal] = field(
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
                                vrBcFgts13Guia: Optional[Decimal] = field(
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
                                pagDireto: Optional[TsSimNao] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                    }
                                )

                            @dataclass
                            class BaseMudCateg:
                                """
                                :ivar codCateg: Preencher com o código
                                    da categoria do trabalhador
                                    declarado no período de referência.
                                    Validação: Deve ser um código válido
                                    e existente na Tabela 01.
                                :ivar vrBcCPrev: Valor da remuneração do
                                    trabalhador a ser considerada para
                                    fins previdenciários declarada em
                                    GFIP ou em S-1200 de trabalhador sem
                                    cadastro no S-2300. Validação: Deve
                                    ser maior que 0 (zero).
                                """
                                codCateg: Optional[str] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "pattern": r"\d{3}",
                                    }
                                )
                                vrBcCPrev: Optional[Decimal] = field(
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
