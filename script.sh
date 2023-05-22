#! /bin/sh

find esociallib/esocial/schemas/v1_1 | grep evt | xargs -n1 xsdata generate -ss namespaces --package esociallib.esocial.bindings.v1_1
