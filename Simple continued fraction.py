"""Напишите программу, которая преобразует обыкновенную дробь в последовательность коэффициентов
созданной цепной дроби.

:author: Fyodorova Elena
"""
import fractions

COEFFICIENTS = []   # For result coefficients
FRACTION = fractions.Fraction(input('Enter a fraction: '))  # Input of the main fraction
under_fraction = FRACTION   # Fraction under last line
# Every iteration adds new level in main fraction, but records only coefficients and last fraction
while under_fraction.denominator != 1:
    COEFFICIENTS.append(str(under_fraction.numerator // under_fraction.denominator))
    under_fraction = fractions.Fraction(
        under_fraction.denominator, under_fraction.numerator % under_fraction.denominator)
COEFFICIENTS.append(str(under_fraction.numerator))  # Adds last coefficient
print('Coefficients: ' + ' '.join(COEFFICIENTS))
