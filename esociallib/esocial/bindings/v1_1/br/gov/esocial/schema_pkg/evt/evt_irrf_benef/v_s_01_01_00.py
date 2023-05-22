from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from esociallib.esocial.bindings.v1_1.org.w3.pkg_2000.pkg_09.xmldsig import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00"


class TsCrdia(Enum):
    """Código de Receita - CR relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho pagos a residente no exterior para fins fiscais.

    :cvar VALUE_047301: IRRF - Residentes no exterior, para fins fiscais
    """
    VALUE_047301 = "047301"


class TsCrmen(Enum):
    """Código de Receita - CR relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho.

    :cvar VALUE_056107: IRRF mensal, 13° salário e férias sobre trabalho
        assalariado no país ou ausente no exterior a serviço do país,
        exceto se contratado por empregador doméstico ou por segurado
        especial sujeito a recolhimento unificado
    :cvar VALUE_056108: IRRF mensal e férias - Empregado doméstico
    :cvar VALUE_056109: IRRF 13° salário na rescisão de contrato de
        trabalho - Empregado doméstico
    :cvar VALUE_056110: IRRF - Empregado doméstico 13º salário
    :cvar VALUE_056111: IRRF - Empregado/Trabalhador rural - Segurado
        especial
    :cvar VALUE_056112: IRRF - Empregado/Trabalhador rural - Segurado
        especial 13° salário
    :cvar VALUE_056113: IRRF - Empregado/Trabalhador rural - Segurado
        especial 13° salário rescisório
    :cvar VALUE_058806: IRRF sobre rendimento do trabalho sem vínculo
        empregatício
    :cvar VALUE_061001: IRRF sobre rendimentos relativos a prestação de
        serviços de transporte rodoviário internacional de carga, pagos
        a transportador autônomo PF residente no Paraguai
    :cvar VALUE_353301: Proventos de aposentadoria, reserva, reforma ou
        pensão pagos por previdência pública
    :cvar VALUE_356201: IRRF sobre participação dos trabalhadores em
        lucros ou resultados - PLR
    :cvar VALUE_188901: Rendimentos Recebidos Acumuladamente - RRA
    """
    VALUE_056107 = "056107"
    VALUE_056108 = "056108"
    VALUE_056109 = "056109"
    VALUE_056110 = "056110"
    VALUE_056111 = "056111"
    VALUE_056112 = "056112"
    VALUE_056113 = "056113"
    VALUE_058806 = "058806"
    VALUE_061001 = "061001"
    VALUE_353301 = "353301"
    VALUE_356201 = "356201"
    VALUE_188901 = "188901"


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        }
    )
    emailPrinc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    nmCid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}",
        }
    )
    matricula: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    codCateg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    paisNascto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{3}",
        }
    )
    paisNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{4}",
        }
    )


