#!/bin/python3
import numpy as np
import argparse
import sys

# The task requires us to run 200 jobs and receive a 200x200 matrix
# therefore, we will create a function which receives a single N value in range (1,200)
# and run the computation for all Z values in range (1,200)
# Results will be inserted into a numpy array

def energy(N):
    # Initializing constants based on least square fit (1)
    a_v = 15.8
    a_s = 18.3
    a_c = 0.714
    a_a = 23.2
    a_p = 12
    k_p = -0.5
    e_b = np.zeros(200)                         # init result vector for a specific N
    delta0_mixed = 0                            # init delta(N,Z) value for {N odd and Z even} or {N even and Z odd}
    for Z in range(1, 200):
        a = N+Z                                 # init A
        # delta_NZ = 0                          # init delta(N,Z)
        delta0_even = 12/(np.sqrt(a))           # init delta(N,Z) value for {N even and Z even}
        delta0_odd = (-12)/(np.sqrt(a))         # init delta(N,Z) value for {N odd and Z odd}
        if (N % 2 == 0) and (Z % 2 == 0):       # setting delta(N,Z) value for {N even and Z even}
            delta_nz = delta0_even
        elif (N % 2 == 1) and (Z % 2 == 1):     # setting delta(N,Z) value for {N odd and Z odd}
            delta_nz = delta0_odd
        else:                                   # setting delta(N,Z) value for {N odd and Z even} or {N even and Z odd}
            delta_nz = delta0_mixed
        s1 = a_v*a                                        # Semi-empirical formula minuend
        s2 = a_s*(np.power(a, 2/3))                       # Semi-empirical formula first subtrahend
        s3 = a_c*((np.power(Z, 2))/(np.power(a, 1/3)))    # Semi-empirical formula second subtrahend
        s4 = a_v*((np.power(a-2*Z, 2))/a)                 # Semi-empirical formula third subtrahend
        eb_z = s1 - s2 - s3 - s4 - delta_nz               # Semi-empirical formula computation
        if (eb_z < 0):
            e_b[Z-1] = np.nan
        else:
            e_b[Z-1] = eb_z                                   # inserting result into the result vector
    return e_b


if __name__ == '__main__':
     #parser = argparse.ArgumentParser()
     #parser.add_argument("")
     #args = parser.parse_args()
     # print(args.value)

     N =  int(sys.argv[1])+1
     res = energy(N)
     print(res)
     print(len(res))

     with open('output.txt', 'w') as f:
         for j in res:
             #temp = str(res[j])
             f.write(f"{j}\n")
         f.close()
