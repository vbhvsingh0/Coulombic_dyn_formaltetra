#reading geom and veloc

filegeom = open("geom").readlines()
fileveloc = open("veloc").readlines()
outputfile = open("output.txt","w")
enfile = open("en.txt","w")
coordfile = open("coords.txt","w")

#conversionfactor from printed to eV
conv_f = 42.6921

#Geom of C
a1file = ((filegeom)[0])
a1_list = a1file.split()
a2 = float(a1_list[2])
a3 = float(a1_list[3])
a4 = float(a1_list[4])

#veloc of C
f1 = ((fileveloc)[0])
f1_list = f1.split()
f2 = (float(f1_list[0]))*conv_f
f3 = (float(f1_list[1]))*conv_f
f4 = (float(f1_list[2]))*conv_f

#Geom of O
a2file = ((filegeom)[1])
a2_list = a2file.split()
b2 = float(a2_list[2])
b3 = float(a2_list[3])
b4 = float(a2_list[4])

#veloc of O
g1 = ((fileveloc)[1])
g1_list = g1.split()
g2 = (float(g1_list[0]))*conv_f
g3 = (float(g1_list[1]))*conv_f
g4 = (float(g1_list[2]))*conv_f

#veloc of H 
h1 = ((fileveloc)[2])
h1_list = h1.split()
h2 = (float(h1_list[0]))*conv_f
h3 = (float(h1_list[1]))*conv_f
h4 = (float(h1_list[2]))*conv_f

#Geom of H
a3file = ((filegeom)[2])
a3_list = a3file.split()
c2 = float(a3_list[2])
c3 = float(a3_list[3])
c4 = float(a3_list[4])

#Geom of H
a4file = ((filegeom)[3])
a4_list = a4file.split()
d2 = float(a4_list[2])
d3 = float(a4_list[3])
d4 = float(a4_list[4])

#veloc of H
i1 = ((fileveloc)[3])
i1_list = i1.split()
i2 = (float(i1_list[0]))*conv_f
i3 = (float(i1_list[1]))*conv_f
i4 = (float(i1_list[2]))*conv_f

#Equations of motions
#total time = 
time_total = 150.0

#current time
t = 0.0
step = 2.0*(0.4134 * 10**(-2))
t_step = step


while t < 12000.0 * (0.4134 * 10.0**(-2.0)):
#distances b/w atoms
	distance_co = (((a2-b2)**2.0)+((a3-b3)**2.0)+((a4-b4)**2.0))**0.5
	distance_ch1 = (((a2-c2)**2.0)+((a3-c3)**2.0)+((a4-c4)**2.0))**0.5
	distance_ch2 = (((a2-d2)**2.0)+((a3-d3)**2.0)+((a4-d4)**2.0))**0.5
	distance_oh1 = (((b2-c2)**2.0)+((b3-c3)**2.0)+((b4-c4)**2.0))**0.5
	distance_oh2 = (((b2-d2)**2.0)+((b3-d3)**2.0)+((b4-d4)**2.0))**0.5
	distance_hh =  (((d2-c2)**2.0)+((d3-c3)**2.0)+((d4-c4)**2.0))**0.5
#forces on each atom
	force_Cx = ((1.0/((distance_co)**3.0))*(a2-b2))+((1.0/((distance_ch1)**3.0))*(a2-c2))+((1.0/((distance_ch2)**3.0))*(a2-d2))
	force_Cy = ((1.0/((distance_co)**3.0))*(a3-b3))+((1.0/((distance_ch1)**3.0))*(a3-c3))+((1.0/((distance_ch2)**3.0))*(a3-d3))
	force_Cz = ((1.0/((distance_co)**3.0))*(a4-b4))+((1.0/((distance_ch1)**3.0))*(a4-c4))+((1.0/((distance_ch2)**3.0))*(a4-d4))
	force_Ox = ((1.0/((distance_co)**3.0))*(b2-a2))+((1.0/((distance_oh1)**3.0))*(b2-c2))+((1.0/((distance_oh2)**3.0))*(b2-d2))
	force_Oy = ((1.0/((distance_co)**3.0))*(b3-a3))+((1.0/((distance_oh1)**3.0))*(b3-c3))+((1.0/((distance_oh2)**3.0))*(b3-d3))
	force_Oz = ((1.0/((distance_co)**3.0))*(b4-a4))+((1.0/((distance_oh1)**3.0))*(b4-c4))+((1.0/((distance_oh2)**3.0))*(b4-d4))
	force_h1x = ((1.0/((distance_ch1)**3.0))*(c2-a2))+((1.0/((distance_oh1)**3.0))*(c2-b2))+((1.0/((distance_hh)**3.0))*(c2-d2))
	force_h1y = ((1.0/((distance_ch1)**3.0))*(c3-a3))+((1.0/((distance_oh1)**3.0))*(c3-b3))+((1.0/((distance_hh)**3.0))*(c3-d3))
        force_h1z = ((1.0/((distance_ch1)**3.0))*(c4-a4))+((1.0/((distance_oh1)**3.0))*(c4-b4))+((1.0/((distance_hh)**3.0))*(c4-d4))
	force_h2x = ((1.0/((distance_ch2)**3.0))*(d2-a2))+((1.0/((distance_oh2)**3.0))*(d2-b2))+((1.0/((distance_hh)**3.0))*(d2-c2))
	force_h2y = ((1.0/((distance_ch2)**3.0))*(d3-a3))+((1.0/((distance_oh2)**3.0))*(d3-b3))+((1.0/((distance_hh)**3.0))*(d3-c3))
        force_h2z = ((1.0/((distance_ch2)**3.0))*(d4-a4))+((1.0/((distance_oh2)**3.0))*(d4-b4))+((1.0/((distance_hh)**3.0))*(d4-c4))


