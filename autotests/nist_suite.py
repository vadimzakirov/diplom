import os
from nist.FrequencyTest import FrequencyTest
from nist.RunTest import RunTest
from nist.Matrix import Matrix
from nist.Spectral import SpectralTest
from nist.TemplateMatching import TemplateMatching
from nist.Universal import Universal
from nist.Complexity import ComplexityTest
from nist.Serial import Serial
from nist.ApproximateEntropy import ApproximateEntropy
from nist.CumulativeSum import CumulativeSums
from nist.RandomExcursions import RandomExcursions

# Open Data File and read the binary data of e

class FullNistTest(object):

    def __init__(self, number, binary_data):
        self.binary_data = binary_data
        self.result_file = f"nist_results/result_{number}"

    def execute(self):
        binary_data = self.binary_data
        with open(self.result_file, "w") as f:
            f.write(f'The statistical test of the Binary Expansion of e \n')
            f.write(f'2.01. Frequency Test:\t\t\t\t\t\t\t\t {FrequencyTest.monobit_test(binary_data[:1000000])} \n')
            f.write(f'2.02. Block Frequency Test:\t\t\t\t\t\t\t {FrequencyTest.block_frequency(binary_data[:1000000])} \n')
            f.write(f'2.03. Run Test:\t\t\t\t\t\t\t\t\t\t {RunTest.run_test(binary_data[:1000000])} \n')
            f.write(f'2.04. Run Test (Longest Run of Ones): \t\t\t\t {RunTest.longest_one_block_test(binary_data[:1000000])} \n')
            f.write(f'2.05. Binary Matrix Rank Test:\t\t\t\t\t\t {Matrix.binary_matrix_rank_text(binary_data[:1000000])} \n')
            f.write(f'2.06. Discrete Fourier Transform (Spectral) Test:\t {SpectralTest.sepctral_test(binary_data[:1000000])} \n')
            f.write(f'2.07. Non-overlapping Template Matching Test:\t\t  {TemplateMatching.non_overlapping_test(binary_data[:1000000], "000000001")} \n')
            f.write(f'2.08. Overlapping Template Matching Test: \t\t\t {TemplateMatching.overlapping_patterns(binary_data[:1000000])} \n')
            f.write(f'2.09. Universal Statistical Test:\t\t\t\t\t {Universal.statistical_test(binary_data[:1000000])} \n')
            f.write(f'2.10. Linear Complexity Test:\t\t\t\t\t\t {ComplexityTest.linear_complexity_test(binary_data[:1000000])} \n')
            f.write(f'2.11. Serial Test:\t\t\t\t\t\t\t\t\t {Serial.serial_test(binary_data[:1000000])} \n')
            f.write(f'2.12. Approximate Entropy Test:\t\t\t\t\t\t  {ApproximateEntropy.approximate_entropy_test(binary_data[:1000000])} \n')
            f.write(f'2.13. Cumulative Sums (Forward):\t\t\t\t\t {CumulativeSums.cumulative_sums_test(binary_data[:1000000], 0)} \n')
            f.write(f'2.13. Cumulative Sums (Backward):\t\t\t\t\t {CumulativeSums.cumulative_sums_test(binary_data[:1000000], 1)} \n')
            result = RandomExcursions.random_excursions_test(binary_data[:1000000])
            f.write('2.14. Random Excursion Test: \n')
            f.write('\t\t STATE \t\t\t xObs \t\t\t\t P-Value \t\t\t Conclusion \n')

            for item in result:
                f.write(f'\t\t {repr(item[0]).rjust(4)} \t\t {item[2]} \t\t {repr(item[3]).ljust(14)} \t\t {(item[4] >= 0.01)} \n')

            result = RandomExcursions.variant_test(binary_data[:1000000])

            f.write('2.15. Random Excursion Variant Test:\t\t\t\t\t\t \n')
            f.write('\t\t STATE \t\t COUNTS \t\t\t P-Value \t\t Conclusion \n')
            for item in result:
                f.write(f'\t\t {repr(item[0]).rjust(4)} \t\t {item[2]} \t\t {repr(item[3]).ljust(14)} \t\t {(item[4] >= 0.01)} \n' )
            f.close()
