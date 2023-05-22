# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
import sys
from os import path
import importlib
import inspect
from enum import EnumMeta
from lxml import etree
from xmldiff import main

# from nfelib.bindings.esocial.v1_1.evt_baixa import ESocial as EsocialBaixa

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path
import pkgutil


for binding in pkgutil.walk_packages(
    ["esociallib/esocial/bindings/v1_1/br/gov/esocial/schema_pkg/evt/"]
):
    importlib.import_module(
        "esociallib.esocial.bindings.v1_1.br.gov.esocial.schema_pkg.evt." + binding.name
    )


def test_in_out():
    path = os.path.join("esociallib", "esocial", "samples", "v1_1")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        tree = etree.parse(input_file)
        ns = tree.getroot().tag.split("}")[0][1:]
        parser = XmlParser()
        obj = parser.from_path(Path(input_file))  # , EsocialBaixa)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        xml = serializer.render(obj=obj, ns_map={None: ns})

        output_file = "tests/output_esocial.xml"
        with open(output_file, "w") as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0
        if len(diff) != 0:
            break