#coulombic energy
	coulomb_C = (1/distance_co)+(1/distance_ch1)+(1/distance_ch2)
	coulomb_O = (1/distance_co)+(1/distance_oh1)+(1/distance_oh2)
	coulomb_h1 = (1/distance_ch1)+(1/distance_oh1)+(1/distance_hh)
 	coulomb_h2 = (1/distance_ch2)+(1/distance_oh2)+(1/distance_hh)
	coulomben_total = (coulomb_C+coulomb_O+coulomb_h1+coulomb_h2)*0.5

#Kintic Energy
	ke_C = (0.5*12.011*(((f2)**2.0)+((f3)**2.0)+((f4)**2.0)))
	ke_O = (0.5*15.999*(((g2)**2.0)+((g3)**2.0)+((g4)**2.0)))
	ke_H1 = (0.5*2.014*(((h2)**2.0)+((h3)**2.0)+((h4)**2.0)))
	ke_H2 = (0.5*2.014*(((i2)**2.0)+((i3)**2.0)+((i4)**2.0)))
	ke_total = (ke_C+ke_O+ke_H1+ke_H2)

#total energy
	energy_total = ke_total + coulomben_total

	outputfile.write("time = {0} fs\n".format(t))
	outputfile.write("Coulombic energy: {0} au\n".format(coulomben_total))
	outputfile.write("Kinetic energy: {0} au\n".format(ke_total))
	outputfile.write("Total energy: {0} au\n".format(energy_total))
	outputfile.write("\n")
	enfile.write("{0:.6f}   {1:.6f}   {2:.6f}   {3:.6f}\n".format(t,coulomben_total,ke_total,energy_total))
 	coordfile.write("{0:.3f}   {1:.6f}   {2:.6f}   {3:.6f}   {4:.6f}   {5:.6f}   {6:.6f}\n".format(t,distance_co,distance_ch1,distance_ch2,distance_oh1,distance_oh2,distance_hh))       
	
	# Calculating geometry and velocities of C for next time step

	a2 = a2+(f2*t_step)+((0.5)*(force_Cx/12.011)*(t_step**2.0))
	a3 = a3+(f3*t_step)+((0.5)*(force_Cy/12.011)*(t_step**2.0))
	a4 = a4+(f4*t_step)+((0.5)*(force_Cz/12.011)*(t_step**2.0))
	f2 = f2+((force_Cx/12.011)*t_step)
	f3 = f3+((force_Cy/12.011)*t_step)
        f4 = f4+((force_Cz/12.011)*t_step)

	# Calculating geometry and velocities of O for next time step

	b2 = b2+(g2*t_step)+((0.5)*(force_Ox/15.999)*(t_step**2.0))
        b3 = b3+(g3*t_step)+((0.5)*(force_Oy/15.999)*(t_step**2.0))
        b4 = b4+(g4*t_step)+((0.5)*(force_Oz/15.999)*(t_step**2.0))
        g2 = g2+((force_Ox/15.999)*t_step)
        g3 = g3+((force_Oy/15.999)*t_step)
        g4 = g4+((force_Oz/15.999)*t_step)

	# Calculating geometry and velocities of H1 for next time step

	c2 = c2+(h2*t_step)+((0.5)*(force_h1x/2.014)*(t_step**2.0))
        c3 = c3+(h3*t_step)+((0.5)*(force_h1y/2.014)*(t_step**2.0))
        c4 = c4+(h4*t_step)+((0.5)*(force_h1z/2.014)*(t_step**2.0))
        h2 = h2+((force_h1x/2.014)*t_step)
        h3 = h3+((force_h1y/2.014)*t_step)
        h4 = h4+((force_h1z/2.014)*t_step)

	# Calculating geometry and velocities of H2 for next time step 

	d2 = d2+(i2*t_step)+((0.5)*(force_h2x/2.014)*(t_step**2.0))
        d3 = d3+(i3*t_step)+((0.5)*(force_h2y/2.014)*(t_step**2.0))
        d4 = d4+(i4*t_step)+((0.5)*(force_h2z/2.014)*(t_step**2.0))
        i2 = i2+((force_h2x/2.014)*t_step)
        i3 = i3+((force_h2y/2.014)*t_step)
        i4 = i4+((force_h2z/2.014)*t_step)

	outputfile.write("New Geom\n")
	outputfile.write("C   {0:.4f}   {1:.4f}   {2:.4f}\n".format(a2,a3,a4))
 	outputfile.write("O   {0:.4f}   {1:.4f}   {2:.4f}\n".format(b2,b3,b4))
	outputfile.write("H   {0:.4f}   {1:.4f}   {2:.4f}\n".format(c2,c3,c4))
	outputfile.write("H   {0:.4f}   {1:.4f}   {2:.4f}\n".format(d2,d3,d4))

	outputfile.write("New Velocity\n")
	outputfile.write("C   {0:.4f}   {1:.4f}   {2:.4f}\n".format(f2,f3,f4))
	outputfile.write("O   {0:.4f}   {1:.4f}   {2:.4f}\n".format(g2,g3,g4))
	outputfile.write("H   {0:.4f}   {1:.4f}   {2:.4f}\n".format(h2,h3,h4))
	outputfile.write("H   {0:.4f}   {1:.4f}   {2:.4f}\n".format(i2,i3,i4))
	outputfile.write("       \n")
	t = t+step

outputfile.close()
enfile.close()
coordfile.close()

