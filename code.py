import numpy as np

#initialization
theta = 0.785398
beta = -0.5235988

#trigo
a = np.sin(theta)
b = np.cos(theta)
c = np.sin(beta)
d = np.cos(beta)

#Liner Polarization
MLP = np.array([[b**2, b*a],[b*a,a**2]])

#Phase Retarder
MPRQ = np.array([[np.exp(-1j*np.pi/4), 0],[0, 1j*np.exp(-1j*np.pi/4)]]) #Quarter Phase Retarder
MPRH = np.array([[np.exp(-1j*np.pi/2), 0],[0, -np.exp(-1j*np.pi/2)]]) #Half Phase Retarder


#Rotator
MR = np.array([[d, -c],[c, d]])

#Matrix for quarter waveplate-half waveplate-quarter waveplate
MQHQ = MPRQ.dot(MPRH.dot(MPRQ))

#Matrix for 45 Linear Polarize, -30 rotator
MLPR = MR.dot(MLP)

#Output
print("Matrix for quarter-half-quarter: ", MQHQ)
print(" ")
print("Matrix for 45 linear polarizer, -30 rotator: ", MLPR)
