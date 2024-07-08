import math
fin_veloc = open("finalveloc.txt").readlines()
fin_geom = open("geom").readlines()
pm = open("projectmom.txt","w")

#reading geoms of C,H,D1,D2
cgeom = ((fin_geom)[0])
cgeom_list = cgeom.split()
cg_x = float(cgeom_list[2])
cg_y = float(cgeom_list[3])
cg_z = float(cgeom_list[4])

ogeom = ((fin_geom)[1])
ogeom_list = ogeom.split()
og_x = float(ogeom_list[2])
og_y = float(ogeom_list[3])
og_z = float(ogeom_list[4])

d1geom = ((fin_geom)[2])
d1geom_list = d1geom.split()
d1g_x = float(d1geom_list[2])
d1g_y = float(d1geom_list[3])
d1g_z = float(d1geom_list[4])

d2geom = ((fin_geom)[3])
d2geom_list = d2geom.split()
d2g_x = float(d2geom_list[2])
d2g_y = float(d2geom_list[3])
d2g_z = float(d2geom_list[4])


#print(cg_x,cg_y,cg_z)
#print(og_x,og_y,og_z)
#print(d1g_x,d1g_y,d1g_z)
#print(d2g_x,d2g_y,d2g_z)

#reading velocities of C,H,D1,D2
cvelo = ((fin_veloc)[0])
cvelo_list = cvelo.split()
c_x = float(cvelo_list[1])
c_y = float(cvelo_list[2])
c_z = float(cvelo_list[3])
vc = ((c_x**2.0)+(c_y**2.0)+(c_z**2.0))**0.5

ovelo = ((fin_veloc)[1])
ovelo_list = ovelo.split()
o_x = float(ovelo_list[1])
o_y = float(ovelo_list[2])
o_z = float(ovelo_list[3])
vo = ((o_x**2.0)+(o_y**2.0)+(o_z**2.0))**0.5

d1velo = ((fin_veloc)[2])
d1velo_list = d1velo.split()
d1_x = float(d1velo_list[1])
d1_y = float(d1velo_list[2])
d1_z = float(d1velo_list[3])
vd1 = ((d1_x**2.0)+(d1_y**2.0)+(d1_z**2.0))**0.5

d2velo = ((fin_veloc)[3])
d2velo_list = d2velo.split()
d2_x = float(d2velo_list[1])
d2_y = float(d2velo_list[2])
d2_z = float(d2velo_list[3])
vd2 = ((d2_x**2.0)+(d2_y**2.0)+(d2_z**2.0))**0.5

#masses
mc = 12.011
mo = 15.999
md = 2.014
totalm = mc+mo+md+md
#print(totalm)

#COM
com_x = (((cg_x*mc)+(og_x*mo)+(d1g_x*md)+(d2g_x*md))/(totalm))
com_y = (((cg_y*mc)+(og_y*mo)+(d1g_y*md)+(d2g_y*md))/(totalm))
com_z = (((cg_z*mc)+(og_z*mo)+(d1g_z*md)+(d2g_z*md))/(totalm))

#print(com_x,com_y,com_z,mc+mo+md+md,(cg_x*mc)+(og_x*mo)+(d1g_x*md)+(d2g_x*md))
#magnitude of vector along C=O is a
a = (((cg_x-og_x)**2.0)+((cg_y-og_y)**2.0)+((cg_z-og_z)**2.0))**0.5
#magnitude of vector along D1 and D2 which is y-axis
b = (((d1g_x-d2g_x)**2.0)+((d1g_y-d2g_y)**2.0)+((d1g_z-d2g_z)**2.0))**0.5


#angle with y'= unit vector along D1 and D2
phic = math.acos(((c_x*(d1g_x-d2g_x))+(c_y*(d1g_y-d2g_y))+(c_z*(d1g_z-d2g_z)))/(b*vc))
phio = math.acos(((o_x*(d1g_x-d2g_x))+(o_y*(d1g_y-d2g_y))+(o_z*(d1g_z-d2g_z)))/(b*vo))
phid1 = math.acos(((d1_x*(d1g_x-d2g_x))+(d1_y*(d1g_y-d2g_y))+(d1_z*(d1g_z-d2g_z)))/(b*vd1))
phid2 = math.acos(((d2_x*(d1g_x-d2g_x))+(d2_y*(d1g_y-d2g_y))+(d2_z*(d1g_z-d2g_z)))/(b*vd2))

