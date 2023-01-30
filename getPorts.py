#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2023  Eduardo Valenzuela

import argparse
import nmap3

parser = argparse.ArgumentParser(description="Muestra información de los puertos usando nmap3")
parser.add_argument("-t", "--target", type=str, help="ip o dominio para analizar", required=True)
parser.add_argument("-p", "--port", type=int, help="Rangos de puertos", required=False)
parser.add_argument("-f", "--format", type=str, help="Obtener un elemento que tenga Match", required=False)

parser = parser.parse_args()

def checkResults(results, text):
    if (results):
        print("Resultados: ", results)
        print("\n")
        for k,v in results.items():
            if(text in v) :
                print(" === Coincidencias === ")
                print("Se encontraron coincidencias con la palabra", text)
                print(v[text])
                return v[text]
            else :
                print("'NO' hay resultados con", text, "!!!")
                return
    else:
        print("error al encontrar resultados con nmap3")
        return

def scanAnalizer(host):
    print("Revisando puertos del Host {}".format(host))
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(host)
    if(results) :
        print("Resultados por default scan top ports", results)
    return

def scanAnalizerPort(host, port, text):
    print("Revisando puertos del Host {}".format(host))
    if not port : print("no ingreso un puerto !!!")
    if not text : print("no ingreso un texto a buscar !!!")
    
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(host, args=str(port))
    checkResults(results, text)

if __name__ == "__main__":
    if parser.target and (parser.port or parser.format):
        scanAnalizerPort(parser.target, parser.port, parser.format)
    elif parser.target and (not parser.port and not parser.format):
        scanAnalizer(parser.target)
    else :
        print("Error en los argumentos incorrectos")
        