#define amino acid and their corresponding symbol and residue mass
#write a function to caculacte the total protein
#if amino acids are not in the table, return error
#if amino acids are all in the tale, return the total mass and print it.
#write an example
mass_table={"G": 57.02,  "A": 71.04,  "S": 87.03,  "P": 97.05,
            "V": 99.07,  "T": 101.05, "C": 103.01, "I": 113.08,
            "L": 113.08, "N": 114.04, "D": 115.03, "Q": 128.06,
            "K": 128.09, "E": 129.04, "M": 131.04, "H": 137.06,
            "F": 147.07, "R": 156.10, "Y": 163.06, "W": 186.08} #define amino acid and their corresponding symbol and residue mass
def get_protein_mass(sequence):
    total_mass=0.00
    for amino in sequence:
        if amino in mass_table:
            total_mass +=mass_table[amino] #write a function to caculacte the total protein
        else:
            return 'Error: Amino acid ''' +amino +' is not defined and has no recorded mass' #if amino acids are not in the table, return error
    return total_mass
#example
my_sequence = 'GASQ' #input your sequence here
mass= get_protein_mass(my_sequence)

#how to print
if 'Error' in str(mass):
    print(mass)
else:
    print(f'The total mass of the total protein is {mass} amu')