#angle with z'= cross product unit vector of vectors along C=O and y-axis
alphac = math.acos(((c_x*(((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z))))+(c_y*(((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x))))+(c_z*(((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))))/(a*b*vc))
alphao = math.acos(((o_x*(((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z))))+(o_y*(((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x))))+(o_z*(((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))))/(a*b*vo))
alphad1 = math.acos(((d1_x*(((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z))))+(d1_y*(((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x))))+(d1_z*(((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))))/(a*b*vd1))
alphad2 = math.acos(((d2_x*(((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z))))+(d2_y*(((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x))))+(d2_z*(((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))))/(a*b*vd2))

#angle with x'= cross product of y'x z'

thetac = math.acos(((c_x*(((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x)))*(d1g_z-d2g_z))-((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_y-d2g_y))))+(c_y*(((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_x-d2g_x))-((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_z-d2g_z))))+(c_z*(((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_y-d2g_y))-((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_z)))*(d1g_x-d2g_x)))))/(a*(b**2.0)*vc))
thetao = math.acos(((o_x*(((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x)))*(d1g_z-d2g_z))-((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_y-d2g_y))))+(o_y*(((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_x-d2g_x))-((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_z-d2g_z))))+(o_z*(((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_y-d2g_y))-((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_z)))*(d1g_x-d2g_x)))))/(a*(b**2.0)*vo))
thetad1 = math.acos(((d1_x*(((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x)))*(d1g_z-d2g_z))-((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_y-d2g_y))))+(d1_y*(((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_x-d2g_x))-((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_z-d2g_z))))+(d1_z*(((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_y-d2g_y))-((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_z)))*(d1g_x-d2g_x)))))/(a*(b**2.0)*vd1))
thetad2 = math.acos(((d2_x*(((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_x)))*(d1g_z-d2g_z))-((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_y-d2g_y))))+(d2_y*(((((cg_x-og_x)*(d1g_y-d2g_y))-((d1g_x-d2g_x)*(cg_y-og_y)))*(d1g_x-d2g_x))-((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_z-d2g_z))))+(d2_z*(((((cg_y-og_y)*(d1g_z-d2g_z))-((d1g_y-d2g_y)*(cg_z-og_z)))*(d1g_y-d2g_y))-((((cg_z-og_z)*(d1g_x-d2g_x))-((d1g_z-d2g_z)*(cg_x-og_z)))*(d1g_x-d2g_x)))))/(a*(b**2.0)*vd2))

#final projection of velocities
v2x = vc*math.cos(thetac)*(-1.0)
v2y = vc*math.cos(phic)
v2z = vc*math.cos(alphac)

o2x = vo*math.cos(thetao)*(-1.0)
o2y = vo*math.cos(phio)
o2z = vo*math.cos(alphao)

d12x = vd1*math.cos(thetad1)*(-1.0)
d12y = vd1*math.cos(phid1)
d12z = vd1*math.cos(alphad1)

d22x = vd2*math.cos(thetad2)*(-1.0)
d22y = vd2*math.cos(phid2)
d22z = vd2*math.cos(alphad2)

pm.write("C {0:.4f}   {1:.4f}   {2:.4f}\n".format(mc*v2x,mc*v2y,mc*v2z))
pm.write("O {0:.4f}   {1:.4f}   {2:.4f}\n".format(mo*o2x,mo*o2y,mo*o2z))
pm.write("D1 {0:.4f}   {1:.4f}   {2:.4f}\n".format(md*d12x,md*d12y,md*d12z))
pm.write("D2 {0:.4f}   {1:.4f}   {2:.4f}\n".format(md*d22x,md*d22y,md*d22z))

pm.close()





