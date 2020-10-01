% nmos 1hz

vd = 2.1533e-12;
rx = 1.7325e6;
id = vd/rx/rx;
k = 1.3804e-23;
T = 300;
gm = 66.2151e-6;
gam = id/4/k/T/gm;
printf("nmos gamma %f\n", gam);

% pmos 1hz

vd = 1.1199e-12;
rx = 1.7474e6;
id = vd/rx/rx;
k = 1.3804e-23;
T = 300;
gm = 28.2327e-6;
gam = id/4/k/T/gm;
printf("pmos gamma %f\n", gam);
