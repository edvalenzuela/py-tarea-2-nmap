#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2023  Eduardo Valenzuela

import argparse
import nmap3

parser = argparse.ArgumentParser(description="Muestra información de los puertos usando nmap3")
parser.add_argument("-t", "--target", type=str, default="1.1.1.1", help="ip o dominio para analizar", required=True)
parser.add_argument("-p", "--port", type=int, default=80, help="Rangos de puertos", required=False)
parser.add_argument("-f", "--format", type=str, default="ports", help="Obtener un elemento", required=False)

parser = parser.parse_args()

def scanAnalizer(host):
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(host, args="-sV")
    print(results)

if __name__ == "__main__":
   if parser.target:
       scanAnalizer(parser.target)