class DmDevTpPgto(Enum):
    """Informar o evento de origem do pagamento.

    Origem: campo {tpPgto}(1210_ideBenef_infoPgto_tpPgto) de S-1210.

    :cvar VALUE_1: S-1200
    :cvar VALUE_2: S-2299
    :cvar VALUE_3: S-2399
    :cvar VALUE_4: S-1202
    :cvar VALUE_5: S-1207
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class InfoIrTpInfoIr(Enum):
    """
    Consolidação dos tipos de valores relativos ao IRRF.

    :cvar VALUE_11: Rendimentos tributáveis: Remuneração mensal
    :cvar VALUE_12: 13º salário
    :cvar VALUE_14: PLR
    :cvar VALUE_31: Retenções do IRRF efetuadas sobre: Remuneração
        mensal
    :cvar VALUE_32: 13º salário
    :cvar VALUE_34: PLR
    :cvar VALUE_41: Deduções da base de cálculo do IRRF: Previdência
        Social Oficial - PSO - Remuneração mensal
    :cvar VALUE_42: PSO - 13º salário
    :cvar VALUE_46: Previdência complementar - Salário mensal
    :cvar VALUE_47: Previdência complementar - 13º salário
    :cvar VALUE_51: Pensão alimentícia - Remuneração mensal
    :cvar VALUE_52: Pensão alimentícia - 13º salário
    :cvar VALUE_54: Pensão alimentícia - PLR
    :cvar VALUE_61: Fundo de Aposentadoria Programada Individual - FAPI
        - Remuneração mensal
    :cvar VALUE_62: Fundo de Aposentadoria Programada Individual - FAPI
        - 13º salário
    :cvar VALUE_63: Fundação de previdência complementar do servidor
        público - Remuneração mensal
    :cvar VALUE_64: Fundação de previdência complementar do servidor
        público - 13º salário
    :cvar VALUE_67: Plano privado coletivo de assistência à saúde
    :cvar VALUE_70: Rendimento não tributável ou isento do IRRF: Parcela
        isenta 65 anos - Remuneração mensal
    :cvar VALUE_71: Parcela isenta 65 anos - 13º salário
    :cvar VALUE_72: Diárias
    :cvar VALUE_73: Ajuda de custo
    :cvar VALUE_74: Indenização e rescisão de contrato, inclusive a
        título de PDV e acidentes de trabalho
    :cvar VALUE_75: Abono pecuniário
    :cvar VALUE_76: Rendimento de beneficiário com moléstia grave ou
        acidente em serviço - Remuneração mensal
    :cvar VALUE_77: Rendimento de beneficiário com moléstia grave ou
        acidente em serviço - 13º salário
    :cvar VALUE_700: Auxílio moradia
    :cvar VALUE_701: Parte não tributável do valor de serviço de
        transporte de passageiros ou cargas
    :cvar VALUE_79: Outras isenções
    :cvar VALUE_7900: Verba transitada pela folha de pagamento de
        natureza diversa de rendimento ou retenção/isenção/dedução de IR
        (exemplo: desconto de convênio farmácia, desconto de
        consignações, etc.)
    :cvar VALUE_7950: Códigos para compatibilidade de versões
        anteriores: Rendimento não tributável
    :cvar VALUE_7951: Rendimento não tributável em função de acordos
        internacionais de bitributação
    :cvar VALUE_7952: Rendimento tributável - RRA
    :cvar VALUE_7953: Retenção de IR - RRA
    :cvar VALUE_7954: Previdência Social Oficial - RRA
    :cvar VALUE_7955: Pensão alimentícia - RRA
    :cvar VALUE_7956: Valores pagos a titular ou sócio de microempresa
        ou empresa de pequeno porte, exceto pró-labore e aluguéis
    :cvar VALUE_7957: Depósito judicial
    :cvar VALUE_7958: Compensação judicial do ano-calendário
    :cvar VALUE_7959: Compensação judicial de anos anteriores
    :cvar VALUE_7960: Exigibilidade suspensa - Remuneração mensal
    :cvar VALUE_7961: Exigibilidade suspensa - 13º salário
    :cvar VALUE_7962: Exigibilidade suspensa - Férias
    :cvar VALUE_7963: Exigibilidade suspensa - PLR
    :cvar VALUE_7964: Exigibilidade suspensa - RRA
    :cvar VALUE_9011: Exigibilidade suspensa - Rendimento tributável
        (base de cálculo do IR): Remuneração mensal
    :cvar VALUE_9012: 13º salário
    :cvar VALUE_9014: PLR
    :cvar VALUE_9031: Exigibilidade suspensa - Retenção do IRRF efetuada
        sobre: Remuneração mensal
    :cvar VALUE_9032: 13º salário
    :cvar VALUE_9034: PLR
    :cvar VALUE_9831: Depósito judicial - Mensal
    :cvar VALUE_9832: Depósito judicial - 13º salário
    :cvar VALUE_9834: Depósito judicial - PLR
    :cvar VALUE_9041: Exigibilidade suspensa - Dedução da base de
        cálculo do IRRF: Previdência Social Oficial - PSO - Remuneração
        mensal
    :cvar VALUE_9042: PSO - 13º salário
    :cvar VALUE_9046: Previdência complementar - Salário mensal
    :cvar VALUE_9047: Previdência complementar - 13º salário
    :cvar VALUE_9051: Pensão alimentícia - Remuneração mensal
    :cvar VALUE_9052: Pensão alimentícia - 13º salário
    :cvar VALUE_9054: Pensão alimentícia - PLR
    :cvar VALUE_9061: Fundo de Aposentadoria Programada Individual -
        FAPI - Remuneração mensal
    :cvar VALUE_9062: Fundo de Aposentadoria Programada Individual -
        FAPI - 13º salário
    :cvar VALUE_9063: Fundação de previdência complementar do servidor
        público - Remuneração mensal
    :cvar VALUE_9064: Fundação de previdência complementar do servidor
        público - 13º salário
    :cvar VALUE_9067: Plano privado coletivo de assistência à saúde
    :cvar VALUE_9082: Compensação judicial: Compensação judicial do ano-
        calendário
    :cvar VALUE_9083: Compensação judicial de anos anteriores
    """
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_14 = 14
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_34 = 34
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_54 = 54
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_63 = 63
    VALUE_64 = 64
    VALUE_67 = 67
    VALUE_70 = 70
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_74 = 74
    VALUE_75 = 75
    VALUE_76 = 76
    VALUE_77 = 77
    VALUE_700 = 700
    VALUE_701 = 701
    VALUE_79 = 79
    VALUE_7900 = 7900
    VALUE_7950 = 7950
    VALUE_7951 = 7951
    VALUE_7952 = 7952
    VALUE_7953 = 7953
    VALUE_7954 = 7954
    VALUE_7955 = 7955
    VALUE_7956 = 7956
    VALUE_7957 = 7957
    VALUE_7958 = 7958
    VALUE_7959 = 7959
    VALUE_7960 = 7960
    VALUE_7961 = 7961
    VALUE_7962 = 7962
    VALUE_7963 = 7963
    VALUE_7964 = 7964
    VALUE_9011 = 9011
    VALUE_9012 = 9012
    VALUE_9014 = 9014
    VALUE_9031 = 9031
    VALUE_9032 = 9032
    VALUE_9034 = 9034
    VALUE_9831 = 9831
    VALUE_9832 = 9832
    VALUE_9834 = 9834
    VALUE_9041 = 9041
    VALUE_9042 = 9042
    VALUE_9046 = 9046
    VALUE_9047 = 9047
    VALUE_9051 = 9051
    VALUE_9052 = 9052
    VALUE_9054 = 9054
    VALUE_9061 = 9061
    VALUE_9062 = 9062
    VALUE_9063 = 9063
    VALUE_9064 = 9064
    VALUE_9067 = 9067
    VALUE_9082 = 9082
    VALUE_9083 = 9083


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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dscLograd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{8}",
        }
    )
    codMunic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{7}",
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    tmpParc: Optional[TsTmpParc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    horNoturno: Optional[TsSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    dscJorn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiTodos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "length": 7,
            "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indApuracao: Optional[TsIndApuracao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    perApur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiPj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmiSem8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    indGuia: Optional[TsIndGuia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        }
    )
    tpAmb: Optional[TsTpAmb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    procEmi: Optional[TsProcEmi8] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    verProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nivEstagio: Optional[TInfoEstagiarioNivEstagio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    areaAtuacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrApol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtPrevTerm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    instEnsino: Optional["TInfoEstagiario.InstEnsino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    ageIntegracao: Optional["TInfoEstagiario.AgeIntegracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    supervisorEstagio: Optional["TInfoEstagiario.SupervisorEstagio"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "pattern": r"\d{14}",
            }
        )
        nmRazao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        dscLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            }
        )
        nrLograd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            }
        )
        bairro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            }
        )
        cep: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "pattern": r"\d{8}",
            }
        )
        codMunic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "pattern": r"\d{7}",
            }
        )
        uf: Optional[TsUf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    remunOutrEmpr: List["TInfoMv.RemunOutrEmpr"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        }
    )
    descRRA: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
        }
    )
    ideAdv: List["TInfoRra.IdeAdv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "required": True,
            }
        )
        nrInsc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
                "required": True,
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrProcJud: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "length": 20,
        }
    )
    codSusp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    dscSalVar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
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
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )
    nrInsc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    dtAdm: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00",
            "required": True,
        }
    )


@dataclass
class ESocial:
    """S-5002 - Imposto de Renda Retido na Fonte por Trabalhador

    :ivar evtIrrfBenef: Evento IRRF por Trabalhador
        DESCRICAO_COMPLETA:Evento Imposto de Renda Retido na Fonte por
        Trabalhador. CHAVE_GRUPO: {Id}
    :ivar signature:
    """
    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_01_00"

    evtIrrfBenef: Optional["ESocial.EvtIrrfBenef"] = field(
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
    class EvtIrrfBenef:
        """
        :ivar ideEvento: Identificação do evento de retorno.
            CHAVE_GRUPO: {perApur*}
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do beneficiário
            DESCRICAO_COMPLETA:Identificação do beneficiário do
            pagamento. CHAVE_GRUPO: {cpfBenef*}
        :ivar Id:
        """
        ideEvento: Optional["ESocial.EvtIrrfBenef.IdeEvento"] = field(
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
        ideTrabalhador: Optional["ESocial.EvtIrrfBenef.IdeTrabalhador"] = field(
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
                arquivo que deu origem ao presente arquivo de retorno ao
                empregador. Validação: Deve corresponder ao recibo de um
                arquivo com informações de rendimentos sujeitos a
                Imposto de Renda Retido na Fonte - IRRF (S-1210 ou
                S-3000).
            :ivar perApur: Informar o mês/ano (formato AAAA-MM) de
                referência das informações.
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
            perApur: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "length": 7,
                    "pattern": r"([2]\d{3}|19[8-9]\d)-(1[0-2]|0[1-9])",
                }
            )

        @dataclass
        class IdeTrabalhador:
            """
            :ivar cpfBenef: Número de inscrição no Cadastro de Pessoas
                Físicas - CPF do beneficiário do pagamento. Origem:
                campo {cpfBenef}(1210_ideBenef_cpfBenef) de S-1210.
            :ivar dmDev: Informações do demonstrativo de valores
                devidos. CHAVE_GRUPO: {perRef}, {ideDmDev}, {tpPgto}
            """
            cpfBenef: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"\d{11}",
                }
            )
            dmDev: List["ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class DmDev:
                """
                :ivar perRef: Período de referência das informações, no
                    formato AAAA-MM (ou AAAA, se for relativo a 13°
                    salário). Origem: campo
                    {perRef}(1210_ideBenef_infoPgto_perRef) de S-1210.
                :ivar ideDmDev: Identificador atribuído pela fonte
                    pagadora para o demonstrativo de valores devidos ao
                    trabalhador. Origem: campo
                    {ideDmDev}(1210_ideBenef_infoPgto_ideDmDev) de
                    S-1210.
                :ivar tpPgto:
                :ivar dtPgto: Informar a data de pagamento. Origem:
                    campo {dtPgto}(1210_ideBenef_infoPgto_dtPgto) de
                    S-1210.
                :ivar codCateg: Preencher com o código da categoria do
                    trabalhador, conforme Tabela 01. Validação: a) Se
                    {tpPgto}(./tpPgto) = [1, 4], retornar o código de
                    categoria informado no evento de origem; b) Se
                    {tpPgto}(./tpPgto) = [2, 3], retornar o código de
                    categoria existente no Registro de Eventos
                    Trabalhistas - RET; c) Se {tpPgto}(./tpPgto) = [5],
                    retornar [000].
                :ivar infoIR: Rendimentos tributáveis, deduções,
                    isenções e retenções do IRRF.
                :ivar totApurMen: Totalizador de tributos com período de
                    apuração mensal. CHAVE_GRUPO: {CRMen}
                    CONDICAO_GRUPO: OC
                :ivar totApurDia: Totalizador de tributos com período de
                    apuração diário. CHAVE_GRUPO: {perApurDia}, {CRDia}
                    CONDICAO_GRUPO: OC
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
                ideDmDev: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "pattern": r".*[^\s].*",
                    }
                )
                tpPgto: Optional[DmDevTpPgto] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                dtPgto: Optional[XmlDate] = field(
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
                infoIR: List["ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoIr"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 999,
                    }
                )
                totApurMen: List["ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.TotApurMen"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 50,
                    }
                )
                totApurDia: List["ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.TotApurDia"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 350,
                    }
                )

                @dataclass
                class InfoIr:
                    """
                    :ivar tpInfoIR:
                    :ivar valor: Composição do valor do rendimento
                        tributável, não tributável, retenção, dedução ou
                        isenção do IRRF, de acordo com a classificação
                        apresentada no campo {tpInfoIR}(./tpInfoIR).
                        Validação: Deve corresponder ao somatório dos
                        valores informados nas rubricas (campo {vrRubr})
                        dos eventos que deram origem ao S-1210 (grupos
                        {infoPerApur} e {infoPerAnt} do S-1200, S-1202,
                        S-1207 e S-2299, e grupo {verbasResc} do
                        S-2399), desde que o campo {indApurIR} vinculado
                        às respectivas rubricas seja igual a [0] ou não
                        informado, obedecendo ao que segue: a) Somar os
                        valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                        em S-1010 seja igual a [1, 3] e subtrair os
                        valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                        em S-1010 seja igual a [2, 4], observando a
                        tabela de relacionamento abaixo:
                        {tpInfoIR}(./tpInfoIR) = [11],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [11, 13]; {tpInfoIR}(./tpInfoIR) =
                        [12],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [12]; {tpInfoIR}(./tpInfoIR) = [14],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [14]; {tpInfoIR}(./tpInfoIR) = [70],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [70]; {tpInfoIR}(./tpInfoIR) = [71],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [71]; {tpInfoIR}(./tpInfoIR) = [72],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [72]; {tpInfoIR}(./tpInfoIR) = [73],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [73]; {tpInfoIR}(./tpInfoIR) = [74],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [74]; {tpInfoIR}(./tpInfoIR) = [75],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [75]; {tpInfoIR}(./tpInfoIR) = [76],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [76]; {tpInfoIR}(./tpInfoIR) = [77],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [77]; {tpInfoIR}(./tpInfoIR) =
                        [700],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [700]; {tpInfoIR}(./tpInfoIR) =
                        [701],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [701]; {tpInfoIR}(./tpInfoIR) =
                        [79],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [79]; {tpInfoIR}(./tpInfoIR) =
                        [7900],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9]; {tpInfoIR}(./tpInfoIR) =
                        [7950],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [0]; {tpInfoIR}(./tpInfoIR) =
                        [7951],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [1]; {tpInfoIR}(./tpInfoIR) =
                        [7952],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [15]; {tpInfoIR}(./tpInfoIR) =
                        [7956],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [78]; {tpInfoIR}(./tpInfoIR) =
                        [7960],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [91]; {tpInfoIR}(./tpInfoIR) =
                        [7961],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [92]; {tpInfoIR}(./tpInfoIR) =
                        [7962],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [93]; {tpInfoIR}(./tpInfoIR) =
                        [7963],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [94]; {tpInfoIR}(./tpInfoIR) =
                        [7964],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [95]; {tpInfoIR}(./tpInfoIR) =
                        [9011],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9011, 9013]; {tpInfoIR}(./tpInfoIR)
                        = [9012],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9012]; {tpInfoIR}(./tpInfoIR) =
                        [9014],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9014]. b) Somar os valores das
                        rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                        em S-1010 seja igual a [2, 4] e subtrair os
                        valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                        em S-1010 seja igual a [1, 3], observando a
                        tabela de relacionamento abaixo:
                        {tpInfoIR}(./tpInfoIR) = [31],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [31, 33]; {tpInfoIR}(./tpInfoIR) =
                        [32],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [32]; {tpInfoIR}(./tpInfoIR) = [34],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [34]; {tpInfoIR}(./tpInfoIR) = [41],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [41, 43]; {tpInfoIR}(./tpInfoIR) =
                        [42],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [42]; {tpInfoIR}(./tpInfoIR) = [46],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [46, 48]; {tpInfoIR}(./tpInfoIR) =
                        [47],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [47]; {tpInfoIR}(./tpInfoIR) = [51],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [51, 53]; {tpInfoIR}(./tpInfoIR) =
                        [52],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [52]; {tpInfoIR}(./tpInfoIR) = [54],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [54]; {tpInfoIR}(./tpInfoIR) = [61],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [61, 66]; {tpInfoIR}(./tpInfoIR) =
                        [62],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [62]; {tpInfoIR}(./tpInfoIR) = [63],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [63, 65]; {tpInfoIR}(./tpInfoIR) =
                        [64],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [64]; {tpInfoIR}(./tpInfoIR) = [67],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [67]; {tpInfoIR}(./tpInfoIR) =
                        [7953],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [35]; {tpInfoIR}(./tpInfoIR) =
                        [7954],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [44]; {tpInfoIR}(./tpInfoIR) =
                        [7955],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [55]; {tpInfoIR}(./tpInfoIR) =
                        [7957],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [81]; {tpInfoIR}(./tpInfoIR) =
                        [7958],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [82]; {tpInfoIR}(./tpInfoIR) =
                        [7959],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [83]; {tpInfoIR}(./tpInfoIR) =
                        [9031],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9031, 9033]; {tpInfoIR}(./tpInfoIR)
                        = [9032],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9032]; {tpInfoIR}(./tpInfoIR) =
                        [9034],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9034]; {tpInfoIR}(./tpInfoIR) =
                        [9831],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9831, 9833]; {tpInfoIR}(./tpInfoIR)
                        = [9832],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9832]; {tpInfoIR}(./tpInfoIR) =
                        [9834],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9834]; {tpInfoIR}(./tpInfoIR) =
                        [9041],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9041, 9043]; {tpInfoIR}(./tpInfoIR)
                        = [9042],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9042]; {tpInfoIR}(./tpInfoIR) =
                        [9046],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9046, 9048]; {tpInfoIR}(./tpInfoIR)
                        = [9047],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9047]; {tpInfoIR}(./tpInfoIR) =
                        [9051],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9051, 9053]; {tpInfoIR}(./tpInfoIR)
                        = [9052],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9052]; {tpInfoIR}(./tpInfoIR) =
                        [9054],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9054]; {tpInfoIR}(./tpInfoIR) =
                        [9061],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9061, 9066]; {tpInfoIR}(./tpInfoIR)
                        = [9062],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9062]; {tpInfoIR}(./tpInfoIR) =
                        [9063],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9063, 9065]; {tpInfoIR}(./tpInfoIR)
                        = [9064],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9064]; {tpInfoIR}(./tpInfoIR) =
                        [9067],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9067]; {tpInfoIR}(./tpInfoIR) =
                        [9082],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9082]; {tpInfoIR}(./tpInfoIR) =
                        [9083],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9083]. OBS.: Se o campo {indApurIR}
                        vinculado à rubrica for igual a [1], considerar
                        {vrRubr} = [0].
                    """
                    tpInfoIR: Optional[InfoIrTpInfoIr] = field(
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
                            "min_inclusive": Decimal("-999999999999.99"),
                            "max_inclusive": Decimal("999999999999.99"),
                            "total_digits": 14,
                            "fraction_digits": 2,
                        }
                    )

                @dataclass
                class TotApurMen:
                    """
                    :ivar CRMen:
                    :ivar vlrCRMen: Valor relativo ao Imposto de Renda
                        Retido na Fonte sobre rendimentos do trabalho.
                        Validação: Deve ser maior que 0 (zero) e
                        agrupado conforme segue: a) Quando o evento de
                        origem for S-1200, S-1202, S-2299, S-2399 e
                        respectivo S-1210: {CRMen}(./CRMen) = [056107]:
                        se {codCateg}(../codCateg) = [101, 103, 105,
                        106, 107, 108, 111, 201, 202, 301, 302, 303,
                        304, 305, 306, 307, 308, 309, 310, 311, 312,
                        313, 401, 410, 501, 721, 722, 723, 901, 902,
                        903, 904], {indApurIR} = [0], os campos {indRRA}
                        e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 for diferente de [22], efetuar o
                        somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32];
                        {CRMen}(./CRMen) = [056108]: se
                        {codCateg}(../codCateg) = [104], {indApurIR} =
                        [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31];
                        {CRMen}(./CRMen) = [056109]: se
                        {codCateg}(../codCateg) = [104], {indApurIR} =
                        [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], apenas se
                        origem for S-2299; {CRMen}(./CRMen) = [056110]:
                        se {codCateg}(../codCateg) = [104], {indApurIR}
                        = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], exceto se
                        origem for S-2299; {CRMen}(./CRMen) = [056111]:
                        se {codCateg}(../codCateg) = [101, 102, 103,
                        105, 106, 107, 108, 111, 201, 202], {indApurIR}
                        = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 = [22], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31];
                        {CRMen}(./CRMen) = [056112]: se
                        {codCateg}(../codCateg) = [101, 102, 103, 105,
                        106, 107, 108, 111, 201, 202], {indApurIR} =
                        [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 = [22], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], exceto se
                        origem for S-2299/S-2399; {CRMen}(./CRMen) =
                        [056113]: se {codCateg}(../codCateg) = [101,
                        102, 103, 105, 106, 107, 108, 111, 201, 202],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 = [22], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], apenas se
                        origem for S-2299/S-2399; {CRMen}(./CRMen) =
                        [058806]: se {codCateg}(../codCateg) = [701,
                        711, 712, 731, 734, 738, 741, 751, 761, 771,
                        781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34];
                        {CRMen}(./CRMen) = [061001]: se
                        {codCateg}(../codCateg) = [712], {indApurIR} =
                        [0] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        = [586], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31];
                        {CRMen}(./CRMen) = [356201]: se
                        {codCateg}(../codCateg) = [1XX], {indApurIR} =
                        [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [34];
                        {CRMen}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não for informado, {indApurIR} = [0] e {indRRA}
                        = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34].
                        b) Quando o evento de origem for S-1207 e
                        respectivo S-1210: {CRMen}(./CRMen) = [353301]:
                        se {indApurIR} = [0] e os campos
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        e {indRRA} não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34];
                        {CRMen}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não for informado, {indApurIR} = [0] e {indRRA}
                        = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34].
                    :ivar vlrCRMenSusp: Valor que deixou de ser
                        descontado relativo ao Imposto de Renda sobre
                        rendimentos do trabalho em decorrência de
                        processos. Validação: Deve ser maior ou igual a
                        0 (zero) e agrupado conforme segue: a) Quando o
                        evento de origem for S-1200, S-1202, S-2299,
                        S-2399 e respectivo S-1210: {CRMen}(./CRMen) =
                        [056107]: se {codCateg}(../codCateg) = [101,
                        103, 105, 106, 107, 108, 111, 201, 202, 301,
                        302, 303, 304, 305, 306, 307, 308, 309, 310,
                        311, 312, 313, 401, 410, 501, 721, 722, 723,
                        901, 902, 903, 904], {indApurIR} = [0], os
                        campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 for diferente de [22], efetuar o
                        somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9032,
                        9831, 9832]; {CRMen}(./CRMen) = [056108]: se
                        {codCateg}(../codCateg) = [104], {indApurIR} =
                        [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9831];
                        {CRMen}(./CRMen) = [056109]: se
                        {codCateg}(../codCateg) = [104], {indApurIR} =
                        [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9032, 9832],
                        apenas se origem for S-2299; {CRMen}(./CRMen) =
                        [056110]: se {codCateg}(../codCateg) = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9032, 9832],
                        exceto se origem for S-2299; {CRMen}(./CRMen) =
                        [056111]: se {codCateg}(../codCateg) = [101,
                        102, 103, 105, 106, 107, 108, 111, 201, 202],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 = [22], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9831];
                        {CRMen}(./CRMen) = [056112]: se
                        {codCateg}(../codCateg) = [101, 102, 103, 105,
                        106, 107, 108, 111, 201, 202], {indApurIR} =
                        [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 = [22], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9032, 9832],
                        exceto se origem for S-2299/S-2399;
                        {CRMen}(./CRMen) = [056113]: se
                        {codCateg}(../codCateg) = [101, 102, 103, 105,
                        106, 107, 108, 111, 201, 202], {indApurIR} =
                        [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib)
                        em S-1000 = [22], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9032, 9832],
                        apenas se origem for S-2299/S-2399;
                        {CRMen}(./CRMen) = [058806]: se
                        {codCateg}(../codCateg) = [701, 711, 712, 731,
                        734, 738, 741, 751, 761, 771, 781], {indApurIR}
                        = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031,  9032,
                        9034, 9831, 9832, 9834]; {CRMen}(./CRMen) =
                        [061001]: se {codCateg}(../codCateg) = [712],
                        {indApurIR} = [0] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        = [586], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9831];
                        {CRMen}(./CRMen) = [356201]: se
                        {codCateg}(../codCateg) = [1XX], {indApurIR} =
                        [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não forem informados, efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9034, 9834];
                        {CRMen}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não for informado, {indApurIR} = [0] e {indRRA}
                        = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9032,
                        9034, 9831, 9832, 9834]. b) Quando o evento de
                        origem for S-1207 e respectivo S-1210:
                        {CRMen}(./CRMen) = [353301]: se {indApurIR} =
                        [0] e os campos
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        e {indRRA} não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9032,
                        9034, 9831, 9832, 9834]; {CRMen}(./CRMen) =
                        [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        não for informado, {indApurIR} = [0] e {indRRA}
                        = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9032,
                        9034, 9831, 9832, 9834].
                    """
                    CRMen: Optional[TsCrmen] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    vlrCRMen: Optional[Decimal] = field(
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
                    vlrCRMenSusp: Optional[Decimal] = field(
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
                class TotApurDia:
                    """
                    :ivar perApurDia: Período de apuração diário do
                        Código de Receita - CR. Validação: Deve ser
                        igual ao dia ("DD") da data informada em
                        {dtPgto}(../dtPgto).
                    :ivar CRDia:
                    :ivar vlrCRDia: Valor relativo ao Imposto de Renda
                        Retido na Fonte sobre rendimentos do trabalho
                        pagos a residente, para fins fiscais, no
                        exterior. Evento de origem: S-1200, S-1202,
                        S-2299, S-2399 e respectivo S-1210. Validação:
                        Deve ser maior que 0 (zero). Efetuar o somatório
                        de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34],
                        se {indApurIR} = [0] e: a)
                        {codCateg}(../codCateg) for diferente de [712] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        for informado com qualquer valor; ou b)
                        {codCateg}(../codCateg) = [712] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        for informado com valor diferente de [586].
                    :ivar vlrCRDiaSusp: Valor que deixou de ser
                        descontado do trabalhador relativo ao Imposto de
                        Renda sobre rendimentos do trabalho pagos a
                        residente, para fins fiscais, no exterior.
                        Evento de origem: S-1200, S-1202, S-2299, S-2399
                        e respectivo S-1210. Validação: Deve ser maior
                        ou igual a 0 (zero). Efetuar o somatório de
                        {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [9031, 9032,
                        9034, 9831, 9832, 9834], se {indApurIR} = [0] e:
                        a) {codCateg}(../codCateg) for diferente de
                        [712] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        for informado com qualquer valor; ou b)
                        {codCateg}(../codCateg) = [712] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        for informado com valor diferente de [586].
                    """
                    perApurDia: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": "0",
                            "max_inclusive": "31",
                            "pattern": r"\d{1,2}",
                        }
                    )
                    CRDia: Optional[TsCrdia] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    vlrCRDia: Optional[Decimal] = field(
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
                    vlrCRDiaSusp: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0"),
                            "max_inclusive": Decimal("999999999999.99"),
                            "total_digits": 14,
                            "fraction_digits": 2,
                        }
                    )
