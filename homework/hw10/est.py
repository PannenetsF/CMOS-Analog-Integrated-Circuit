import math

kn = 280e-6
kp = 70e-6

L = 0.5e-6

CL = 5e-12

VGST1 = 0.2
VGST2 = 0.2
VGST3 = 0.2
VGST4 = 0.2
VGST7 = 0.2


def est(i, norp):
    if norp == 'n':
        return 2 * i / kn * L / (0.2)**2 * 1e6
    if norp == 'p':
        return 2 * i / kp * L / (0.2)**2 * 1e6

i_in = 100e-6
i_in_b = 2 * i_in

print('i_in_b: W: ', est(i_in_b, 'n'))
print('i_in: W: ', est(i_in, 'n'))

