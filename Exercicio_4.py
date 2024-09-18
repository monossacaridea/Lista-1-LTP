# Exercício 4: Dada uma lista de notas de alunos notas = [6.3, 7.5, 9.2, 5.1, 6.8], calcule e exiba a média das notas. Além disso, exiba a quantidade de notas acima da média (6).

notas = [6.3, 7.5, 9.2, 5.1, 6.8]
media = sum(notas) / len(notas)
notas_acima_da_media = sum(1 for nota in notas if nota > media)

print(f"A média das notas é: {media:.2f}")
print(f"A quantidade de notas acima da média é: {notas_acima_da_media}")
