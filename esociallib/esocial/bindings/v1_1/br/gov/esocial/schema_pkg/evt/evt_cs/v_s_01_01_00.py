from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from esociallib.esocial.bindings.v1_1.org.w3.pkg_2000.pkg_09.xmldsig import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00"


class TsAliqRat(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


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


class TsIndComerc(Enum):
    """
    :cvar VALUE_2: Comercialização da produção efetuada diretamente no
        varejo a consumidor final ou a outro produtor rural pessoa
        física por produtor rural pessoa física, inclusive por segurado
        especial, ou por pessoa física não produtor rural
    :cvar VALUE_3: Comercialização da produção por prod. rural PF/seg.
        especial - Vendas a PJ (exceto entidade inscrita no Programa de
        Aquisição de Alimentos - PAA) ou a intermediário PF
    :cvar VALUE_7: Comercialização da produção isenta de acordo com a
        Lei 13.606/2018 efetuada diretamente no varejo a consumidor
        final ou a outro produtor rural pessoa física por produtor rural
        pessoa física, inclusive por segurado especial, ou por pessoa
        física não produtor rural
    :cvar VALUE_8: Comercialização da produção da pessoa física/segurado
        especial para entidade inscrita no PAA
    :cvar VALUE_9: Comercialização da produção no mercado externo
    """
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class TsIndConstr(Enum):
    """
    :cvar VALUE_0: Não é construtora
    :cvar VALUE_1: Empresa construtora
    """
    VALUE_0 = 0
    VALUE_1 = 1


class TsIndCoop(Enum):
    """
    :cvar VALUE_0: Não é cooperativa
    :cvar VALUE_1: Cooperativa de trabalho
    :cvar VALUE_2: Cooperativa de produção
    :cvar VALUE_3: Outras cooperativas
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


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


class TsIndSubstPatr(Enum):
    """
    :cvar VALUE_1: Integralmente substituída
    :cvar VALUE_2: Parcialmente substituída
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsIndSubstPatrObra(Enum):
    """
    :cvar VALUE_1: Contribuição patronal substituída
    :cvar VALUE_2: Contribuição patronal não substituída
    """
    VALUE_1 = 1
    VALUE_2 = 2


class TsPercTransf(Enum):
    """
    :cvar VALUE_1: 0,2000
    :cvar VALUE_2: 0,4000
    :cvar VALUE_3: 0,6000
    :cvar VALUE_4: 0,8000
    :cvar VALUE_5: 1,0000
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        }
    )
    emailPrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    nmCid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    paisNascto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    paisNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{4}",
        }
    )


class BasesAquisIndAquis(Enum):
    """Indicativo da aquisição.

    Origem: campo {indAquis} de S-1250.

    :cvar VALUE_1: Aquisição da produção de produtor rural pessoa física
        ou segurado especial em geral
    :cvar VALUE_2: Aquisição da produção de produtor rural pessoa física
        ou segurado especial em geral por entidade do PAA
    :cvar VALUE_3: Aquisição da produção de produtor rural pessoa
        jurídica por entidade do PAA
    :cvar VALUE_4: Aquisição da produção de produtor rural pessoa física
        ou segurado especial em geral - Produção isenta (Lei
        13.606/2018)
    :cvar VALUE_5: Aquisição da produção de produtor rural pessoa física
        ou segurado especial em geral por entidade do PAA - Produção
        isenta (Lei 13.606/2018)
    :cvar VALUE_6: Aquisição da produção de produtor rural pessoa
        jurídica por entidade do PAA - Produção isenta (Lei 13.606/2018)
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class BasesRemunIndIncid(Enum):
    """Preencher com o código correspondente ao tipo de incidência para fins de apuração da contribuição previdenciária.
    Validação: a) Para empresas com {classTrib}(5011_infoCS_infoContrib_classTrib) = [01, 70, 80], todas as bases de cálculo devem ser totalizadas com {indIncid}(./indIncid) = [9], EXCETO para {classTrib}(5011_infoCS_infoContrib_classTrib) = [01] E {ideEstab/tpInsc}(5011_infoCS_ideEstab) = [4], que deve ser totalizada com {indIncid}(./indIncid) = [1].
    b) Para empresas com {classTrib}(5011_infoCS_infoContrib_classTrib) = [03], considerar a informação prestada no campo {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) do evento S-5001, conforme abaixo:
    - Se o {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) em S-5001 = [1] (contrib. subst. integralmente), a base de cálculo do respectivo trabalhador deve ser totalizada com {indIncid}(./indIncid) = [9];
    - Se o {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) em S-5001 = [2] (contrib. não substituída), a base de cálculo do respectivo trabalhador deve ser totalizada com {indIncid}(./indIncid) = [1] (normal);
    - Se o {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) em S-5001 = [3] (ativ. concomitante), a base de cálculo do respectivo trabalhador deve ser totalizada com {indIncid}(./indIncid) = [2].
    c) Para empresas com {classTrib}(5011_infoCS_infoContrib_classTrib) = [10] (sindicato de avulsos não portuários), as bases de cálculo dos trabalhadores avulsos da categoria [202] devem ser totalizadas com {indIncid}(./indIncid) = [9].
    d) Para {classTrib}(5011_infoCS_infoContrib_classTrib) = [22] (segurado especial), as bases de cálculo dos trabalhadores devem ser totalizadas com {indIncid}(./indIncid) = [9], EXCETO para a categoria [104] (empregado doméstico), que deve ser totalizada com {indIncid}(./indIncid) = [1].
    e) Para contribuinte com {classTrib}(5011_infoCS_infoContrib_classTrib) = [99] e com {indCoop}(5011_infoCS_infoContrib_infoPJ_indCoop) = [1] (cooperativa de trabalho), as remunerações dos cooperados (categoria [731, 734]) cuja lotação esteja classificada com {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020 = [05, 06, 07] devem ser totalizadas com {indIncid}(./indIncid) = [9]. Nos demais casos, {indIncid}(./indIncid) = [1].
    f) Para contribuintes com {classTrib}(5011_infoCS_infoContrib_classTrib) = [11], as bases de cálculo dos trabalhadores devem ser totalizadas com {indIncid}(./indIncid) = [9], EXCETO para as categorias de contribuinte individual, que devem ser totalizadas com {indIncid}(./indIncid) = [1].
    g) Para {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020 = [91], todas as bases de cálculo devem ser totalizadas com {indIncid}(./indIncid) = [9].

    :cvar VALUE_1: Normal
    :cvar VALUE_2: Atividade concomitante
    :cvar VALUE_9: Substituída ou isenta
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_9 = 9


class InfoCsIndExistInfo(Enum):
    """
    Indicativo de existência de valores de bases e de contribuições sociais.

    :cvar VALUE_1: Há informações com apuração de contribuições sociais
    :cvar VALUE_2: Há movimento, porém sem apuração de contribuições
        sociais
    :cvar VALUE_3: Não há movimento no período informado em
        {perApur}(5011_ideEvento_perApur)
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoPjIndTribFolhaPisCofins(Enum):
    """Indicador de tributação sobre a folha de pagamento - PIS e COFINS.
    Evento de origem: S-1000.

    :cvar S: Sim
    """
    S = "S"


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}",
        }
    )
    codMunic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{7}",
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    tmpParc: Optional[TsTmpParc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    horNoturno: Optional[TsSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    dscJorn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiTodos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nivEstagio: Optional[TInfoEstagiarioNivEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    areaAtuacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrApol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtPrevTerm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    instEnsino: Optional["TInfoEstagiario.InstEnsino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    ageIntegracao: Optional["TInfoEstagiario.AgeIntegracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    supervisorEstagio: Optional["TInfoEstagiario.SupervisorEstagio"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "pattern": r"\d{14}",
            }
        )
        nmRazao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        dscLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        nrLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            }
        )
        bairro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            }
        )
        cep: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "pattern": r"\d{8}",
            }
        )
        codMunic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "pattern": r"\d{7}",
            }
        )
        uf: Optional[TsUf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    remunOutrEmpr: List["TInfoMv.RemunOutrEmpr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        }
    )
    descRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
        }
    )
    ideAdv: List["TInfoRra.IdeAdv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )
    codSusp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    dscSalVar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtAdm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class ESocial:
    """S-5011 - Informações das Contribuições Sociais Consolidadas por Contribuinte

    :ivar evtCS: Evento Informações das Contribuições Sociais
        Consolidadas por Contribuinte. CHAVE_GRUPO: {Id}
    :ivar signature:
    """
    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_01_00"

    evtCS: Optional["ESocial.EvtCs"] = field(
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
    class EvtCs:
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoCS: Informações relativas às contribuições sociais
            DESCRICAO_COMPLETA:Informações relativas às contribuições
            sociais devidas à Previdência Social e a Outras Entidades e
            Fundos.
        :ivar Id:
        """
        ideEvento: Optional[TIdeEventoRetornoContrib] = field(
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
        infoCS: Optional["ESocial.EvtCs.InfoCs"] = field(
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
        class InfoCs:
            """
            :ivar nrRecArqBase:
            :ivar indExistInfo:
            :ivar infoCPSeg: Informações de contribuição previdenciária
                do segurado. CONDICAO_GRUPO: OC
            :ivar infoContrib: Informações gerais do contribuinte
                DESCRICAO_COMPLETA:Informações gerais do contribuinte
                necessárias à apuração das contribuições sociais.
            :ivar ideEstab: Identificação do estabelecimento/obra
                DESCRICAO_COMPLETA:Informações de identificação do
                estabelecimento ou obra de construção civil.
                CHAVE_GRUPO: {tpInsc}, {nrInsc} CONDICAO_GRUPO: OC
            :ivar infoCRContrib: Totalizador dos Códigos de Receita do
                contribuinte DESCRICAO_COMPLETA:Informações consolidadas
                das contribuições sociais devidas à Previdência Social e
                Outras Entidades e Fundos, por Código de Receita - CR.
                CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
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
            indExistInfo: Optional[InfoCsIndExistInfo] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            infoCPSeg: Optional["ESocial.EvtCs.InfoCs.InfoCpseg"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            infoContrib: Optional["ESocial.EvtCs.InfoCs.InfoContrib"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            ideEstab: List["ESocial.EvtCs.InfoCs.IdeEstab"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                }
            )
            infoCRContrib: List["ESocial.EvtCs.InfoCs.InfoCrcontrib"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                }
            )

            @dataclass
            class InfoCpseg:
                """
                :ivar vrDescCP: Valor total da contribuição descontada
                    dos segurados. Origem: campo
                    {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                    de S-5001, quando
                    {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                    em S-5001 = [21].
                :ivar vrCpSeg: Valor total calculado relativo à
                    contribuição dos segurados. Origem: campo
                    {vrCpSeg}(5001_infoCpCalc_vrCpSeg) de S-5001.
                """
                vrDescCP: Optional[Decimal] = field(
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

            @dataclass
            class InfoContrib:
                """
                :ivar classTrib:
                :ivar infoPJ: Informações exclusivas da PJ
                    DESCRICAO_COMPLETA:Informações complementares,
                    exclusivas da Pessoa Jurídica. CONDICAO_GRUPO: O (se
                    {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc) =
                    [1]); N (nos demais casos)
                """
                classTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"\d{2}",
                    }
                )
                infoPJ: Optional["ESocial.EvtCs.InfoCs.InfoContrib.InfoPj"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass
                class InfoPj:
                    """
                    :ivar indCoop: Indicativo de cooperativa. Evento de
                        origem: S-1000.
                    :ivar indConstr: Indicativo de construtora. Evento
                        de origem: S-1000.
                    :ivar indSubstPatr: Indicativo de substituição da
                        contribuição previdenciária patronal. Origem:
                        campo
                        {indSubstPatr}(1280_infoSubstPatr_indSubstPatr)
                        de S-1280.
                    :ivar percRedContrib: Percentual de redução da
                        contribuição prevista na Lei 12.546/2011. Evento
                        de origem: S-1280.
                    :ivar percTransf: Percentual de contribuição social
                        - Lei 11.096/2005. Evento de origem: S-1280.
                    :ivar indTribFolhaPisCofins:
                    :ivar infoAtConc: Informações de atividades
                        concomitantes DESCRICAO_COMPLETA:Informações
                        prestadas por empresa enquadrada no regime de
                        tributação Simples Nacional com tributação
                        previdenciária substituída e não substituída.
                        CONDICAO_GRUPO: O (se
                        {classTrib}(../../classTrib) = [03]; N (nos
                        demais casos)
                    """
                    indCoop: Optional[TsIndCoop] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    indConstr: Optional[TsIndConstr] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    indSubstPatr: Optional[TsIndSubstPatr] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    percRedContrib: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0"),
                            "max_inclusive": Decimal("100"),
                            "total_digits": 5,
                            "fraction_digits": 2,
                        }
                    )
                    percTransf: Optional[TsPercTransf] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    indTribFolhaPisCofins: Optional[InfoPjIndTribFolhaPisCofins] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoAtConc: Optional["ESocial.EvtCs.InfoCs.InfoContrib.InfoPj.InfoAtConc"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class InfoAtConc:
                        """
                        :ivar fatorMes: Informe o fator a ser utilizado
                            para cálculo da contribuição patronal do mês
                            dos trabalhadores envolvidos na execução das
                            atividades enquadradas no Anexo IV em
                            conjunto com as dos Anexos I a III e V da
                            Lei Complementar 123/2006. Evento de origem:
                            S-1280.
                        :ivar fator13: Informe o fator a ser utilizado
                            para cálculo da contribuição patronal do
                            décimo terceiro dos trabalhadores envolvidos
                            na execução das atividades enquadradas no
                            Anexo IV em conjunto com as dos Anexos I a
                            III e V da Lei Complementar 123/2006. Evento
                            de origem: S-1280.
                        """
                        fatorMes: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": Decimal("0"),
                                "max_inclusive": Decimal("100"),
                                "total_digits": 5,
                                "fraction_digits": 2,
                            }
                        )
                        fator13: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": Decimal("0"),
                                "max_inclusive": Decimal("100"),
                                "total_digits": 5,
                                "fraction_digits": 2,
                            }
                        )

            @dataclass
            class IdeEstab:
                """
                :ivar tpInsc:
                :ivar nrInsc: Informar o número de inscrição do
                    contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstab/tpInsc}(./tpInsc).
                    Evento de origem: S-1260, S-1270 ou S-5001.
                :ivar infoEstab: Informações do estabelecimento
                    DESCRICAO_COMPLETA:Informações relativas a cada
                    estabelecimento, necessárias à apuração das
                    contribuições sociais. CONDICAO_GRUPO: N (se
                    {ideEstab/tpInsc}(../tpInsc) = [2] OU (se
                    {ideEstab/tpInsc}(../tpInsc) = [3] e se tratar de
                    empregador doméstico) OU se não existir informação
                    em S-1200, S-1270, S-2299 ou S-2399 relativas ao
                    estabelecimento); O (nos demais casos)
                :ivar ideLotacao: Identificação da lotação tributária.
                    CHAVE_GRUPO: {codLotacao} CONDICAO_GRUPO: O (se
                    existir informação em S-1200, S-1270, S-2299 ou
                    S-2399 relativas ao estabelecimento identificado em
                    {ideEstab/nrInsc}(../nrInsc)); N (nos demais casos)
                :ivar basesAquis: Informações sobre aquisição rural
                    DESCRICAO_COMPLETA:Informações de bases de cálculo
                    relativas à aquisição de produção rural. Evento de
                    origem: S-1250 (existente até a versão 2.5 do
                    leiaute). CHAVE_GRUPO: {indAquis} CONDICAO_GRUPO: O
                    (se existir informação em S-1250 relativa ao
                    estabelecimento identificado em
                    {ideEstab/nrInsc}(../nrInsc) e se não houver
                    informação de
                    {indExcApur1250}(1299_infoFech_indExcApur1250) em
                    S-1299); N (nos demais casos)
                :ivar basesComerc: Informações da comercialização da
                    produção DESCRICAO_COMPLETA:Informações de bases de
                    cálculo relativas à comercialização da produção
                    rural da Pessoa Física. Informações desse grupo
                    conforme informado pelo contribuinte em S-1260.
                    CHAVE_GRUPO: {indComerc} CONDICAO_GRUPO: O (se
                    houver evento S-1260 válido na competência relativo
                    ao estabelecimento identificado em
                    {ideEstab/nrInsc}(../nrInsc)); N (nos demais casos)
                :ivar infoCREstab: Códigos de Receita por
                    estabelecimento DESCRICAO_COMPLETA:Informações das
                    contribuições sociais devidas à Previdência Social e
                    Outras Entidades e Fundos, consolidadas por
                    estabelecimento e por Código de Receita - CR.
                    CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
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
                infoEstab: Optional["ESocial.EvtCs.InfoCs.IdeEstab.InfoEstab"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                ideLotacao: List["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    }
                )
                basesAquis: List["ESocial.EvtCs.InfoCs.IdeEstab.BasesAquis"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 6,
                    }
                )
                basesComerc: List["ESocial.EvtCs.InfoCs.IdeEstab.BasesComerc"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 5,
                    }
                )
                infoCREstab: List["ESocial.EvtCs.InfoCs.IdeEstab.InfoCrestab"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )

                @dataclass
                class InfoEstab:
                    """
                    :ivar cnaePrep: Preencher com o código CNAE,
                        conforme informado em S-1005. Evento de origem:
                        S-1005.
                    :ivar cnpjResp: Preencher com o CNPJ responsável
                        pela inscrição no cadastro de obras da RFB.
                        Evento de origem: S-1005.
                    :ivar aliqRat: Informar a alíquota RAT. Validação:
                        Deve corresponder à alíquota declarada no evento
                        S-1005. Caso não haja informação, retornar a
                        alíquota definida na legislação vigente para o
                        código CNAE informado.
                    :ivar fap: Fator Acidentário de Prevenção - FAP.
                        Validação: Informação obrigatória e exclusiva se
                        {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc)
                        = [1]. Deve corresponder ao FAP estabelecido
                        para a empresa pelo órgão governamental
                        competente, exceto se: a)
                        {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) =
                        [4] e se não existir o campo
                        {cnpjResp}(./cnpjResp); ou b)
                        {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) =
                        [1, 4] e se houver informação de
                        {procAdmJudFap}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap)
                        em S-1005; ou c)
                        {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) =
                        [1, 4] e o estabelecimento ou o CNPJ responsável
                        pela inscrição no CNO não for encontrado na
                        tabela FAP referente ao ano de
                        {perApur}(5011_ideEvento_perApur). Caso haja
                        alguma exceção acima, retornar o FAP declarado
                        no evento S-1005.
                    :ivar aliqRatAjust:
                    :ivar infoEstabRef: Informações de RAT e FAP de
                        referência DESCRICAO_COMPLETA: Informações de
                        RAT e FAP de referência, nos casos de processo
                        administrativo ou judicial que altere a(s)
                        alíquota(s). CONDICAO_GRUPO: OC (se houver
                        informação de
                        {procAdmJudRat}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudRat)
                        em S-1005 ou de
                        {procAdmJudFap}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap)
                        em S-1005); N (nos demais casos)
                    :ivar infoComplObra: Informações complementares
                        relativas a obras DESCRICAO_COMPLETA:Informações
                        complementares relativas a obras de construção
                        civil. CONDICAO_GRUPO: O (se houver informação
                        de
                        {infoObra}(1005_infoEstab_inclusao_dadosEstab_infoObra)
                        em S-1005); N (nos demais casos)
                    """
                    cnaePrep: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{7}",
                        }
                    )
                    cnpjResp: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{14}",
                        }
                    )
                    aliqRat: Optional[TsAliqRat] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    fap: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0.5"),
                            "max_inclusive": Decimal("2"),
                            "total_digits": 5,
                            "fraction_digits": 4,
                        }
                    )
                    aliqRatAjust: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0.5"),
                            "max_inclusive": Decimal("6"),
                            "total_digits": 5,
                            "fraction_digits": 4,
                        }
                    )
                    infoEstabRef: Optional["ESocial.EvtCs.InfoCs.IdeEstab.InfoEstab.InfoEstabRef"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoComplObra: Optional["ESocial.EvtCs.InfoCs.IdeEstab.InfoEstab.InfoComplObra"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class InfoEstabRef:
                        """
                        :ivar aliqRat: Retornar a alíquota RAT definida
                            na legislação vigente. Validação: Deve
                            corresponder à alíquota definida na
                            legislação vigente para o código CNAE
                            informado em S-1005.
                        :ivar fap: Fator Acidentário de Prevenção - FAP
                            estabelecido pelo órgão governamental
                            competente. Validação: Informação
                            obrigatória e exclusiva se
                            {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc)
                            = [1]. Deve corresponder ao FAP estabelecido
                            para a empresa pelo órgão governamental
                            competente.
                        :ivar aliqRatAjust:
                        """
                        aliqRat: Optional[TsAliqRat] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        fap: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": Decimal("0.5"),
                                "max_inclusive": Decimal("2"),
                                "total_digits": 5,
                                "fraction_digits": 4,
                            }
                        )
                        aliqRatAjust: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": Decimal("0.5"),
                                "max_inclusive": Decimal("6"),
                                "total_digits": 5,
                                "fraction_digits": 4,
                            }
                        )

                    @dataclass
                    class InfoComplObra:
                        """
                        :ivar indSubstPatrObra: Indicativo de
                            substituição da contribuição patronal de
                            obra de construção civil. Origem: campo
                            {indSubstPatrObra}(1005_infoEstab_inclusao_dadosEstab_infoObra_indSubstPatrObra)
                            de S-1005.
                        """
                        indSubstPatrObra: Optional[TsIndSubstPatrObra] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )

                @dataclass
                class IdeLotacao:
                    """
                    :ivar codLotacao: Informar o código atribuído pelo
                        empregador para a lotação tributária. Evento de
                        origem: S-1270 ou S-5001.
                    :ivar fpas: Preencher com o código relativo ao FPAS.
                        Evento de origem: S-1020.
                    :ivar codTercs: Preencher com o código de Terceiros,
                        conforme Tabela 04. Evento de origem: S-1020.
                    :ivar codTercsSusp: Informar o código combinado dos
                        Terceiros para os quais o recolhimento está
                        suspenso em virtude de processos judiciais.
                        Evento de origem: S-1020.
                    :ivar infoTercSusp: Informações de suspensão de
                        contribuição a Terceiros
                        DESCRICAO_COMPLETA:Informações de suspensão de
                        contribuições destinadas a Outras Entidades e
                        Fundos (Terceiros). CHAVE_GRUPO: {codTerc}
                        CONDICAO_GRUPO: OC
                    :ivar infoEmprParcial: Informação complementar de
                        obra de construção civil
                        DESCRICAO_COMPLETA:Informação complementar que
                        apresenta identificação do contratante e do
                        proprietário de obra de construção civil
                        contratada sob regime de empreitada parcial ou
                        subempreitada. Evento de origem: S-1020.
                        CONDICAO_GRUPO: O (se
                        {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao)
                        em S-1020 relativo a {codLotacao}(../codLotacao)
                        for igual a [02]); N (nos demais casos)
                    :ivar dadosOpPort: Informações relativas ao operador
                        portuário. CONDICAO_GRUPO: O (se
                        {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao)
                        em S-1020 relativo a {codLotacao}(../codLotacao)
                        for igual a [08]); N (nos demais casos)
                    :ivar basesRemun: Bases de cálculo por categoria
                        DESCRICAO_COMPLETA:Bases de cálculo da
                        contribuição previdenciária incidente sobre
                        remunerações, por categoria. CHAVE_GRUPO:
                        {indIncid}, {codCateg} CONDICAO_GRUPO: O (se
                        houver evento S-1200/S-2299/S-2399 com
                        informações de remuneração válido na competência
                        relativo ao estabelecimento identificado em
                        {ideEstab/nrInsc}(../../nrInsc)); N (nos demais
                        casos)
                    :ivar basesAvNPort: Contratação de avulsos não
                        portuários DESCRICAO_COMPLETA:Informações de
                        bases de cálculo relativas à contratação de
                        trabalhadores avulsos não portuários.
                        Informações desse grupo conforme informado pelo
                        contribuinte em S-1270. CONDICAO_GRUPO: O (se
                        houver evento S-1270 válido na competência
                        relativo ao estabelecimento identificado em
                        {ideEstab/nrInsc}(../../nrInsc)); N (nos demais
                        casos)
                    :ivar infoSubstPatrOpPort: Informação de
                        substituição prevista na Lei 12.546/2011
                        DESCRICAO_COMPLETA:Grupo preenchido
                        exclusivamente pelo Órgão Gestor de Mão de Obra
                        - OGMO
                        ({classTrib}(5011_infoCS_infoContrib_classTrib)
                        = [09]), relativamente a operador portuário
                        enquadrado nos arts. 7º a 9º da Lei 12.546/2011.
                        CONDICAO_GRUPO: OC (se
                        {classTrib}(5011_infoCS_infoContrib_classTrib) =
                        [09]; N (nos demais casos)
                    """
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
                    fpas: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{3}",
                        }
                    )
                    codTercs: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "pattern": r"\d{4}",
                        }
                    )
                    codTercsSusp: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{4}",
                        }
                    )
                    infoTercSusp: List["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.InfoTercSusp"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 15,
                        }
                    )
                    infoEmprParcial: Optional["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.InfoEmprParcial"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    dadosOpPort: Optional["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.DadosOpPort"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    basesRemun: List["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesRemun"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        }
                    )
                    basesAvNPort: Optional["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesAvNport"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoSubstPatrOpPort: Optional["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.InfoSubstPatrOpPort"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class InfoTercSusp:
                        """
                        :ivar codTerc: Informar o código de Terceiro.
                            Origem: campo
                            {codTerc}(1020_infoLotacao_inclusao_dadosLotacao_fpasLotacao_infoProcJudTerceiros_procJudTerceiro_codTerc)
                            de S-1020.
                        """
                        codTerc: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "pattern": r"\d{4}",
                            }
                        )

                    @dataclass
                    class InfoEmprParcial:
                        """
                        :ivar tpInscContrat: Tipo de inscrição do
                            contratante.
                        :ivar nrInscContrat: Número de inscrição
                            (CNPJ/CPF) do contratante.
                        :ivar tpInscProp: Tipo de inscrição do
                            proprietário do CNO. Validação: Retornar o
                            tipo de inscrição do proprietário no CNO.
                            Caso não tenha sido encontrado, retornar
                            {tpInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_tpInscProp)
                            de S-1020. Se o tipo de inscrição do
                            proprietário no CNO não for encontrado e se
                            não houver informação de
                            {tpInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_tpInscProp)
                            em S-1020, retornar
                            {tpInscContrat}(5011_infoCS_ideEstab_ideLotacao_infoEmprParcial_tpInscContrat).
                        :ivar nrInscProp: Preencher com o número de
                            inscrição (CNPJ/CPF) do proprietário do CNO.
                            Validação: Retornar o número de inscrição do
                            proprietário no CNO. Caso não tenha sido
                            encontrado, retornar
                            {nrInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_nrInscProp)
                            de S-1020. Se o número de inscrição do
                            proprietário no CNO não for encontrado e se
                            não houver informação de
                            {nrInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_nrInscProp)
                            em S-1020, retornar
                            {nrInscContrat}(5011_infoCS_ideEstab_ideLotacao_infoEmprParcial_nrInscContrat).
                        :ivar cnoObra:
                        """
                        tpInscContrat: Optional[TsTpInsc12] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        nrInscContrat: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "pattern": r"\d{11}|\d{14}",
                            }
                        )
                        tpInscProp: Optional[TsTpInsc12] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        nrInscProp: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "pattern": r"\d{11}|\d{14}",
                            }
                        )
                        cnoObra: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "pattern": r"\d{12}",
                            }
                        )

                    @dataclass
                    class DadosOpPort:
                        """
                        :ivar cnpjOpPortuario: Preencher com o CNPJ do
                            operador portuário. Origem: campo
                            {dadosLotacao/nrInsc}(1020_infoLotacao_inclusao_dadosLotacao_nrInsc)
                            de S-1020.
                        :ivar aliqRat: Informar a alíquota RAT. Origem:
                            campo
                            {dadosOpPort/aliqRat}(1020_infoLotacao_inclusao_dadosLotacao_dadosOpPort_aliqRat)
                            de S-1020.
                        :ivar fap: Fator Acidentário de Prevenção - FAP.
                            Origem: campo
                            {dadosOpPort/fap}(1020_infoLotacao_inclusao_dadosLotacao_dadosOpPort_fap)
                            de S-1020.
                        :ivar aliqRatAjust:
                        """
                        cnpjOpPortuario: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "pattern": r"\d{14}",
                            }
                        )
                        aliqRat: Optional[TsAliqRat] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        fap: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": Decimal("0.5"),
                                "max_inclusive": Decimal("2"),
                                "total_digits": 5,
                                "fraction_digits": 4,
                            }
                        )
                        aliqRatAjust: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": Decimal("0.5"),
                                "max_inclusive": Decimal("6"),
                                "total_digits": 5,
                                "fraction_digits": 4,
                            }
                        )

                    @dataclass
                    class BasesRemun:
                        """
                        :ivar indIncid:
                        :ivar codCateg: Preencher com o código da
                            categoria do trabalhador, conforme definido
                            em S-5001.
                        :ivar basesCp: Bases, contribuições do segurado
                            e deduções da CP DESCRICAO_COMPLETA:Valores
                            correspondentes às bases, contribuições do
                            segurado e deduções da contribuição
                            previdenciária.
                        """
                        indIncid: Optional[BasesRemunIndIncid] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
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
                        basesCp: Optional["ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesRemun.BasesCp"] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )

                        @dataclass
                        class BasesCp:
                            """
                            :ivar vrBcCp00: Preencher com a base de
                                cálculo da contribuição previdenciária
                                sobre a remuneração. Origem: para
                                {codCateg}(../codCateg) diferente de
                                [104]: somatório do campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [11, 15]; para
                                {codCateg}(../codCateg) = [104]:
                                somatório do campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [11, 15], limitado ao teto
                                do salário de contribuição. OBS.: A
                                contribuição previdenciária patronal do
                                empregador doméstico tem como base de
                                cálculo o somatório do salário de
                                contribuição de cada empregado.
                            :ivar vrBcCp15: Preencher com a base de
                                cálculo da contribuição adicional para o
                                financiamento dos benefícios de
                                aposentadoria especial após 15 anos de
                                contribuição. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, se
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [12, 16].
                            :ivar vrBcCp20: Preencher com a base de
                                cálculo da contribuição adicional para o
                                financiamento dos benefícios de
                                aposentadoria especial após 20 anos de
                                contribuição. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [13, 17].
                            :ivar vrBcCp25: Preencher com a base de
                                cálculo da contribuição adicional para o
                                financiamento dos benefícios de
                                aposentadoria especial após 25 anos de
                                contribuição. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [14, 18].
                            :ivar vrSuspBcCp00: Valor da BC com
                                incidência suspensa em decorrência de
                                decisão judicial. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [91, 95].
                            :ivar vrSuspBcCp15: Valor da base de cálculo
                                da contribuição previdenciária adicional
                                correspondente a exposição a agente
                                nocivo que dá ao trabalhador direito a
                                aposentadoria especial aos 15 anos de
                                trabalho, com incidência suspensa em
                                decorrência de decisão judicial. Origem:
                                campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [92, 96].
                            :ivar vrSuspBcCp20: Valor da base de cálculo
                                da contribuição previdenciária adicional
                                correspondente a exposição a agente
                                nocivo que dá ao trabalhador expectativa
                                de aposentadoria especial aos 20 anos de
                                trabalho, com incidência suspensa em
                                decorrência de decisão judicial. Origem:
                                campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [93, 97].
                            :ivar vrSuspBcCp25: Valor da base de cálculo
                                da contribuição previdenciária adicional
                                correspondente a exposição a agente
                                nocivo que dá ao trabalhador direito a
                                aposentadoria especial aos 25 anos de
                                trabalho, com incidência suspensa em
                                decorrência de decisão judicial. Origem:
                                campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [94, 98].
                            :ivar vrBcCp00VA: Preencher com a base de
                                cálculo da contribuição previdenciária
                                sobre a remuneração - Contrato Verde e
                                Amarelo. Origem: somatório do campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [41, 45].
                            :ivar vrBcCp15VA: Preencher com a base de
                                cálculo da contribuição adicional para o
                                financiamento dos benefícios de
                                aposentadoria especial após 15 anos de
                                contribuição - Contrato Verde e Amarelo.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, se
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [42, 46].
                            :ivar vrBcCp20VA: Preencher com a base de
                                cálculo da contribuição adicional para o
                                financiamento dos benefícios de
                                aposentadoria especial após 20 anos de
                                contribuição - Contrato Verde e Amarelo.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [43, 47].
                            :ivar vrBcCp25VA: Preencher com a base de
                                cálculo da contribuição adicional para o
                                financiamento dos benefícios de
                                aposentadoria especial após 25 anos de
                                contribuição - Contrato Verde e Amarelo.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [44, 48].
                            :ivar vrSuspBcCp00VA: Valor da BC com
                                incidência suspensa em decorrência de
                                decisão judicial - Contrato Verde e
                                Amarelo. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [81, 85].
                            :ivar vrSuspBcCp15VA: Valor da base de
                                cálculo da contribuição previdenciária
                                adicional correspondente a exposição a
                                agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 15
                                anos de trabalho, com incidência
                                suspensa em decorrência de decisão
                                judicial - Contrato Verde e Amarelo.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [82, 86].
                            :ivar vrSuspBcCp20VA: Valor da base de
                                cálculo da contribuição previdenciária
                                adicional correspondente a exposição a
                                agente nocivo que dá ao trabalhador
                                expectativa de aposentadoria especial
                                aos 20 anos de trabalho, com incidência
                                suspensa em decorrência de decisão
                                judicial - Contrato Verde e Amarelo.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [83, 87].
                            :ivar vrSuspBcCp25VA: Valor da base de
                                cálculo da contribuição previdenciária
                                adicional correspondente a exposição a
                                agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 25
                                anos de trabalho, com incidência
                                suspensa em decorrência de decisão
                                judicial - Contrato Verde e Amarelo.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [84, 88].
                            :ivar vrDescSest: Valor total descontado do
                                trabalhador para recolhimento ao SEST.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [22].
                            :ivar vrCalcSest: Valor calculado relativo à
                                contribuição devida pelo trabalhador
                                para recolhimento ao SEST. Origem: campo
                                {vrCsSegTerc}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_vrCsSegTerc)
                                de S-5001, quando
                                {calcTerc/tpCR}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_tpCR)
                                em S-5001 = [121802], exceto se houver
                                informação de processo judicial do
                                trabalhador, quando deve ser utilizado o
                                valor apurado em
                                {vrDescSest}(./vrDescSest).
                            :ivar vrDescSenat: Valor total descontado do
                                trabalhador para recolhimento ao SENAT.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [23].
                            :ivar vrCalcSenat: Valor calculado relativo
                                à contribuição devida pelo trabalhador
                                para recolhimento ao SENAT. Origem:
                                campo
                                {vrCsSegTerc}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_vrCsSegTerc)
                                de S-5001, quando
                                {calcTerc/tpCR}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_tpCR)
                                em S-5001 = [122102], exceto se houver
                                informação de processo judicial do
                                trabalhador, quando deve ser utilizado o
                                valor apurado em
                                {vrDescSenat}(./vrDescSenat).
                            :ivar vrSalFam: Valor total do salário-
                                família para a categoria indicada.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [31].
                            :ivar vrSalMat: Valor total do salário-
                                maternidade para a categoria indicada.
                                Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor)
                                em S-5001 = [32].
                            """
                            vrBcCp00: Optional[Decimal] = field(
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
                            vrBcCp15: Optional[Decimal] = field(
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
                            vrBcCp20: Optional[Decimal] = field(
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
                            vrBcCp25: Optional[Decimal] = field(
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
                            vrSuspBcCp00: Optional[Decimal] = field(
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
                            vrSuspBcCp15: Optional[Decimal] = field(
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
                            vrSuspBcCp20: Optional[Decimal] = field(
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
                            vrSuspBcCp25: Optional[Decimal] = field(
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
                            vrBcCp00VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrBcCp15VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrBcCp20VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrBcCp25VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrSuspBcCp00VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrSuspBcCp15VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrSuspBcCp20VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrSuspBcCp25VA: Optional[Decimal] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": Decimal("0"),
                                    "max_inclusive": Decimal("999999999999.99"),
                                    "total_digits": 14,
                                    "fraction_digits": 2,
                                }
                            )
                            vrDescSest: Optional[Decimal] = field(
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
                            vrCalcSest: Optional[Decimal] = field(
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
                            vrDescSenat: Optional[Decimal] = field(
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
                            vrCalcSenat: Optional[Decimal] = field(
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
                            vrSalFam: Optional[Decimal] = field(
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
                            vrSalMat: Optional[Decimal] = field(
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
                    class BasesAvNport:
                        """
                        :ivar vrBcCp00: Valor da base de cálculo da
                            contribuição previdenciária sobre a
                            remuneração dos trabalhadores avulsos não
                            portuários. Origem: campo
                            {vrBcCp00}(1270_remunAvNP_vrBcCp00) de
                            S-1270.
                        :ivar vrBcCp15: Valor da base de cálculo da
                            contribuição adicional para o financiamento
                            dos benefícios de aposentadoria especial
                            após 15 anos de contribuição. Origem: campo
                            {vrBcCp15}(1270_remunAvNP_vrBcCp15) de
                            S-1270.
                        :ivar vrBcCp20: Valor da base de cálculo da
                            contribuição adicional para o financiamento
                            dos benefícios de aposentadoria especial
                            após 20 anos de contribuição. Origem: campo
                            {vrBcCp20}(1270_remunAvNP_vrBcCp20) de
                            S-1270.
                        :ivar vrBcCp25: Valor da base de cálculo da
                            contribuição adicional para o financiamento
                            dos benefícios de aposentadoria especial
                            após 25 anos de contribuição. Origem: campo
                            {vrBcCp25}(1270_remunAvNP_vrBcCp25) de
                            S-1270.
                        :ivar vrBcCp13: Valor da base de cálculo da
                            contribuição previdenciária sobre o 13°
                            salário dos trabalhadores avulsos não
                            portuários contratados. Origem: campo
                            {vrBcCp13}(1270_remunAvNP_vrBcCp13) de
                            S-1270.
                        :ivar vrDescCP: Preencher com o valor total da
                            contribuição descontada dos trabalhadores
                            avulsos não portuários. Origem: campo
                            {vrDescCP}(1270_remunAvNP_vrDescCP) de
                            S-1270.
                        """
                        vrBcCp00: Optional[Decimal] = field(
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
                        vrBcCp15: Optional[Decimal] = field(
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
                        vrBcCp20: Optional[Decimal] = field(
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
                        vrBcCp25: Optional[Decimal] = field(
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
                        vrDescCP: Optional[Decimal] = field(
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
                    class InfoSubstPatrOpPort:
                        """
                        :ivar cnpjOpPortuario: Preencher com o CNPJ do
                            operador portuário. Origem: campo
                            {dadosLotacao/nrInsc}(1020_infoLotacao_inclusao_dadosLotacao_nrInsc)
                            de S-1020 relativo a
                            {codLotacao}(1280_infoSubstPatrOpPort_codLotacao)
                            em S-1280.
                        """
                        cnpjOpPortuario: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "pattern": r"\d{14}",
                            }
                        )

                @dataclass
                class BasesAquis:
                    """
                    :ivar indAquis:
                    :ivar vlrAquis: Valor total da aquisição de produção
                        rural de produtor rural. Origem: campo
                        {vlrTotAquis} de S-1250.
                    :ivar vrCPDescPR: Preencher com o valor da
                        contribuição previdenciária descontada pelo
                        adquirente de produção de produtor rural - sub-
                        rogação. Origem: somatório do campo {vrCpDescPR}
                        de S-1250.
                    :ivar vrCPNRet: Valor da contribuição previdenciária
                        que deixou de ser retida pelo declarante em
                        decorrência de decisão/sentença judicial.
                    :ivar vrRatNRet: Valor da GILRAT, incidente sobre a
                        aquisição de produção rural de produtor rural,
                        cuja retenção deixou de ser efetuada em
                        decorrência de decisão/sentença judicial.
                    :ivar vrSenarNRet: Valor da contribuição destinada
                        ao SENAR, incidente sobre a aquisição de
                        produção rural de produtor rural pessoa
                        física/segurado especial, que deixou de ser
                        retida em decorrência de decisão/sentença
                        judicial.
                    :ivar vrCPCalcPR: Valor calculado relativo à
                        contribuição previdenciária do produtor rural,
                        de acordo com {indAquis}(./indAquis), conforme
                        segue: a) {indAquis}(./indAquis) = [1, 2]:
                        {vlrAquis}(./vlrAquis) x 1,2%; b)
                        {indAquis}(./indAquis) = [3]:
                        {vlrAquis}(./vlrAquis) x 1,7%; c)
                        {indAquis}(./indAquis) = [4, 5, 6]: 0 (zero).
                    :ivar vrRatDescPR: Valor da contribuição destinada
                        ao financiamento dos benefícios concedidos em
                        razão do grau de incidência da incapacidade
                        laborativa decorrente dos riscos ambientais do
                        trabalho, incidente sobre a aquisição de
                        produção rural de produtor rural.
                    :ivar vrRatCalcPR: Valor calculado relativo à
                        contribuição GILRAT devida pelo produtor rural,
                        de acordo com {indAquis}(./indAquis), conforme
                        segue: a) {indAquis}(./indAquis) = [1, 2, 3]:
                        {vlrAquis}(./vlrAquis) x 0,1%; b)
                        {indAquis}(./indAquis) = [4, 5, 6]: 0 (zero).
                    :ivar vrSenarDesc: Valor da contribuição destinada
                        ao SENAR, incidente sobre a aquisição de
                        produção rural de produtor rural pessoa
                        física/segurado especial. Origem: campo
                        {vrSenarDesc} de S-1250.
                    :ivar vrSenarCalc: Valor calculado da contribuição
                        devida pelo produtor rural ao SENAR, conforme
                        segue: a) {indAquis}(./indAquis) = [1, 2, 4, 5]:
                        {vlrAquis}(./vlrAquis) x 0,2%; b)
                        {indAquis}(./indAquis) = [3, 6]: 0 (zero). OBS.:
                        No período de 04/2020 a 06/2020, a alíquota deve
                        ser 0,1%.
                    """
                    indAquis: Optional[BasesAquisIndAquis] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    vlrAquis: Optional[Decimal] = field(
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
                    vrCPDescPR: Optional[Decimal] = field(
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
                    vrCPNRet: Optional[Decimal] = field(
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
                    vrRatNRet: Optional[Decimal] = field(
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
                    vrSenarNRet: Optional[Decimal] = field(
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
                    vrCPCalcPR: Optional[Decimal] = field(
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
                    vrRatDescPR: Optional[Decimal] = field(
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
                    vrRatCalcPR: Optional[Decimal] = field(
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
                    vrSenarDesc: Optional[Decimal] = field(
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
                    vrSenarCalc: Optional[Decimal] = field(
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
                class BasesComerc:
                    """
                    :ivar indComerc: Indicativo de comercialização.
                        Origem: campo
                        {indComerc}(1260_infoComProd_ideEstabel_tpComerc_indComerc)
                        de S-1260.
                    :ivar vrBcComPR: Valor da base de cálculo da
                        comercialização da produção rural do produtor
                        rural PF/segurado especial a outra PF no varejo
                        ou a outro produtor rural PF/segurado especial
                        ou no mercado externo, conforme
                        {indComerc}(./indComerc). Origem: campo
                        {vrTotCom}(1260_infoComProd_ideEstabel_tpComerc_vrTotCom)
                        de S-1260.
                    :ivar vrCPSusp: Valor da contribuição previdenciária
                        com exigibilidade suspensa. Origem: campo
                        {vrCPSusp}(1260_infoComProd_ideEstabel_tpComerc_infoProcJud_vrCPSusp)
                        de S-1260.
                    :ivar vrRatSusp: Valor da contribuição para GILRAT
                        com exigibilidade suspensa. Origem: campo
                        {vrRatSusp}(1260_infoComProd_ideEstabel_tpComerc_infoProcJud_vrRatSusp)
                        de S-1260.
                    :ivar vrSenarSusp: Valor da contribuição para o
                        SENAR com exigibilidade suspensa. Origem: campo
                        {vrSenarSusp}(1260_infoComProd_ideEstabel_tpComerc_infoProcJud_vrSenarSusp)
                        de S-1260.
                    """
                    indComerc: Optional[TsIndComerc] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    vrBcComPR: Optional[Decimal] = field(
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
                    vrCPSusp: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0"),
                            "max_inclusive": Decimal("999999999999.99"),
                            "total_digits": 14,
                            "fraction_digits": 2,
                        }
                    )
                    vrRatSusp: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0"),
                            "max_inclusive": Decimal("999999999999.99"),
                            "total_digits": 14,
                            "fraction_digits": 2,
                        }
                    )
                    vrSenarSusp: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0"),
                            "max_inclusive": Decimal("999999999999.99"),
                            "total_digits": 14,
                            "fraction_digits": 2,
                        }
                    )

                @dataclass
                class InfoCrestab:
                    """
                    :ivar tpCR:
                    :ivar vrCR: Valor correspondente ao CR apurado.
                        Validação: Deve ser apurado de acordo com a
                        legislação em vigor na competência. Deve ser
                        maior que 0 (zero).
                    :ivar vrSuspCR: Valor suspenso correspondente ao CR
                        apurado. Validação: Deve ser apurado de acordo
                        com as informações de processos judiciais e
                        administrativos.
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
                    vrSuspCR: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0"),
                            "max_inclusive": Decimal("999999999999.99"),
                            "total_digits": 14,
                            "fraction_digits": 2,
                        }
                    )

            @dataclass
            class InfoCrcontrib:
                """
                :ivar tpCR:
                :ivar vrCR: Valor correspondente ao CR apurado.
                    Validação: Deve ser apurado de acordo com a
                    legislação em vigor na competência. Deve ser maior
                    que 0 (zero).
                :ivar vrCRSusp: Valor do tributo com exigibilidade
                    suspensa.
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
                vrCRSusp: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": Decimal("0"),
                        "max_inclusive": Decimal("999999999999.99"),
                        "total_digits": 14,
                        "fraction_digits": 2,
                    }
                )
