import subprocess
#import os

command = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#GitHub Login
command.stdin.write('gh auth login\n\n')
command.stdin.write('Y\n\n')
#TODO: Preguntarle al profe :(


#Clone repos
command.stdin.write('cd /Users/brian/Documents')
command.stdin.write('mkdir cloned_repositories')
command.stdin.write('cd cloned_repositories')
command.stdin.write('gh classroom clone student-repos')

#Select Classroom
#TODO: 2024-2 Tecnicas 1 - Grupo 2

#Select Assigment
#TODO: Calculadora Java