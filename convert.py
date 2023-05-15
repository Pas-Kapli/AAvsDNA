#!/usr/bin/python

import sys
import re

table = { 
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
} 

def write_file(filename,content):
  with open(filename, "w") as f:
    for line in content:
      f.write(line+"\n")

def readfile(filename):
  with open(filename) as f:
    content = f.readlines()
  return content

def nuc_to_aa(s):
  """convert string s from nucleotide to amino acid"""
  codon_len = 3

  # convert string to list of triplets (codons)
  codons = [s[i:i+codon_len] for i in range(0, len(s), codon_len)]

  # convert list of codons to a list of amino acids and join them into a string
  return ''.join(list(map(lambda x : table[x], codons)))

def fasta_nt_to_aa(content):
  data = []
  lineno = 0
  for line in content:
    lineno = lineno + 1
    if lineno % 2 == 1:
      data.append(line)
    else:
      data.append(nuc_to_aa(line))

  return data;
    

def fasta_validate(content):
  """Check file is valid FASTA and remove all blank lines"""
  data = []
  original_lineno = 0
  lineno = 0
  for line in content:
    original_lineno = original_lineno+1
    s = line.strip()
    if len(s) > 0:
      lineno = lineno+1
      if lineno % 2 == 1:
        if s[0] != '>':
          print("[FATAL] Expected header on line " + str(original_lineno))
          sys.exit(0)
      else:
        if len(s) % 3 <> 0:
          print("[FATAL] Length of sequence on line " + str(original_lineno) + "not divisible by 3")
          sys.exit(0)
      data.append(s)

  return data
      
def print_aa(filename,data):
  write_file(filename,data)

def print_12(filename,data):
  """remove positions that are multiples of 3 from sequences"""
  data12 = []
  lineno = 0
  for line in data:
    lineno = lineno + 1
    if lineno % 2 == 1:
      data12.append(line)
    else:
      line12 = ''.join([line[i:i+2] for i in range(0,len(line),3)])
      data12.append(line12)
  write_file(filename,data12)
    

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("usage: " + sys.argv[0] + " FILE")
    sys.exit(0)

  content_nt  = fasta_validate(readfile(sys.argv[1]))
  content_aa = fasta_nt_to_aa(content_nt)
  print_aa(sys.argv[1] + ".AA", content_aa)
  print_12(sys.argv[1] + ".12", content_nt)
