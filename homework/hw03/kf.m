% nmos1hz
fn=713.4537e-9;
av=117.3763;
w=1e-6*100;
l=1e-6*100;
cgs=5.5991e-15;
cox=1.5*cgs/w/l;
f=1;
kf=fn/av/av*w*l*cox*cox*f;
printf("nmos kf is %e\n", kf);

% pmos 1hz
fn=1.1552e-6;
av=50.0542;
w=1e-6*100;
l=1e-6*100;
cgs=6.4187e-15;
cox=1.5*cgs/w/l;
f=1;
kf=fn/av/av*w*l*cox*cox*f;
printf("pmos kf is %e\n", kf);

